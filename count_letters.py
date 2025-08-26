#!/usr/bin/env python3

import sys
from typing import Optional


def read_text_from_args_or_stdin() -> Optional[str]:
	"""Return input text from CLI args, stdin, or None if interactive input is needed."""
	if len(sys.argv) > 1:
		return " ".join(sys.argv[1:])

	# If data is piped in, read it non-interactively
	if not sys.stdin.isatty():
		data = sys.stdin.read()
		return data.rstrip("\n")

	return None


def count_letters(text: str) -> int:
	"""Count unicode letters in text (letters from any alphabet)."""
	return sum(1 for ch in text if ch.isalpha())


def main() -> None:
	text = read_text_from_args_or_stdin()
	if text is None:
		try:
			text = input("Введите предложение: ")
		except EOFError:
			text = ""

	print(count_letters(text))


if __name__ == "__main__":
	main()