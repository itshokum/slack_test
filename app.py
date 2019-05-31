from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    req_data = request.get_json()
    return(req_data.get('challenge'))
    

		
		
if __name__ == '__main__':
    app.run(debug=True)