# Meme Generator

This app is a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. Our content team spent countless hours writing quotes in a variety of filetypes.

This app is both a command line tool and a web interface as a Flask web app.

User inputs are:
- Image URL
- Body of the meme
- Author of the meme

## Required Libraries

All required libraries are in the ```requirements.txt``` file.

Use the following command to install in a new virtual environment
```pip install -r requirements.txt```

## Running the web app

Use the following command to run the Flask app
```flask run --host 0.0.0.0 --port 3000 --reload```

You can then access the app on the address http://0.0.0.0:3000


## Running the Command-Line Interface tool

The project contains a simple cli app ```meme.py```. The utility can be which can be run from the terminal by invoking ```python3 meme.py```

The script must take three optional CLI arguments:

```--body``` a string quote body
```--author``` a string quote author
```--path``` an image path
The script returns a path to a generated image. If any argument is not defined, a random selection is used.