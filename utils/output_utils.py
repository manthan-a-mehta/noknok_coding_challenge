from collections import Counter
from utils.helpers import Helpers

def output1_render(lines,path_url_list,path_word_list):
    """
    Takes in the url path, word path and prints the top three words in all the urls of our text file

    Parameters: 
            lines(list): list of all the urls
            path_url_list: path to the file containing all the urls
            path_word_list: path to the file containing all the words
    return: 
            word_count: count of all the words across all the urls in text files            
    """
    try:
        if(len(lines)==0):
            print("There are no urls in the text file {}".format(path_url_list))
        word_count={}
        for line in lines:
            line=line.strip()
            print(line)
            helper=Helpers(line,path_url_list,path_word_list) # Defining the helper object
            dct=helper.print_sorted_list(path_word_list) # Prints the top 3 words and stores the counter for output 2 use
            print("")
            word_count=dict(Counter(word_count)+Counter(dct)) # Sums up occurences of all the words in the word file
        return word_count
    except Exception as e:
        print("There was an error {} when trying to parse list of urls {}".format(e,path_url_list))
        
    
    
