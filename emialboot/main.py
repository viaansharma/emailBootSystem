import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

licenser = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as sourse:
            print('Listening..')
            voice = licenser.listen(sourse)
            info = licenser.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sidhusharma01011999@gmail.com', 'sidhu007')
    email = EmailMessage()
    email['From'] = 'sidhusharma01011999@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {'brother': 'utkarsha817@gmail.com',
              'money': 'viaan.sharma@staqo.com',
              'good': 'piyush.jaiswal@staqo.com'
              }


def get_email_info():
    talk("To Whom you want to send email")
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject of email")
    subject = get_info()
    talk("Tell me the text in your email")
    message = get_info()
    send_email(receiver, subject, message)
    talk("hey lazy dude your email is send chack out now.")
    talk("Do you want to send more email")
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
