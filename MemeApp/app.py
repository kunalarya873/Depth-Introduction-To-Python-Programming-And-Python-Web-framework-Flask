from flask import Flask, render_template
import json
import requests
app = Flask(__name__)
def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url).text)
    meme_url = response["url"]
    subreddit = response['subreddit']
    return meme_url, subreddit


@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == '__main__':
    app.run(debug=True)