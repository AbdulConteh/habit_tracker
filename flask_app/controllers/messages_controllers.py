from flask_app.models.messages_models import Message
from flask import redirect, render_template, session, request
from flask_app import app

@app.route('/send/message', methods=['POST'])
def message_box():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "sender_id" : request.form['sender_id'], 
        "receiver_id": request.form['receiver_id'], 
        "content" : request.form['content']
    }
    print("**********message",data)
    Message.create_messages(data)
    print(data['sender_id'])
    print(data['receiver_id'])
    return redirect('/profile')

@app.route('/delete/messages/<int:id>')
def delete_messages(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id" : id
    }
    print(data)
    Message.delete_message(data)
    return redirect ('/profile')