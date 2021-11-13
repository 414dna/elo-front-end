from flask import Flask,render_template,request,flash
from requests.models import HTTPError
from backend_api import auth1, user1
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('front.html')
@app.route('/confirm',methods=['POST','GET'])
def confirm():
    if request.method=='POST':
        # n=request.form.get('uname')
        mail=request.form.get('mail')
        password=request.form.get('psw')
        print(f'/{mail}/{password}')
        try:
            resp=auth1(email=mail,password=password)
        except HTTPError:
            flash('Invalid password provided error')
            return 'efef'
        if resp['registered']:
            
            return render_template('nodepg.html')
@app.route('/login',methods=['POST','GET'])
def login():
    noder=request.form.get('node')
    macr=request.form.get('mac')
    user1(node=noder,id=macr)
    return 'done'

if __name__ == '__main__':
    app.run(debug=True)
