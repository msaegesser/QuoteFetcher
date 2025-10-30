"""
fetch quotes from https://zenquotes.io/
"""

import requests
import sys
import json

class QuoteFetcher():
    """
    helper class to fetch quotes from url
    """
    _inDebug: bool = False
    _baseUrl: str = ""
    _currentQuote: dict = {"quote": str,
                           "author": str}

    def __init__(self, url) -> None:
        """
        init method
        """
        if self._inDebug:
            print(f"passed url: {url}")

        self._baseUrl = url
    
    def getRandomQuote(self) -> dict:
        """
        get a random quote from the url
        """
        req_cmd: str = self._baseUrl + "/api/random"
        if self._inDebug:
            print(f"request command: {req_cmd}")
        
        resp: requests.Response = requests.post(req_cmd)
        if self._inDebug:
            print(f"request respone: {resp}")

        return self._create_dict_from_respObject(resp)
        
    def _create_dict_from_respObject(self, respObj: requests.Response) -> dict:
        """
        creates a dict from the response object
        """
        tempDict: dict = json.loads(respObj.text)
        if self._inDebug:
            print(f"temporary dict: {tempDict}")
        
        definitveDict: dict = {"quote": tempDict[0]["q"],
                               "author": tempDict[0]["a"]}
        
        if self._inDebug:
            print(f"definitive dict: {definitveDict}")

        return definitveDict

    def print_quote(self, quote: dict) -> None:
        """
        formats and prints out the quote.
        """
        print("--- random quote ---")
        print(f'"{quote["quote"]}" - {quote["author"]}')

def main():
    """
    main entry point
    """
    baseUrl = "https://zenquotes.io/"

    # create object
    quoteFetcher: QuoteFetcher = QuoteFetcher(baseUrl)
    # get random quote
    quote: dict = quoteFetcher.getRandomQuote()
    quoteFetcher.print_quote(quote)


if __name__ == '__main__':
    sys.exit(main())