import asyncio
import contextlib
import functools
import logging
import os
import time
import unittest


class CoreTestCase(unittest.TestCase):
    def assertIsReady(self):
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()