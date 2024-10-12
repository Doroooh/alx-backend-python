#!/usr/bin/env python3
"""a script a type-annotated function concat
that takes a string str1 and a string str2
as arguments and returns a concatenated string"""


def concat (str1:str, str2:str)-> str:
	"""_summary_

	Args:
		str1 (string): string
		str2 (string): string

	Returns:
		string: a concatenated string
	"""
	return str1 + str2
