from pymongo import MongoClient
from email_validator import validate_email
import string
import random
import smtplib


def sendmail(too, hash):
    gmail_user = 'torrleechs@gmail.com'
    gmail_password = ''
    sent_from = gmail_user
    to = too
    subject = 'Mail to verify!'
    body = f'Link for verification is https://024x.eu.org/verify?hash={hash}'
    email_text = """\
From: %s
To: %s
Subject: %s




%s

""" % (sent_from, ", ".join(to), subject, body)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()


client = MongoClient(
    'mongodb+srv://user:pass@clusterX.xxxx.mongodb.net/dbname?retryWrites=true&w=majority'
)
db = client.Apk
collection = db.user


def regist(id, mail, pas):
    validate_email(mail).email
    hash = ''.join(random.choices(string.ascii_letters, k=15))
    sendmail(mail, hash)
    collection.insert_one({
        '_id': id,
        'email': mail,
        'pass': pas,
        'is_verified': False,
        'hash': hash,
    })
    return {'status': 'signup Successful Please check your mail and verify!'}


def verif(hash):
    #collection.findOne({'hash': hash})
    collection.update_one({'hash': hash}, {'$set': {'is_verified': True}, '$unset':{'hash':hash}}  )
    return {'status': 'Verified!'}
