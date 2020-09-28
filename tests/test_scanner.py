import unittest
import scanner

class TestScanner(unittest.TestCase):
	"""
	First test
	"""

	def test_message(self):
		msg = scanner.message()
		self.assertIsNotNone(msg)

	def test_get_root(self):
		root_path = scanner.get_root()
		self.assertIsNot(root_path, False)