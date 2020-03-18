from flask import Flask, render_template, abort, jsonify, request, url_for

from model import wordsDB

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/word")
def word_list():
    return render_template("word_list.html", words=wordsDB)

@app.route("/word/<int:index>")
def word_view(index):
    try:
        word = wordsDB[index]
        return render_template("word.html",
                                word=word,
                                index=index,
                                max_index=len(wordsDB)-1
                                )
    except IndexError:
        abort(404)

@app.route("/api/word/")
def api_word_list():
    return jsonify(wordsDB)

@app.route('/api/word/<int:index>')
def api_word_detail(index):
    try:
        return wordsDB[index]
    except IndexError:
        abort(404)