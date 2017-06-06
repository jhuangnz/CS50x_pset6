##
#   Implement a website that generates a pie chart categorizing a user’s tweets.
# 
#   Author: Julie Huang, julie@juliehuang.co.nz
#  
#   This file contains a solution for part 3 of 'Sentiments' from pset6
# 
#   CS50x

from flask import Flask, redirect, render_template, request, url_for

import os
import sys
import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count = 100)

    positives = os.path.join(sys.path[0], "positive-words.txt")  # directory path for positives
    negatives = os.path.join(sys.path[0], "negative-words.txt")  # directory path for negatives
    
    analyzer = Analyzer(positives, negatives)  # instantiate Analyzer
    
    positive, negative, neutral = 0.0, 0.0, 0.0  # initialize scores
    
    for tweet in tweets:  # for fetched tweets
        score = analyzer.analyze(tweet)  # analyze tweet to get its score
        
        if score > 0:
            positive += 1.0  # tweet is positive, increment positive scorer
        elif score < 0:
            negative += 1.0  # tweet is negative, increment negative scorer
        else:
            neutral += 1.0  # tweet is neutral, increment neutral scorer
        
    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
