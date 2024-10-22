import sqlite3


def initiate_db():
    """Создаёт таблицу Products, если она ещё не создана."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создание таблицы Products
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        price INTEGER NOT NULL
                    )''')

    conn.commit()
    conn.close()


def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Получение всех продуктов из таблицы
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products


def add_product(title, description, price):
    """Добавляет продукт в базу данных."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Добавление продукта
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (title, description, price))

    conn.commit()
    conn.close()


# Пример: добавление продуктов в базу
if __name__ == "__main__":
    initiate_db()  # Создание таблицы при первом запуске

    # Добавление нескольких продуктов
    add_product("Продукт1", "Описание 1", 100)
    add_product("Продукт2", "Описание 2", 200)
    add_product("Продукт3", "Описание 3", 300)
    add_product("Продукт4", "Описание 4", 400)
