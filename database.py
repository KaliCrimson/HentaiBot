import sqlite3


conn = sqlite3.connect('db.db')
cur = conn.cursor()


conn.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT,fullname TEXT, balance INTEGER DEFAULT 20, referals INTEGER DEFAULT 0)')
conn.commit()

def add_new_user(user_id, username, fullname):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (user_id, username, fullname) VALUES (?, ?, ?)", (user_id, username, fullname))
    conn.commit()


def check_user(user_id):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  users WHERE user_id=?", (user_id,))
    conn.commit()
    return cur.fetchone()

######################################
def check_balance(user_id):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("SELECT balance FROM users WHERE user_id=?", (user_id,))
    conn.commit()
    return cur.fetchone()



async def update_balance(user_id, amount):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id,))
    conn.commit()


def update_balance_wiwod(user_id, amount):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("UPDATE users SET balance = balance - ? WHERE user_id = ?", (amount, user_id,))
    conn.commit()
##########################################


def check_wallet(user_id):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("SELECT wallet FROM users WHERE user_id=?", (user_id,))
    conn.commit()
    return cur.fetchone()


def update_wallet(user_id, wallet1):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("UPDATE users SET wallet = ? WHERE user_id = ?", (wallet1, user_id,))
    conn.commit()
#############################################
def check_referals(user_id):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("SELECT referals FROM users WHERE user_id=?", (user_id,))
    conn.commit()
    return cur.fetchone()



def update_referals(user_id, amount):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute("UPDATE users SET referals = referals + ? WHERE user_id = ?", (amount, user_id,))
    conn.commit()