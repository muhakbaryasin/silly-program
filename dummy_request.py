from Scrapper import  Scrapper
from pyquery import PyQuery as pq

scrapper = Scrapper()

def collection_of_womens_name():
	list_of_name = []
	rsp_data = scrapper.requestData(url = 'https://www.babble.com/pregnancy/1000-most-popular-girl-names')
	
	if rsp_data is None:
		return list_of_name
	
	html_query = pq(rsp_data)('li.p1')
	
	for each_name in html_query:
		name = pq(each_name).text().split(" ")[0]
		if len(name) < 20:
			list_of_name.append(name)
	
	return list_of_name
	

if __name__ == "__main__":
	list_of_womens_name = collection_of_womens_name()
	
	