from flask import Flask,request
app = Flask(__name__)
import os
import mongo as m



@app.route("/",methods=['GET'])
def read_root():
    return {'status':'working'}
@app.route("/register/",methods=['GET'])
def register():
    _id = request.args.get('uid', None)
    mail = request.args.get('mail', None)
    pas = request.args.get('pass', None)
    try:
        return dict(m.regist(_id,mail,pas))
    except Exception as e:
        print(e)
        return {'status': 'Error!, Contact admin'}

@app.route('/verify/',methods=['GET'])
def verify():
    hash = request.args.get('hash', None)
    #return m.verif(hash)
    try:
        return m.verif(hash)
    except Exception as e:
        print(e)
        return {'status': 'Error!, Contact admin'}
    
@app.route('/send')
def send():
    return {
        "this is a test":"test"
    }
        
app.run(host='0.0.0.0', port=81)

        
          