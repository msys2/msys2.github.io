<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/rss/channel">
        <html>
            <head>
                <title><xsl:value-of select="title"/></title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                    .rss-info { background: #f0f8ff; border: 1px solid #d0e7ff; border-radius: 5px; padding: 15px; margin-bottom: 25px; }
                    .rss-info h3 { margin-top: 0; color: #0066cc; }
                    .rss-info p { margin-bottom: 8px; }
                    .rss-url { 
                        font-family: monospace; 
                        font-size: 0.9em; 
                        color: #333; 
                        background: #fff; 
                        padding: 8px; 
                        border: 1px solid #ccc; 
                        border-radius: 3px; 
                        word-break: break-all; 
                        margin: 5px 0;
                        display: block;
                    }
                    h1 { color: #333; border-bottom: 2px solid #ddd; }
                    .item { margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid #eee; }
                    .item h2 { color: #0066cc; }
                    .item h2 a { color: #0066cc; text-decoration: none; }
                    .item h2 a:hover { text-decoration: underline; }
                    .date { color: #666; font-size: 0.9em; margin-bottom: 10px; }
                    .description { line-height: 1.6; }
                </style>
            </head>
            <body>
                <div class="rss-info">
                    <h3>📡 RSS Feed</h3>
                    <p>This is a web view of an RSS feed. To subscribe to updates in your RSS reader, copy the current page URL from your browser's address bar.</p>
                </div>

                <h1><xsl:value-of select="title"/></h1>
                <p><xsl:value-of select="description"/></p>
                
                <xsl:for-each select="item">
                    <div class="item">
                        <h2>
                            <a href="{link}">
                                <xsl:value-of select="title"/>
                            </a>
                        </h2>
                        <div class="date">
                            <xsl:value-of select="pubDate"/>
                        </div>
                        <div class="description">
                            <xsl:value-of select="description" disable-output-escaping="yes"/>
                        </div>
                    </div>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>