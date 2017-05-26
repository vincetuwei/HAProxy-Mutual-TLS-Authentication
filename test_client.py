"""
    Simple Python Client used to test HAProxy Mutual SSL.
"""

import os
import requests
from requests.exceptions import SSLError
import json

URL = "https://foo.com:8443"

def main():
    test_with_cert()
    print
    print "-"*30
    print
    test_without_cert()

def test_with_cert():
    print "Test HAProxy Mutual SSL with Certificates Provided"
    os.environ["REQUESTS_CA_BUNDLE"] = os.path.abspath("certs/ca/ca.crt")
    response = requests.get(URL, verify=True, cert=('certs/client/client.crt', 'certs/client/client.key'))
    print("HTTP Status:  {}\n".format(response.status_code))

    if response.status_code == 200:
        parsed = json.loads(response.content)
        print json.dumps(parsed, indent=4, sort_keys=True)

def test_without_cert():
    print "Test HAProxy Mutual SSL without certificates"
    try:
        requests.get(URL)
    except SSLError as err:
        print("Got Error from Server: {}\n".format(err))

if __name__ == '__main__':
    main()
