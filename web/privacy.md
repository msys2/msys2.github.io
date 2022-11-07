# Privacy

## Pacman & Mirrors

In the default configuration pacman will connect to "mirror.msys2.org" when updating/installing packages and transmit the IP address, the requested file, as well as a user agent in the form of "pacman/6.0.1 (MSYS_NT-10.0-19042 x86_64) libalpm/13.0.1". This means the target server will receive the following information:

* The IP address
* The package/database requested for download
* The pacman version
* The Windows version, including the Windows build number
* The architecture of the pacman installation

"mirror.msys2.org" will then redirect the request to a [tier 1 mirror](./dev/mirrors.md) which will receive the same information again. To prevent requests going to third party mirrors you can reduce the mirror list to just "repo.msys.org".

## Logging

We log the above listed information for every request to "msys2.org", including a timestamp, and keep it for up to two weeks for the following reasons:

* Debugging and abuse detection
* Creation and publication of anonymised usage reports:
  * Overall popularity of requested packages and package types, based on the IP and request path
  * Distribution of Windows/pacman versions used, based on the user agent
  * Distribution of cloud/non-cloud users, based on the IP

For what mirrors log, store or process see their respective websites.

## Packages

Software packaged in our repository might talk to third party servers for functional, analytics, or other reasons. Please see the respective upstream documentation for details.
