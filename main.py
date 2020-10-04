#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image

#def remove_data()

def main():
	for files in sys.argv[1:]:
		try:
			with Image.open(files) as img:
				print("Filename: %s\nFormat: %s\nSize: %s\nMode: %s" % (files, img.format, img.size, img.mode))
		except OSError:
			pass


if __name__ == "__main__": main()