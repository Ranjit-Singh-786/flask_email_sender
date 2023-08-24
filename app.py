from flask import Flask,request,render_template
from flask_mail import Mail,Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'smartengineer0786@gmail.com'
app.config['MAIL_PASSWORD'] = '---write your password----'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app=app)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/send_email' , methods=['GET','POST'])
def send_email():
    if request.method=='POST':
        


        msg = Message('HELLO RANJIT SINGH 💌',sender='smartengineer0786@gmail.com',recipients=['ranjitsingh97591@gmail.com'])
        msg.body = """hii welcome ranjit singh this is 
        mail with html content."""
        mail.send(message=msg)
        return render_template('index.html')
        

if __name__ =="__main__":
    app.run(debug=True)