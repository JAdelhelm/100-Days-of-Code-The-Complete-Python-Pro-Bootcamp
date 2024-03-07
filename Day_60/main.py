from flask import Flask, render_template, url_for, request
import requests
from email.message import EmailMessage
from email.utils import make_msgid
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
RESPONSE_BLOG = requests.get(blog_url).json()


def sent_email(name, email, phone, message):
    email_sent = ""
    password_sent = ""

    email_receiver = ""
    try:
        msg = MIMEMultipart('related')
        msg["Subject"] = f"Blog - Nachricht von {name}"
        msg["To"] = email_receiver

        msg_context = f"""<html><body>
        <p>Name:</br>{name}</p>
        <p>Email:</br>{email}</p>
        <p>Phone:</br>{phone}</p></br>
        <p>Message:</br>{message}</p>
                        </body>"""
        
        msg.attach(MIMEText(msg_context, 'html'))
        # Sending the email
        server = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
        server.login(user=email_sent, password=password_sent)
        server.send_message(msg)
        server.quit()

    except Exception as e:
        print(e)




@app.route("/")
def index():
    image_url = url_for('static', filename='assets/img/home-bg.jpg')
    return render_template("index.html", image_url=image_url, json_with_posts=RESPONSE_BLOG)

@app.route("/home")
def home():
    image_url = url_for('static', filename='assets/img/home-bg.jpg')
    return render_template("index.html", image_url=image_url, json_with_posts=RESPONSE_BLOG)

@app.route("/about")
def about():
    image_url = url_for('static', filename='assets/img/about-bg.jpg')
    return render_template("about.html", image_url=image_url)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    image_url = url_for('static', filename='assets/img/contact-bg.jpg')
    if request.method == "POST":
        sent_email(
            name = request.form["name"], 
            email = request.form["email"], 
            phone = request.form["phone"], 
            message = request.form["message"])
        
        return render_template("contact.html", sent_message=True, image_url=image_url)
    else:
        return render_template("contact.html", sent_message=False, image_url=image_url)

@app.route("/post/<int:clicked_post_id>")
def blog_post(clicked_post_id):
    response_post_with_id = RESPONSE_BLOG[clicked_post_id-1]

    return render_template("post.html", id_of_post=response_post_with_id)







if __name__ == "__main__":
    app.run(debug=True)