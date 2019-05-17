import json

from myrepolib.repomod import fake_data
from myrepolib import __version__

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return f"This is what i really wanted to write  {__version__}"

@app.route("/fakedata")
def fakedata():
    return json.dumps(fake_data())


if __name__ == "__main__":
    app.run()
