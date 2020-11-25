"""
    send_mail.py: a module that, you guessed it, sends mail through an SMTP server. 
    There is a base function (basic_send_mail)
"""
import json
import smtplib, ssl
with open("../secret.json", "r") as fp:
    SECRETS = json.load(fp)['email']

def basic_send_mail(
    smtp_server_url, 
    port, 
    sender_email, 
    password, 
    receiver_email,
    message
):
    print(f"server: {smtp_server_url}, port: {port}, {type(port)}")
    with smtplib.SMTP_SSL(smtp_server_url, port) as server:
        print("########################################################")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def send_myweb_mail(receiver_email, message):
    basic_send_mail(
        SECRETS['smtp_server'],
        SECRETS['port'],
        SECRETS['username'],
        SECRETS['password'],
        receiver_email,
        message
    )

if __name__ == "__main__":
    send_myweb_mail("jamie.segeren@icloud.com", """\
Subject: hey there 

Like my new email?""")