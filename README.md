# Password checker using `haveibeenpwned` API

## How it works
> Your entered password is encrypted using SHA-1 hashing
> The first five characters of the hash is sent to the `haveibeenpwned` API
> Response containing all breached password hashes is searched for your hash
> You get a response telling you if your password has been pwnd or not