#!/usr/bin/python3
""" A Python script that takes in a URL and an email, 
sends a POST request to the passed URL with the email as a parameter, 
and displays the body of the response (decoded in utf-8)"""


import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('UTF-8'))
