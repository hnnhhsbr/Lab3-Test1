#!/usr/bin/env python

import wikipedia
import sys
import requests

def extract_links(url):
	page = wikipedia.page(sys.argv[-1])
	links = []

	for link in page.links:
		links.append({"page":link})
	
	return links

if __name__ == "__main__":
    	if len(sys.argv) != 2:
            print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))
	    sys.exit(1)	
	for link in extract_links(sys.argv[-1]):
		print ("[{}]".format(link["page"]))
