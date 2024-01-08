#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import error, request


if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read().decode("utf-8")
            print(body)
    except error.HTTPError as e:
        print("Error code:", e.code)
