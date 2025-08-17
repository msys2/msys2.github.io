#!#!/usr/bin/env python3
# Converts the news page to an RSS feed

import os
import base64
import re
import argparse
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET
from urllib.parse import urljoin


def extract_canonical_url(soup):
    """Extract the canonical URL from the HTML content"""

    canonical_link = soup.find("link", rel="canonical")
    if canonical_link and canonical_link.get("href"):
        return canonical_link["href"]
    return None


def make_urls_absolute(soup, base_url):
    """Convert relative URLs to absolute URLs in the HTML content"""

    # Handle links
    for link in soup.find_all("a", href=True):
        link["href"] = urljoin(base_url, link["href"])

    # Handle images
    for img in soup.find_all("img", src=True):
        img["src"] = urljoin(base_url, img["src"])

    return soup


def html_to_rss(html_content, feed_title, feed_description):
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract page URL from canonical link
    page_url = extract_canonical_url(soup)
    if not page_url:
        raise ValueError("No canonical URL found in the HTML content")

    print(f"Found canonical URL: {page_url}")

    # Convert relative URLs to absolute
    soup = make_urls_absolute(soup, page_url)

    # Create RSS root structure
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    # Channel metadata
    ET.SubElement(channel, "title").text = feed_title
    ET.SubElement(channel, "link").text = page_url
    ET.SubElement(channel, "description").text = feed_description
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "lastBuildDate").text = datetime.now().strftime(
        "%a, %d %b %Y %H:%M:%S +0000"
    )

    # Find all h3 entries (news items)
    h3_tags = soup.find_all("h3", id=True)

    for h3 in h3_tags:
        # Extract date and title from h3
        h3_id = h3.get("id", "")
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", h3_id)

        if not date_match:
            print(f"Skipping h3 with id '{h3_id}' - no valid date found")
            continue

        date_str = date_match.group(1)

        # Get title text (remove any code tags for cleaner title)
        title_text = h3.get_text().strip()
        # Remove the date prefix from title
        title_clean = re.sub(r"^\d{4}-\d{2}-\d{2}\s*-\s*", "", title_text)

        # Collect content paragraphs until next h3
        content_parts = []
        current = h3.next_sibling
        while current and current.name != "h3":
            content_parts.append(str(current))
            current = current.next_sibling
        content = "".join(content_parts)

        # Create RSS item
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = title_clean

        # Use the actual page URL for link and guid, not just the base URL
        item_url = f"{page_url}#{h3_id}"
        ET.SubElement(item, "link").text = item_url
        ET.SubElement(item, "guid").text = item_url

        # Convert date to RFC 822 format
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        rfc_date = date_obj.strftime("%a, %d %b %Y 00:00:00 +0000")
        ET.SubElement(item, "pubDate").text = rfc_date

        # Add content as CDATA
        description = ET.SubElement(item, "description")
        description.text = content

    # Embed XSLT stylesheet
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xsl_file = os.path.join(script_dir, "news2rss.xsl")
    with open(xsl_file, 'r', encoding='utf-8') as f:
        xsl_content = f.read()
    xsl_b64 = base64.b64encode(xsl_content.encode('utf-8')).decode('ascii')
    data_uri = f"data:text/xsl;base64,{xsl_b64}"

    xml_str = ET.tostring(rss, encoding="unicode")
    full_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    full_xml += f'<?xml-stylesheet type="text/xsl" href="{data_uri}"?>\n'
    full_xml += xml_str
    return full_xml


def main():
    parser = argparse.ArgumentParser(description="Convert HTML page to RSS feed")
    parser.add_argument(
        "-f", "--file", help="Path to the HTML file to convert", required=True
    )
    parser.add_argument("-o", "--output", help="Output RSS file path", required=True)
    parser.add_argument("--title", help="RSS feed title", default="MSYS2 News")
    parser.add_argument(
        "--description",
        help="RSS feed description",
        default="MSYS2 project news and updates",
    )

    args = parser.parse_args()
    print(f"Reading HTML from file {args.file}...")
    with open(args.file, "r", encoding="utf-8") as f:
        html_content = f.read()

    print("Converting to RSS feed...")
    rss_content = html_to_rss(html_content, args.title, args.description)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(rss_content)

    print(f"RSS feed saved to {args.output}")


if __name__ == "__main__":
    main()
