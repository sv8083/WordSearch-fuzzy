import operator
from django.apps import apps

app_config = apps.get_app_config('fuzzy_search')
words= app_config.words
word_count= app_config.word_count

def search_query(word_letter):
	'''
    Search function to check the input(partial) word is present in any word of words list.
    Parameters:
        word_letter: Input from user
    Returns list of available words
    '''
	results= []
	for word in words:
		if word_letter in word:
			results.append(word)
	return results

def sort_query(results, word):
	'''
	Sorts and returns the result as follows:
		Matches at the start of a word ranks higher.
		Common words (those with a higher usage count) ranks higher than rare words.
		Short words ranks higher than long words.
		An exact match always ranks as the first result.
	Parameters
		results: list of result received from search function
		word: word received from user
	Returns:
	'''
	result_distances = [(result, result.find(word), word_count[result], len(result)) for result in results]
	result_distances.sort(key=operator.itemgetter(1))
	result_distances.sort(key=operator.itemgetter(3))
	searchResults = [result_distance[0] for result_distance in result_distances][:25]
	return searchResults
