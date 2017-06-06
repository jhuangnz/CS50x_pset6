##
#   Implement a website that generates a pie chart categorizing a user’s tweets.
# 
#   Author: Julie Huang, julie@juliehuang.co.nz
#  
#   This file contains a solution for part 3 of 'Sentiments' from pset6
# 
#   CS50x

import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        self.negatives = set()  # empty set for storing words from negatives
        self.positives = set()  # empty set for storing words from positives
        
        self.positive_infile = open(positives, "r")  # opens positives and returns file pointer
        if positives == None:                        
            exit("invalid positives directory path")  # exit if unable to open positives
        
        line = self.positive_infile.readline()  # read first line of positives
        
        while line != "":  # loop until EOF indicated by ""
            if line.startswith(";") == False:  # skip lines starting with ";"
                line = line.strip("\n")  # strip newline
                self.positives.add(line)  # add word to self.positives
                
            line = self.positive_infile.readline()  # read next line
        
        self.positive_infile.close()  # close positives
        
        if "" in self.positives:
            self.positives.remove("")  # if "" in self.positives, remove
        
        self.negative_infile = open(negatives, "r")  # opens negatives and returns file pointer
        if negatives == None:
            exit("invalid negatives directory path")  # exit if unable to open negatives
        
        line = self.negative_infile.readline()  # read first line of negatives
        
        while line != "":  # loop until EOF indicated by ""
            if line.startswith(";") == False:  # skip lines starting with ";"
                line = line.strip("\n")  # strip newline
                self.negatives.add(line)  # add word to self.negatives
                
            line = self.negative_infile.readline()  # read next line 
        
        self.negative_infile.close()  # close negatives
        
        if "" in self.negatives:
            self.negatives.remove("")  # if "" in self.negatives, remove
        
        # DEBUGGING ONLY print("positives = {}".format(self.positives), "\n, \n", "negatives = {}".format(self.negatives))
        # DEBUGGING ONLY print("words in self.positives = {}".format(len(self.positives)))
        # DEBUGGING ONLY print("words in self.negatives = {}".format(len(self.negatives)))

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
    
        tracker = 0  # keeps score of tweet sentiment
        
        tokenizer = nltk.tokenize.TweetTokenizer() # instantiate TweetTokenizer
        tokens = tokenizer.tokenize(text) # tokenize text (returns list of strings, a word for each string)
        
        for i in range(len(tokens)):  # for each token(word) in tokens(the tokenized text)
            tokens[i] = tokens[i].lower()  # change all letters to lower case
            if "\n" in tokens[i]:
                tokens[i] = tokens[i].strip("\n")  # strip if newline character in token
            
            if tokens[i] in self.positives:  # if word in positives, increment score
                tracker += 1
            elif tokens[i] in self.negatives: # if word in negatives, decrement score
                tracker -= 1
            else:
                tracker = tracker # if word in neither positives or negatives, no change to score
                
        return tracker  # return final score

           
