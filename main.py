from email.mime import base
import os
import user_controller
from flask import Flask, jsonify, request
from db import db
import base64

################ TODO:
# try PRAGMA foreign_keys

app = Flask(__name__)

####################### User

@app.route('/register', methods=['POST'])
def register():
    auth_user = request.authorization.username
    auth_password = request.authorization.password

    ## Use this if Authorization header is used.
    # Example: 'Authorization': 'Basic <base64 of username:password>'

    # auth = request.headers.get('Authorization')
    # #decode base64
    # auth_split = auth.split(' ')
    # base64_bytes = auth_split[1].encode('ascii')
    # message_bytes = base64.b64decode(base64_bytes)
    # message = message_bytes.decode('ascii')

    # print (f'Decoded auth: {message}')

    result = user_controller.insert_user(auth_user, auth_password)

    return result, 200

@app.route('/deleteuser/<id>', methods=['DELETE'])
def delete(id):

    ## Use this if Authorization header is used.
    # Example: 'Authorization': 'Basic <base64 of username:password>'

    # auth = request.headers.get('Authorization')
    # #decode base64
    # auth_split = auth.split(' ')
    # base64_bytes = auth_split[1].encode('ascii')
    # message_bytes = base64.b64decode(base64_bytes)
    # message = message_bytes.decode('ascii')

    # print (f'Decoded auth: {message}')

    result = user_controller.delete_user(id)

    return result, 200

if __name__ == "__main__":
    db.create_tables()

    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)