import smtplib
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        send_email(data['name'], data['email'], data['message'])
        return render_template('landing.html', msg_sent=True)
    return render_template('landing.html', msg_sent=False)

def send_email(name, email, message):
    email_message  = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        connection.sendmail(app.config['MAIL_USERNAME'], 'barrowmuminatou@gmail.com', email_message)

@app.route('/home', methods=['POST'])
def handle_form_submission():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    send_email(name, email, message)
    return render_template('landing.html')


if __name__ == "__main__":
    app.run(debug=True)

 
