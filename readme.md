# Brief Description of the Task 1:
The task is to request urls and find the top **3** most frequently occuring words in a list of webpages and display them in decreasing order of their frequency. 
# Brief Description of the Task 2:
The task is to find the occurences of all the words in a text file and display them in a decreasing order of their frequency across all the urls.
# Setup and Installations:

### Creating a virtual environment and activating it.

#### Run the following from the terminal from within the noknok_cc folder 


**These commands are for a linux system. The commands were run on ubuntu 20.04 version.**

#### 1) Run the following commands from the command line.
```
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
**Make sure you run the following command inside the noknok_cc folder which is the zipped file**

#### 2) Select the interpreter by going to view->command palette->select interpreter.
**Now select the python interpreter that is corresponding to your virtual environment.**

# Folder Structure:
noknok_cc
 ┣ utils
 ┃ ┣ helpers.py
 ┃ ┗ output_utils.py
 ┣ Coding Challenge 2022.pdf
 ┣ main.py
 ┣ readme.md
 ┣ urls.txt
 ┗ words.txt
 
 The files **helpers.py** and **output_utils.py** contain the core functionality of the project. Description of each of the functions is given in the files itself. The files **urls.txt** contains the list of urls and **words.txt** contains the list of words to be queried.
 
 # Libraries used:
requests: Sends a get, put, or post request to the requested url
collections: Package used to convert a dictionary to counter for easy addition of two dictionaries.
argparse: To get the command line inputs and fpass these values to the required functions.

# Running the python file
To run the program after the libraries have been installed run the following command from inside the folder **noknok_cc**:

```
$ python main.py --url_file <path_to_your_url_file> --word_file  <path_to_your_word_file>
```




 
 