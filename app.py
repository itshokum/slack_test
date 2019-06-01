from flask import Flask,request
import slack

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    req_data = request.get_json()
    client = slack.WebClient(token='xoxp-614042023619-627665357718-654197053223-cbd3494ae5722886db1c507e854349f2')
    response = client.conversations_history(channel='CJDEY1Q5N',limit=1)
    assert response["ok"]
     
    for resp in response["messages"]:
        if resp['type'] == "message":
            print(resp['text'])
						
    return(resp['text'])
    

		
		
if __name__ == '__main__':
    app.run(debug=True)