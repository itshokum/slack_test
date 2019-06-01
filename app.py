import os
from flask import Flask,request
import slack

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    req_data = request.get_json()
    tk = os.environ.get('slack_token')
    print(tk)
    client = slack.WebClient(token=tk)
    response = client.conversations_history(channel='CJDEY1Q5N',limit=1)
    assert response["ok"]
     
    for resp in response["messages"]:
        if resp['type'] == "message":
            print(resp['text'])
						
    return(resp['text'])
    

		
		
if __name__ == '__main__':
    app.run(debug=True)