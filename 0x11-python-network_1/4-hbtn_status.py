#!/usr/bin/python3
"""
fetche inside an url and requests model
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'
resp = requests.get(url)
print('Body response:')
print('\t- type:', type(resp.text))
print('\t- content:', resp.text)
