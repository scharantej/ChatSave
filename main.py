
# main.py

from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import db
import json

app = Flask(__name__)
app.secret_key = 'secretkey'

firebase_admin.initialize_app()
ref = db.reference('/')

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html', user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = json.loads(request.data)
    user = data['user']
    session['user'] = user
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/create-chat')
def create_chat():
    chat = ref.child('chats').push()
    user = session['user']
    chat['users'] = [user]
    chat['messages'] = []
    return chat['id']

@app.route('/get-chats')
def get_chats():
    chats = ref.child('chats').get()
    return chats

@app.route('/get-chat', methods=['POST'])
def get_chat():
    data = json.loads(request.data)
    chat_id = data['chat_id']
    chat = ref.child('chats').child(chat_id).get()
    return chat

@app.route('/send-message', methods=['POST'])
def send_message():
    data = json.loads(request.data)
    chat_id = data['chat_id']
    message = data['message']
    user = session['user']
    chat = ref.child('chats').child(chat_id)
    new_message = chat['messages'].append({'user': user, 'message': message})
    new_message.set(new_message.id)
    return new_message.id

if __name__ == '__main__':
    app.run(debug=True)
