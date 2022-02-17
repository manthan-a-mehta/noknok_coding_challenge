
from utils.helpers import Helpers
from collections import Counter
import argparse
from utils.output_utils import output1_render
import sys

parser = argparse.ArgumentParser(description='Process some url')

parser.add_argument('--url_file', type=str,
                    help='path to the url file',default=None)
parser.add_argument('--word_file',type=str,
                    help='path to the word list file',default=None)

args = parser.parse_args() # Command line usability

path_url_list=args.url_file
path_word_list=args.word_file

if(path_url_list is None ):
    print("Url list is empty please enter a proper value")
    sys.exit()
    
if(path_word_list is None ):
    print("Word list is empty please enter a proper value")
    sys.exit()

lines = []
with open(path_url_list) as f: # Reading the url text file
    lines = f.readlines()

with open(path_word_list) as f:
    words=f.readlines()

## Beginning Output 1##

print("output {}".format(1))
print("==========")
print("")
word_count=output1_render(lines,path_url_list,path_word_list)
print("===========================")
print("")

## Beginning Output 2##

print("output {}".format(2))
print("==========")

try:
    ans=dict(sorted(word_count.items(), key = lambda x: x[1], reverse = True))  # Sorts the dictionary of all the words
    for k,v in ans.items():
        print(k+"- "+str(v))
except Exception as e:
    print("There was an error {} when parsing word list {}".format(e,path_word_list))