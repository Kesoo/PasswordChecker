# Password checker using `haveibeenpwned` API

## How it works
1. Run: `python3 checkPassword.py`
2. Enter the password you want to check
3. Your entered password is encrypted using SHA-1 hashing
4. The first five characters of the hash is sent to the `haveibeenpwned` API
5. Response containing all breached password hashes is searched for your hash
6. You get a response telling you if your password has been pwnd or not

* [haveibeenpwned API](https://haveibeenpwned.com/API/v3)