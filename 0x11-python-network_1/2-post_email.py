#!/usr/bin/python3
""" A Python script that takes in a URL and an email, 
sends a POST request to the passed URL with the email as a parameter, 
and displays the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    # Check if both URL and email are provided
    if len(argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
    else:
        url = argv[1]
        email = argv[2]
        # Encode email as ASCII
        data = urllib.parse.urlencode({"email": email}).encode("ascii")
        # Create POST request with encoded email data
        request = urllib.request.Request(url, data)
        # Send request and retrieve response
        with urllib.request.urlopen(request) as response:
            # Decode and print response body
            print(response.read().decode("utf-8"))

