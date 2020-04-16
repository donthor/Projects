#!/usr/bin/env python3
"""Retrieve and print words from a URL

Usage:
    python3 words.py <URL>
"""
import sys
from collections import Counter
from urllib.request import urlopen
def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document
        
    Returns:
        A list of strings containing the words from the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line

    Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)

def occurDict(items):
    d = {}
    for i in items:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d

def main(url):
    """Prints each word from a text document from a URL

    Args:
        url: The URL of a UTF-8 text decument
    """
    words = fetch_words(url)
    print_items(words)
    print()
    print(Counter(words))
    print()
    print(occurDict(words))

if __name__ == '__main__':
    print(sys.argv[0])
    main(sys.argv[1]) #The 0th argument is the module filename