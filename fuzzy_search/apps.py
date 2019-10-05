from django.apps import AppConfig


class FuzzySearchConfig(AppConfig):
    name = 'fuzzy_search'
    verbose_name = "Application to perform fuzzy searches"
    
    def __init__(self, app_name, app_module):
        super(self.__class__, self).__init__(app_name, app_module)
        self.words= []
        self.word_count= {}

    def ready(self):
        '''
        This function is called once server is up and runnning.
	    Reads Tab comma Separated files stores the words
        '''
        with open('word_search.tsv') as datafile:
            for row in datafile:
                word= row.split('\t')[0] 
                frequency = row.split('\t')[1]
                self.word_count[word] = int(frequency.strip())
                self.words.append(word)
        
        print("Collecting words from TSV file complete")
        
        
