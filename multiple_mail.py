from flask import Flask, request, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'smartengineer0786@gmail.com'
app.config['MAIL_PASSWORD'] = "###"   # 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app=app)

def get_data_structure(folder_path):
    list_of_items = os.listdir(folder_path)

    data = []
    
    for item in list_of_items:
        if item.endswith("png"):
            data_item = dict()
            student_name , user_name = item.split('-')
            file_path = os.path.join(folder_path,item)

            #username editing
            username = user_name[0:-4]
            email_id = username

            data_item['name'] = student_name
            data_item['email'] = email_id
            data_item['file_path'] = file_path
            data_item['file_name'] = item
            data.append(data_item)
        else:
            print(f"Keep This file in another folder {item}")
    return data


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        folder_path = str(request.form['folder_path'])
        subject = str(request.form['subject'])
        content = str(request.form['body'])
        sender_name = "Siddharth Singh"

        data = get_data_structure(folder_path)

        for student in data:
            student_name = student['name']
            student_email = student['email']
            msg = Message(subject, sender='smartengineer0786@gmail.com', recipients=[student_email])
            msg.body = f"Dear {student_name},\n\n {content}.\n\nBest Regards Team Upflairs,\n{sender_name} \nUpflairs Pvt. Ltd. Jaipur Rajsthan\n6350417917"

        # Attach image


            img_path = student['file_path']
            with app.open_resource(img_path) as img:
                msg.attach(filename=student['file_name'], content_type='image/png', data=img.read())
            
            mail.send(message=msg)
        return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
