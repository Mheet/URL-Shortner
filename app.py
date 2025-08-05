import sqlite3
import random
import string
from flask import Flask, render_template, g, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-should-be-a-real-secret'


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
    
    db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            db = get_db()
            long_url = request.form['long_url']
            custom_alias = request.form['custom_alias']

            if custom_alias:
                short_code = custom_alias
            else:
                short_code = generate_short_code()

            try:
                db.execute(
                    'INSERT INTO urls (long_url, short_code) VALUES (?, ?)',
                    [long_url, short_code]
                )
                db.commit()

                new_link = url_for('redirect_to_url', short_code=short_code, _external=True)
                return render_template('index.html', new_link=new_link)

            except sqlite3.IntegrityError:
                flash('That custom alias is already taken! Please choose another.')


    return render_template('index.html')


@app.route('/<short_code>')
def redirect_to_url(short_code):

    db = get_db()

    url_data = db.execute(
        'SELECT long_url FROM urls WHERE short_code = ?', [short_code]
    ).fetchone()

    if url_data:
        long_url = url_data['long_url']
        return redirect(long_url)

    else:
        return "URL not found!", 404
    

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')