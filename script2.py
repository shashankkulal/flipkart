from BeautifulSoup import BeautifulSoup
from html2text import html2text
import urllib2
from texttable import Texttable

search = raw_input("Enter company name, color or model : ")
search = search.replace(' ', '+')

def make_url():
	url = "http://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&filterNone=true&q="+ search +"&otracker=start"
	open_url(url)


def open_url(url):
	pname = []
	price = []
	text = urllib2.urlopen(url).read()
	soup = BeautifulSoup(text)
	
	data = soup.findAll('div', attrs = {'id':'products'})
	for div in data:
		temp_div = div.findAll('div', attrs = {'class':'gd-col gu3'})
		for temp in temp_div:
			p1 = """%s""" % str(temp.findAll('a', attrs = {'class':'fk-display-block'}))
			p1 = p1.replace('\n', '')
			soup = BeautifulSoup(p1)
			pname.append(soup.text)
			p2 = """%s""" % str(temp.findAll('span', attrs = {'class':'fk-font-17 fk-bold'}))
			p2 = p2.replace('\n', '')
			soup = BeautifulSoup(p2)
			price.append(soup.text)
	combine_list(pname,price)
	
def combine_list(pname,price):
	c = zip(pname,price)
	c.insert(0,('Phone Name','Price'))
	t = Texttable()
	t.add_rows(c)
	print t.draw()


make_url()
