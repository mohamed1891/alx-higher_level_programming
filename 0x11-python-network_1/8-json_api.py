#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""


if __name__ == "__main__":
    from requests import post
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = post(url, data={'q': q})

    resp_type = response.headers['content-type']

    if resp_type and 'application/json' in resp_type:
        result = response.json()
        if result:
            print("[{}] {}".format(result['id'], result['name']))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
