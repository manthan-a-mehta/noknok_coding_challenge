import requests
from collections import Counter

class Helpers():
    def __init__(self,url,url_path,word_path):
        """
        Initializes the helper class.

        Parameters:
                  url(str): url for the website to be scraped
                  url_path(str): path of the text file containing all urls
        """
        self.url=url
        self.url_path=url_path
        self.word_path=word_path
    
    def get_word_count(self,word):
        """
        Counts the occurence of the word in the url contained in class variable url

        Parameters:
                  word(str): word whose count needs to be calculated
        Returns: 
                  word count(int): frequency of the word in the text attribute of the url
        """
        try:
            text=requests.get(str(self.url)).text
            text,word=text.lower(),word.lower()
            wordslist = list(str(text).split())
            return wordslist.count(word)
        except Exception as e:
            print("There was some error {} during requesting url {}".format(e,self.url))
    
    def get_all_word_count(self,path_words):
        """
        Calculates occurence of all the words in a particular url for all the words in a text file

        Parameters:
                  path_words(str): Path of text file containing all the words to be queried
        Returns: 
                  dct(dictionary): dictionary of the form {word:count} for all the words in the text file.
        """
        lines = []
        
        try:
           with open(path_words) as f:
               lines = f.readlines()
           dct={}
           for word in lines:
               word=word.strip()
               dct[word]=self.get_word_count(word)
           return dct
        
        except Exception as e:
            print("There was some error {} during querying file {}".format(e,path_words))
            if(len(lines==0)):
                print("There are no words in the file specified in the path{}".format(path_words))
            
    
    def print_sorted_list(self,path_words):
        """
        Prints the words in decreasing order of their frequency

        Parameters:
                  path_words(str): Path of the text file contating all the words
        Returns: 
                  cache(dictionary): dictionary containing count of all the words in the text file
        """
        word_count=self.get_all_word_count(path_words)
        cache=word_count.copy()
        word_count=Counter(word_count)
        for k,v in word_count.most_common(3):
            print("{}-".format(k),v)
        return cache




   


