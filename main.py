import requests

url = input("Enter url: ")

if not url.startswith("http://") or not url.startswith("https://"):
    url = "http://" + url
    print("Modified URL:", url)


print()



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
    ]

    missingHeaders = []
    ownedHeaders = []
    recommendedHeaders = []

    for header in expectedHeaders:
        if header not in headers:
            missingHeaders.append(header)
            recommendedHeaders.append(get_recommendation(header))

        else:
            ownedHeaders.append(header)

    if ownedHeaders:
        print("Available Headers:")
        for header in ownedHeaders:
            print(f"- {header}")
    else:
        print("No headers available!")

    print()

    if missingHeaders:
        print("Missing Headers:")
        for header in missingHeaders:
            print(f"- {header}")

        print("\nRecommended Headers:")
        for recommendation in recommendedHeaders:
            print(f"- {recommendation}")

    else:
        print("All headers available.")




def get_recommendation(header):
    if header == 'Cache-Control':
        return "Consider setting Cache-Control header to control caching behavior."
    elif header == 'Connection':
        return "Use Connection header to specify whether the connection should be closed after the request."
    elif header == 'Date':
        return "Include the Date header in your response to provide information about when the response was generated."
    elif header == 'Host':
        return "Specify the Host header to indicate the domain name of the server."
    elif header == 'User-Agent':
        return "Include a User-Agent header to identify the client making the request."
    elif header == 'Accept':
        return "Use the Accept header to indicate the media types that the client can process."
    elif header == 'Authorization':
        return "Include the Authorization header for authenticating the request."
    elif header == 'Location':
        return "When using redirection, include the Location header with the URL to redirect to."
    elif header == 'Server':
        return "Specify the Server header to indicate the server software and version."
    elif header == 'Content-Type':
        return "Include the Content-Type header to specify the media type of the response content."
    elif header == 'Content-Length':
        return "Specify the Content-Length header to indicate the size of the response content in bytes."
    elif header == 'Strict-Transport-Security':
        return "Implement Strict-Transport-Security to enhance security by enforcing secure connections."
    elif header == 'X-Content-Type-Options':
        return "Use X-Content-Type-Options header to prevent browsers from MIME-sniffing a response."
    elif header == 'X-Frame-Options':
        return "Protect against clickjacking attacks by including the X-Frame-Options header."
    elif header == 'Content-Security-Policy':
        return "Enhance security by implementing Content-Security-Policy to control resource loading."

    return "No recommendation found for the specified header."


func_get_headers(url)
