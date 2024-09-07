# urlshortener

Implement a Python command line tool that performs URL shortening and expansion.\
The tool has two primary functions:
1. Given a complete URL, return a shortened URL.
2. Given a shortened URL, return the complete URL.

The shortened URLs has an expiration time of N seconds; once the time has passed, the link should no longer be valid for the expand
command, but the original url could be minified again.\
Command parameters:
1. Parameter --minify=https://www.example.com/path?q=search
2. Parameter --expand=https://myurlshortener.com/fstp4

If a complete URL has already been shortened and is not expired, the tool should return the same shortened URL.\
If a shortened URL doesn’t exist or is expired, it should return an appropriate message.