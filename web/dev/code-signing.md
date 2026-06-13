# Code Signing

A summary of how things are set up currently for code signing in MSYS2 and how to reproduce it.

* Signing is handled via ["Azure Artifact
Signing"](https://azure.microsoft.com/en-us/products/artifact-signing).
* Christoph (@lazka) has it set up on his personal Azure account, and it costs
  ~€8.60 a month for the basic model. If we want to move to signing all binaries
  we likely need to move to the premium model which is 10x that.
* The costs are currently sponsored by Microsoft for 2026 (would also cover
  premium), but the sponsorship requires yearly renewal so there are no
  guarantees for the future. The sponsorship was initiated via @dscho.

## How to Set up Azure Artifact Signing

A good guide is
https://www.hanselman.com/blog/automatically-signing-a-windows-exe-with-azure-trusted-signing-dotnet-sign-and-github-actions,
though we use "Federated credentials", so auth happens via GitHub Actions OIDC,
and not secret token. And replace "Trusted Signing" with "Artifact Signing"
everywhere since Microsoft rebranded it since the blog post was written.

Most resources can't be renamed after creation, so make sure to pick a good
naming scheme from the start.

Short overview of the resources:

* An Azure Subscription - Handles billing. This was created automatically via the
  sponsorship.
* A Resource Group - A container for the resources below. Part of the subscription.
* Artifact Signing Account - The thing that handles signing and costs money.
    * Identity validation - This is a one-time process to validate the identity
      of yourself.
    * Certificate Profile - The cert used for signing.
* App registration - A thing which has permissions to sign with the Artifact
  Signing Account.
    * Federated credentials - Allows GitHub Actions to authenticate to Azure via
      OIDC.

## Identity Validation

Identity validation requires:

* You need to be a citizen of one of the allowed countries (if not, ask
  @dscho)
* Your name and address, taken from the Azure billing section
    * Search for "Cost Management + Billing" in Azure, then "Properties", then
      "Sold-to address". Make sure this matches your ID and proof of residency.
* A government issued ID
* A proof of residency document
* A phone with MS Authenticator installed
* A front-facing camera, for selfies

MS outsources identity validation to https://www.au10tix.com.

Steps (as far as I can remember):

* You create an "Identity validation" in Azure
* Follow the link to the AU10TIX site, which then moves your to your phone
* Take photos of everything with your phone and hope it is happy (it took
  multiple tries for me)
* Install the MS Authenticator app to scan some QR code to get a verified ID
  (you don't need to be logged in, in MS Authenticator)
* Back on Azure scan a QR code with the MS Authenticator app
* This then opens another Azure thing which requires another selfie
* Then your identity verification in Azure should show as "completed". It takes
  a few minutes for the status to update though, so be patient.

## Technical Details

Signing currently happens automatically via GHA in https://github.com/msys2/msys2-installer.

If a job runs in the "msys2/msys2-installer" repo, in the "sign-env" environment
(which is tied to the protected "main" branch), and has "id-token" permissions,
it can create an OIDC token and use it to authenticate with Azure as the "App
registration". The "App registration" has permissions to sign with the "Artifact
Signing Account".

The signing requires an endpoint, account name, singing profile, client id, and
tenant id. All of these could be public as knowing them does not allow signing,
but we keep them secret anyway.

For signing binaries we use [aas-sign](https://github.com/skeeto/aas-sign). For
verifying signatures we use
[osslsigncode](https://github.com/mtrojnar/osslsigncode). Both are cross
platform and open source.

An alternative that only works on Windows would be
[dotnet/sign](https://github.com/dotnet/sign) and
[Get-AuthenticodeSignature](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-authenticodesignature).
See [this
PR](https://github.com/git-for-windows/git-for-windows-automation/pull/165) for
a Windows set up used by git-for-windows.