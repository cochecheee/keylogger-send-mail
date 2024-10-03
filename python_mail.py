import smtplib

class emailService:
    def __init__(self) -> None:
        pass
        
    def send_mail(self,sender_email, sender_password, receiver_email,subject=None):
        msg = 'Hello'
        smtp = 'smtp.gmail.com'
        smtp_port = 587
        session = smtplib.SMTP(smtp, smtp_port)
        session.starttls()
        session.login(sender_email,sender_password)
        session.sendmail(from_addr=sender_email,
                         to_addrs=receiver_email,
                         msg=msg)

def main():
    email = emailService();
    print(f"email {email}")
    email.send_mail(
        sender_email="pythonsendmail8@gmail.com",
        sender_password="ymunhhhojswuiaqg",
        receiver_email="buitien747@gmail.com",
        subject="Test mail"
    )

if __name__ == '__main__':
    main()