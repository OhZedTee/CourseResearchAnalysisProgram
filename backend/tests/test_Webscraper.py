from bs4 import BeautifulSoup
import os
import sys

from src.WebScrape import scraper

from unittest.mock import patch
from unittest import TestCase
import unittest

class MainTest(TestCase):

	#test to see if scrape returns a hashmap
	def test_valid_scrape(self):
		scrapeHash = scraper("tests/data/Section_Selection_Results___WebAdvisor___University_of_Guelph.html")
		self.assertTrue(scrapeHash)

	#test to see if the length of the object matches the test file
	def test_scraper_hash_length(self):
		scrapeHash = scraper("tests/data/Section_Selection_Results___WebAdvisor___University_of_Guelph.html")
		self.assertEqual(len(scrapeHash),30)

	def test_key_exists(self):
		scrapeHash = scraper("tests/data/Section_Selection_Results___WebAdvisor___University_of_Guelph.html")
		keyExists = False;
		if "CIS-1500" in scrapeHash:
			keyExists = True;
		self.assertTrue(keyExists)

	def test_key_does_not_exist(self):
		scrapeHash = scraper("tests/data/Section_Selection_Results___WebAdvisor___University_of_Guelph.html")
		keyExists = False;
		if "VETM-4500" in scrapeHash:
			keyExists = True;
		self.assertFalse(keyExists)

if __name__ == '__main__':
    unittest.main()