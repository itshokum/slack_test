from flask import Flask,request
import slack

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    req_data = request.get_json()
    client = slack.WebClient(token='xoxp-614042023619-627665357718-651853951524-29a751efacdc1fa13f4f4ac233b40c93')
    response = client.conversations_history(channel='CJDEY1Q5N',limit=1)
    assert response["ok"]
     
    for resp in response["messages"]:
        if resp['type'] == "message":
            print(resp['text'])
						
    return(resp['text'])
    

		
		
if __name__ == '__main__':
    app.run(debug=True)