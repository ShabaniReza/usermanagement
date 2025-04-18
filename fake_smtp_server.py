import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Receiving message from:', peer)
        print('From:', mailfrom)
        print('To:', rcpttos)
        print('Message data:\n')
        print(data.decode())  # نمایش محتوای ایمیل
        return

def run_fake_smtp_server():
    server = CustomSMTPServer(('localhost', 1025), None)
    print("Fake SMTP server started on localhost:1025")
    asyncore.loop()

if __name__ == '__main__':
    run_fake_smtp_server()