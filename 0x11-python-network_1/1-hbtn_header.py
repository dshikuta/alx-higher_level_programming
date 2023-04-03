#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response."""

if _name_ == '_main_':
    import sys
    import urllib.request
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        url_res = response.info()
        print(url_res['X-Request-Id'])
