from flask import Flask, render_template, abort, jsonify, request, url_for, redirect
from model import wordsDB, save_db
from datetime import datetime
import random

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
@app.route("/word/random")
def random_word():
    try:
        random.seed(datetime.now())
        index = random.randint(0, len(wordsDB) - 1)
        word = wordsDB[index]
        return render_template("word.html",
                                word=word,
                                index=index,
                                max_index=len(wordsDB) - 1
                                )
    except IndexError:
        abort(404)

@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    try:
        if request.method == "POST":
            # Form has been submitted and needs processing
            card = {"phrase": request.form['phrase'],
                    "difficulty": request.form['difficulty']}
            wordsDB.append(card)
            save_db()
            return redirect(url_for('word_view', index=len(wordsDB)-1))
        else:
            return render_template("add_card.html")
    except IndexError:
        abort(404)

@app.route("/remove_card/<int:index>", methods=["GET", "POST"])
def remove_card(index):
    if request.method == "POST":
        del wordsDB[index]
        save_db()
        return redirect(url_for('welcome'))
    else:
        return render_template("remove_card.html", word=wordsDB[index])

@app.route("/api/word/")
def api_word_list():
    return jsonify(wordsDB)

@app.route('/api/word/<int:index>')
def api_word_detail(index):
    try:
        return wordsDB[index]
    except IndexError:
        abort(404)