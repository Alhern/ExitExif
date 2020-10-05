#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image, ExifTags

#def remove_data()

def main():
	f = input("Please enter your image's filename: ")
	try:
		with Image.open(f) as img:
			print("Filename: %s\nFormat: %s\nSize: %s\nMode: %s" % (f, img.format, img.size, img.mode))
			data = img._getexif()
			if (data == None):
				print("No EXIF data.")
			else:
				print("Raw EXIF:\n%s\n" % data)
				print("Decoded EXIF:")
				for key, val in data.items():
					if key in ExifTags.TAGS:
						print("%s: %s" % (ExifTags.TAGS[key], repr(val)))
	except OSError:
		pass


if __name__ == "__main__": main()