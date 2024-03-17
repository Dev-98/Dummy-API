from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hallo, ich bin Dev"

@app.route('/resume',methods=['GET','POST'])
def resume():

    try :

        files = request.files['resume']

        if files:

            a = {'analytics': "The provided resume lacks relevant experience and skills for the Java Developer role. To improve the resume, it should highlight Java-related projecthe resume's matching potential.",
                'score': "40%",
                'jobs': [{'name': "Avarri",'stipend':"₹ 5,000-7,000 /month",'link':"https://internshala.com/internship/detail/nodejs-development-internship-in-mumbai-at-nextgen-techno-ventures-private-limited1709554501"},
                        {'name': "Yarri",'stipend':"₹ 50,000-70,000 /month",'link':"https://internshala.com/internship/detail/nodejs-development-internship-in-mumbai-at-nextgen-techno-ventures-private-limited1709554501"},
                        {'name': "Gwarri",'stipend':"₹ 500-700 /month",'link':"https://internshala.com/internship/detail/nodejs-development-internship-in-mumbai-at-nextgen-techno-ventures-private-limited1709554501"},
                        {'name': "Berojgarri",'stipend':"₹ 5 /month",'link':"https://internshala.com/internship/detail/nodejs-development-internship-in-mumbai-at-nextgen-techno-ventures-private-limited1709554501"}
                        ]}
            
            return jsonify(a), 200
        
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080))) 
