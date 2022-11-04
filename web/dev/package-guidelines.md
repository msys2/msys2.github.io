# Package Guidelines

## Applying git patches

Git patches should be applied in `prepare()`. Since the build system doesn't have a committer configured and we generally try to avoid changing the git history because that distorts the input for a later `pkgver()` call, we apply patches without committing:

* Use `git apply` to apply a git patch without creating a commit
* In case of a git checkout use `git cherry-pick --no-commit` to backport a commit without creating a commit.

## Release Signing Keys

### What to do when a new release is signed with a new key?

Visit the upstream website or other official communication channels and verify that the new key is an official release signing key.

While at it you can also verify that `validpgpkeys` does not contain inactive signing keys. If a key in `validpgpkeys` seems unused, either because the person upstream switched to a new key, or if the key isn't listed upstream anymore please remove it from `validpgpkeys`.
