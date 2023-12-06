import requests

def func_get_headers(url):

    headers = requests.get(url).headers


    # https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
    expectedHeaders = [
        'Cache-Control',
        'Connection',
        'Date',
        'Host',
        'User-Agent',
        'Accept',
        'Authorization',
        'Location',
        'Server',
        'Content-Type',
        'Content-Length',
        'Strict-Transport-Security',
        'X-Content-Type-Options',
        'X-Frame-Options',
        'Content-Security-Policy',
        'TESTTESTTEST'
    ]

    missingHeaders = []
    ownedHeaders = []

    for header in expectedHeaders:
        if header not in headers:
            missingHeaders.append(header)
        else:
            ownedHeaders.append(header)

    # return headers.get("Cache-Control")
    #return headers
    print("Data: ", headers)
    print()
    print("Expected Headers: ", expectedHeaders)
    print()
    print("Missing Headers: ", missingHeaders)
    print()
    print("Owned Headers ", ownedHeaders)
    print()
    print(headers.get("Date"))
    print()
    print(headers.get("Connection"))




func_get_headers("https://www.google.com")


