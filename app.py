# Flask Packages
from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

# NLP Packages
from textblob import TextBlob, Word
import random
import time

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse', methods=['POST'])
def analyse():
    start=time.time()
    # check for features
    if request.method == 'POST':
        rawtext = request.form['rawtext']   # takes a raw import form HTML form
        blob = TextBlob(rawtext)    # change the rawtext import a blob
        received_text = blob    # make a copy of the blob to be used as received text
        blob_sentiment = round(blob.sentiment.polarity,3)    # assigned polarity
        blob_subjectivity = round(blob.sentiment.subjectivity,3) # assign subjectivity
        number_of_tokens = len(list(blob.words))    # check for number of words
        nouns = list()
        # extracting main point from raw text
        for word, tag in blob.tags:
            if tag == 'NN':
                nouns.append(word.lemmatize())
                len_of_words = len(nouns)
                rand_words = random.sample(nouns, len(nouns))
                final_word = list()
                for item in rand_words:
                    word = Word(item).pluralize()
                    final_word.append(word)
                    summary = final_word
                    end = time.time()
                    final_time = round(end-start, 3)
        return render_template(
            'index.html',received_text=received_text,number_of_tokens=number_of_tokens,
            blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity,summary=summary,final_time=final_time
        )



if __name__=='__main__':
    app.run(debug=True)