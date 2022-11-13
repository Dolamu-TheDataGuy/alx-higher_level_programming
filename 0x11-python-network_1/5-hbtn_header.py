#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""
import requests
import sys


if __name__ == "__main__":
    #made the request get with the url
    #r = requests.get(sys.argv[1])
    r = requests.get(sys.argv[1])
    # used the headers.get to get requests
    #req = r.headers.get("X-Request-Id")
    #print(req)
    print(r.headers.get("X-Request-Id"))
