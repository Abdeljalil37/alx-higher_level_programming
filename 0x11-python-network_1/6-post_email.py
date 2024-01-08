#!/usr/bin/python3
"""A  script that:
- takes in a URL and an email address
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    # Send a POST request with the email parameter
    payload = {'email': email}
    resp = requests.post(url, data=payload)

    print(resp.text)
