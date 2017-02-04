from flask import Flask, request, redirect
from credentials import ACCOUNT_SID, AUTH_TOKEN, MY_CELL, MY_TWILIO
from twilio.rest import TwilioRestClient

import twilio.twiml 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
app = Flask(__name__)

# Sending message test
client.messages.create(
    to=MY_CELL, 
    from_=MY_TWILIO, 
    body=_body, 
    media_url=_media_url, 
)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/send_sms")
def send_sms(_body, _media_url):
	client.messages.create(
    to=MY_CELL, 
    from_=MY_TWILIO, 
    body=_body, 
    media_url=_media_url, 
)

# @app.route("/", methods=['GET','POST'])
# def response(_body, _media_url):
# 	resp = twilio.twiml.Response()

# 	if (_media_url == None):
# 		resp.message(_body)
# 	else:
# 		with resp.message(_body) as m:
# 			m.media(_media_url)

# 	return str(resp)

@app.route('/twilio',methods=['POST'])
def twilio_post():
	resp = twiml.Response()
	if request.form['From'] == MY_CELL:
		message = request.form['Body']
		# handle message;
	return Response(resp.toxml(), mimetype="text/xml"), 200

if __name__ == "__main__":
    app.run(debug=True)