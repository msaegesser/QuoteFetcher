"""
fetch quotes from https://zenquotes.io/
"""

import requests
import sys
import json

def create_dict_from_respObject(respObj: requests.Response) -> dict:
    """
    creates a dict from the response object
    """
    return json.loads(respObj.text)

def print_quote(quote: dict):
    """
    formats and prints out the quote.
    """
    print("--- random quote ---")
    print(f'"{quote["q"]}" from {quote["a"]}')

def fetch_quote(url: str) -> requests.Response:
    """
    simple quote fetch function
    """
    return requests.post(url)

def main():
    """
    main entry point
    """
    url = "https://zenquotes.io/api/random"
    
    quote = fetch_quote(url)

    print_quote(create_dict_from_respObject(quote)[0])


if __name__ == '__main__':
    sys.exit(main())