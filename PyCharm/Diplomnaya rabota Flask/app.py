from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)


# Модель игры
class Game:
    def __init__(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image


# Игры
shooter_games = [
    Game("Shooter Game 1", "Описание шутера 1", "static/images/shooter1.jpg"),
    Game("Shooter Game 2", "Описание шутера 2", "static/images/shooter2.jpg"),
    Game("Shooter Game 3", "Описание шутера 3", "static/images/shooter3.jpg"),
    Game("Shooter Game 4", "Описание шутера 4", "static/images/shooter4.jpg"),
    Game("Shooter Game 5", "Описание шутера 5", "static/images/shooter5.jpg"),
]

racing_games = [
    Game("Racing Game 1", "Описание гонки 1", "static/images/racing1.jpg"),
    Game("Racing Game 2", "Описание гонки 2", "static/images/racing2.jpg"),
    Game("Racing Game 3", "Описание гонки 3", "static/images/racing3.jpg"),
    Game("Racing Game 4", "Описание гонки 4", "static/images/racing4.jpg"),
    Game("Racing Game 5", "Описание гонки 5", "static/images/racing5.jpg"),
]

strategy_games = [
    Game("Strategy Game 1", "Описание стратегии 1", "static/images/strategy1.jpg"),
    Game("Strategy Game 2", "Описание стратегии 2", "static/images/strategy2.jpg"),
    Game("Strategy Game 3", "Описание стратегии 3", "static/images/strategy3.jpg"),
    Game("Strategy Game 4", "Описание стратегии 4", "static/images/strategy4.jpg"),
    Game("Strategy Game 5", "Описание стратегии 5", "static/images/strategy5.jpg"),
]

cart = []

# Создание базы данных
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        age = int(request.form['age'])

        if age < 18:
            flash("Ваш возраст менее 18 лет, регистрация запрещена")
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Такой пользователь уже зарегистрирован")
            return redirect(url_for('register'))

        new_user = User(username=username, password=password, age=age)
        db.session.add(new_user)
        db.session.commit()
        flash("Регистрация успешна!")
        return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/games')
def games():
    return render_template('games.html', shooter=shooter_games, racing=racing_games, strategy=strategy_games)


@app.route('/add_to_cart/<game_title>')
def add_to_cart(game_title):
    cart.append(game_title)
    flash(f"{game_title} добавлена в корзину!")
    return redirect(url_for('games'))


@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)


if __name__ == '__main__':
    app.run(debug=True)
