import wikipediaapi
import pickle


def link_func(topic): 
	
	# take a certain category/topic and returns a list of articles


	wiki_wiki = wikipediaapi.Wikipedia('en')
	main_page = wiki_wiki.page(topic)

	related_articles = [main_page.text]

	for link in main_page.links: # iterate over all possible links that are connected to this page
		pages = wiki_wiki.page(link).text
		related_articles.append(pages)
		print(link)
		if len(related_articles)>1000:
			break

	return related_articles

topics = dict({
	'Switzerland':[],
	'Human':[],
	'Education':[],
	'Law':[],
	'Religion':[],
	'Music':[],
	'Technology':[],
	'Artificial Intelligence':[]	
})


for top in topics.keys():
	top_articles = link_func(top) 
	topics[top] = top_articles

with open('corpus.pickle', 'wb') as handle:
	pickle.dump(topics,handle, protocol=2)





























