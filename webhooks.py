from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms():
    resp = MessagingResponse()
    resp.message("Thanks for the Python message. I will get back to you")
    print(str(resp))
    return str(resp)
