import requests

from udemy.web_scraping.scrapping_website.pages.quote_pages import QuotePages

page_content= requests.get('http://quotes.toscrape.com/').content
page = QuotePages(page_content)

# print(page)
for e in page.Quotes:
	print(e.content)