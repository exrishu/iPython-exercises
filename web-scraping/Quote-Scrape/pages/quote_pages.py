from bs4 import  BeautifulSoup

from udemy.web_scraping.scrapping_website.locators.quote_page_locator import QuotePageLocators
from udemy.web_scraping.scrapping_website.parsers.quote import QuoteParser

class QuotePages:
	def __init__(self,page):
		self.soup = BeautifulSoup(page,'html.parser')


	@property
	def Quotes(self):
		locator = QuotePageLocators.QUOTE
		quote_tags = self.soup.select(locator)
		return [QuoteParser(e) for e in quote_tags]
