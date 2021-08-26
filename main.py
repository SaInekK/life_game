from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)

'''Прошу прощения за съехавший счетчик - не знаю, как его поправить:)'''
@app.route('/index')
@app.route('/')
def index():
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


if __name__ == "__main__":  # Запуск вебсервера
    app.run(debug=True)
