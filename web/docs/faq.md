# FAQ

### How can I get MSYS2 running under Wine?

Wine fails to run Cygwin binaries and as a result MSYS2 and Git for Windows, which are based on Cygwin. See the following bug reports for the current state of things:

* https://github.com/msys2/MSYS2-packages/issues/682
* https://github.com/git-for-windows/git/issues/3478
* https://bugs.winehq.org/show_bug.cgi?id=40528

It might require fixes in both Wine and Cygwin to get resolved. If anyone makes some progress on this, let us know!

### How can I make MSYS2/pacman trust my company's custom TLS CA certificate

In case your computer is managed by an organization they might MITM all your TLS connections and install their own custom CA certificate onto your system so that MITM connections are still marked as secure. Because OpenSSL in MSYS2 currently doesn't integrate with the Windows system CA store, and thus doesn't know about your organization's custom certificates you have to add them and trust them manually.

You might be affected if you see the following errors when using pacman, curl or similar:

* `SSL certificate problem: unable to get local issuer certificate`
* `SSL certificate problem: self signed certificate in certificate chain`

First we need to get the certificates of your organization

1) via Firefox:

* Open https://repo.msys2.org in Firefox (the connection should be marked as secure!)
* Press ctrl+i to open the page info
* Go to "Security" and click "View Certificate"
* Go through all tabs where the certificate belongs to your organization, scroll down and click on "PEM (cert)" to download the "*.pem" file

2) or via Chrome/Chromium/Edge:

See https://stackoverflow.com/a/70398349

3) or by asking your IT department to give you the certificates.

Now that we have the certificate files, we copy them into MSYS2 and register them:

* Open a MSYS2 shell
* Place the .pem/.cer files into `/etc/pki/ca-trust/source/anchors`
* Run `update-ca-trust` (there is no output)

Now TLS connections to the MSYS2 repo should work:

```bash
$ curl --fail --silent --show-error -I https://repo.msys2.org -o /dev/null && echo "OK!"
OK!
```

The certificates can be removed again by deleting the .pem/.cer files in `/etc/pki/ca-trust/source/anchors` and running `update-ca-trust` again.

### How long are old packages kept on repo.msys2.org?

1.75 years after a package version leaves the pacman package database, it is removed from the server. This means that if you do not update the pacman DB for more than 1.75 years, the installation of packages may fail until you update.

External projects that rely on specific package versions on the repo server are advised to mirror those packages if the above retention policy does not meet their needs.

### What does "magic number mismatch detected" mean?

msys2 is a fork of cygwin and uses a pinned memory address to allow coordination between different executables running in the same environment. This memory format is determined by a "magic number" header at the top of the pinned memory address to ensure that corrupted memory is not read. While having multiple copies of the msys2 dll running at the same time is not necessarily a problem, what is a problem is having multiple versions that write different versions to the same space (or if that pinned memory gets rebased and accessed in a wrong way).

For this reason, the following scenarios can cause a address memory mismatch:

1. Address randomization being turned on for the initial program or dll
2. A program loading multiple versions of msys2 with mismatched magic numbers
3. A program loading multiple versions of msys2 and forcing the dll to be address rebased
4. A separate program loading msys2 in

Since a lot of command line tools pack msys2 with them to provide a nice operating scenario then you may need to make sure that these are aligned correctly. For this reason, make sure to be using compatible versions of msys2 with other components
