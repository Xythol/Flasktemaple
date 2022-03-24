from db import db
import hashlib
from secrets import token_bytes
from json import dumps

def insert_user(name, password):
    try:
        salt = token_bytes(16).hex()
        password_salt = password + salt
        encoded_ps = password_salt.encode()
        encrypted_ps = hashlib.sha256(encoded_ps).hexdigest()

        # Insert into users table
        cursor = db.conn.cursor()
        sql = "INSERT INTO users(name, password, salt) VALUES (?, ?, ?)"
        cursor.execute(sql, [name, encrypted_ps, salt])
        db.conn.commit()
        user_id = cursor.lastrowid

        # Creating session token and put in user_sessions table
        session_token = token_bytes(16).hex()
        sql = "INSERT INTO user_sessions(user_id, token) VALUES (?, ?)"
        cursor.execute(sql, [user_id, session_token])
        db.conn.commit()

        # Constructing the json to return to the client
        return_dict = {}
        message = f'{name} is insert into users table with id: {user_id}'
        return_dict['message'] = message
        return_dict['session_token'] = session_token

        return dumps(return_dict)
    except db.conn.Error as error:
        print ("Error while running insert_user", error)
    
def update_user(id, password):
    try:
        salt = token_bytes(16).hex()
        password_salt = password + salt
        encoded_ps = password_salt.encode()
        encrypted_ps = hashlib.sha256(encoded_ps).hexdigest()

        cursor = db.conn.cursor()
        sql = """
                UPDATE users 
                SET password = ?,
                    salt = ?
                WHERE id = ?                
            """
        cursor.execute(sql, [encrypted_ps, salt, id])
        db.conn.commit()
        return f'{cursor.rowcount} rows updated from games table.'

    except db.conn.Error as error:
        print ("Error while running update_game", error)

def get_user():
    try:
        cursor = db.conn.cursor()
        sql = """
                SELECT * FROM users
            """
        cursor.execute(sql)
        return cursor.fetchall()
    except db.conn.Error as error:
        print ("Error while running get_user", error)

def delete_user(id):
    try:
        cursor = db.conn.cursor()
        sql = """
                DELETE FROM users
                WHERE id = ?
            """
        cursor.execute(sql, [id])
        db.conn.commit()
        return f'{cursor.rowcount} rows deleted from games table.'
    except db.conn.Error as error:
        print ("Error while running delete_game", error)