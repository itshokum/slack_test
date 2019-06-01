from flask import Flask,request
import slack

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    req_data = request.get_json()
    client = slack.WebClient(token='xoxp-614042023619-627665357718-619191220513-e5cd817b97126dc3ab32b90b88e66b2f')
    response = client.conversations_history(channel='CJDEY1Q5N',limit=1)
    assert response["ok"]
     
    for resp in response["messages"]:
        if resp['type'] == "message":
            print(resp['text'])
						
    return(resp['text'])
    

		
		
if __name__ == '__main__':
    app.run(debug=True)