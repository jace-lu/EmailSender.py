import smtplib
import optparse
from email.mime.text import MIMEText



def sendMail(user, pwd, receiver, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = receiver
    msg['Subject'] = subject

    try:
        print("[+] Connecting To Mail Server.")
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print("[+] Starting Encrypted Session.")
        smtpServer.ehlo()
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server.")
        smtpServer.login(user, pwd)
        print("[+] Sending Mail.")
        smtpServer.sendmail(user, receiver, msg.as_string())
        print("sent")
        print("[+] Mail Sent Successfully.")
    except:
        print("[-] Sending Mail Failed.")


def main():
    parser = optparse.OptionParser('usage%prog ' + \
                                   '-t <target email> ' + \
                                   '-l <gmail login> -p <gmail password>')
    parser.add_option('-t', dest='tgt', type='string', \
                      help='specify target email')
    parser.add_option('-l', dest='user', type='string', \
                      help='specify gmail login')
    parser.add_option('-p', dest='pwd', type='string', \
                      help='specify gmail password')
    (options, args) = parser.parse_args()

    tgt = options.tgt
    user = options.user
    pwd = options.pwd

    if tgt == None or user == None or pwd == None:
        print(parser.usage)
        exit(0)

    spamMsg = "Place whatever message you want here" 
    subject = "PLace whatever suvject you want here"
    sendMail(user, pwd, tgt, subject, spamMsg)


if __name__ == '__main__':
    main()
