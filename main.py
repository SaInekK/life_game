from flask import Flask, render_template, request, redirect, url_for, flash
from project.forms import MessageForm
from game_of_life import GameOfLife
import os

app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


class Config(object):
    SECRET_KEY = os.environ.get("SECRET KEY") or "any_key"


app.config.from_object(Config)


@app.route('/index', methods=["POST", "GET"])
@app.route('/', methods=["POST", "GET"])
def index():
    height = 25
    width = 25
    if request.method == 'POST':
        height = request.form.get('height')
        width = request.form.get('width')
        if height.isdigit() and width.isdigit():
            GameOfLife(int(height), int(width)).generate_universe()
            return redirect(url_for('life'))
        else:
            flash('Enter 2 numbers')
    GameOfLife(25, 25).generate_universe()
    return render_template('index.html')


@app.route('/life/')
@app.route('/life')
def life():
    game = GameOfLife()
    if game.generation > 0:
        game.form_new_generation()
    game.generation += 1
    return render_template('life.html.j2', world=game.world, old_world=game.old_world, counter=game.generation)


@app.route('/static/')
@app.route('/static')
def stat():
    game = GameOfLife()
    if game.generation > 0:
        game.form_new_generation()
    game.generation += 1
    return render_template('life-static.html.j2', world=game.world, old_world=game.old_world, counter=game.generation)


@app.route('/message', methods=["POST", "GET"])
@app.route('/message/', methods=["POST", "GET"])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name, email, message, sep='/n')
        print("\nData received. Now redirecting...")
        return redirect(url_for('message'))

    return render_template('message.html.j2', form=form)


if __name__ == "__main__":  # Запуск вебсервера
    app.run(debug=True)
