import random
import os
import requests
from flask import Flask, render_template, abort, request

from modules.MemeGenerator import MemeEngine
from modules.QuoteEngine import QuoteModel, Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []

    for root, dirs, files in os.walk(images_path):
        for name in files:
            imgs.append(os.path.join(root, name))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    url, body, author = request.form

    img = requests.get(url, allow_redirects=True)

    file = f"./static/{random.randint(0, 100000000)}.jpg"
    open(file, 'wb').write(img.content)

    path = meme.make_meme(file, body, author)

    os.remove(file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
