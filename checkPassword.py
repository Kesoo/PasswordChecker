import requests
import hashlib
from getpass import getpass

# Define constants
URL = 'https://api.pwnedpasswords.com/range/'

def checkPassword():
    #Get password from user
    password = getpass('Enter password to check: \n')

    #Hash the password
    passwordHash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    #Send first five characters of hash to API
    hashPrefix = passwordHash[0 : 5]
    response = requests.get(URL + hashPrefix)
    
    #Check response for matches
    checkHashes(response.text, hashPrefix, passwordHash)
    return

def checkHashes(apiResponse, hashPrefix, passwordHash):
    
    #For each line in response
    for line in apiResponse.splitlines():

        #Split at : store [0] as hash and add prefix, store [1] as numberOfBreaches
        hashAndNumber = line.split(':')
        hashToCheck = hashPrefix + hashAndNumber[0]
        numberOfBreaches = hashAndNumber[1]

        #Check if hash matches password, if it matches return numberOfBreaches, else return
        if hashToCheck == passwordHash:
            print('Change your password! \nYour password has been breached and found in ' + numberOfBreaches + ' different places!')
            return

    print('Your password is still (probably) secure!')

#Do the thing
checkPassword()
