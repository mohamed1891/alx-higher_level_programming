#!/usr/bin/python3
"""sends a POST request to the passed URL
with the email as a parameter, and
finally displays the body of the response.
"""


if __name__ == "__main__":
    from requests import post
    import sys

    url = post(sys.argv[1], {'email': sys.argv[2]})
    print(url.text)
