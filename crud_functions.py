import sqlite3


def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        price INTEGER NOT NULL
                    )''')

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products


def add_product(title, description, price):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (title, description, price))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initiate_db()

    add_product("Продукт1", "Описание 1", 100)
    add_product("Продукт2", "Описание 2", 200)
    add_product("Продукт3", "Описание 3", 300)
    add_product("Продукт4", "Описание 4", 400)
