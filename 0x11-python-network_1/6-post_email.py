#!/usr/bin/python3
"""a POST request sent  to the passed URL
with the email as a parameter,
and finally displays the body of the response."""

if __name__ == "__main__":
    import sys
    import requests

    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
