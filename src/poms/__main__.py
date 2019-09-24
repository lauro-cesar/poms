import argparse
import asyncio
import os
import signal
import sys
import threading
import websockets


def main() -> None:
	parser = argparse.ArgumentParser(prog="python3 -m poms",description="Interactive client.",add_help=False)
	parser.add_argument("uri", metavar="<uri>")
	args = parser.parse_args()


if __name__ == "__main__":
	main()