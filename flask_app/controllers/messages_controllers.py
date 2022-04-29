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
    # print("**********message",data)
    Message.save(data)
    message = data['content']
    print(message)
    return redirect('/profile')

