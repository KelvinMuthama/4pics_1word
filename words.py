import sqlite3

def all_words():
    # create a connection with the db
    conn = sqlite3.connect('eng_words.db')

    # Create a cursor object
    cur = conn.cursor()

    # Execute sql commands
    table = cur.execute('SELECT word FROM english_words')
    all_rows = table.fetchall()
    english_words = {word for (word,) in all_rows}

   
    return english_words
    