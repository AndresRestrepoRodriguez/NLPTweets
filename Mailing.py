from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from SMTPConnection import SMTPConnection


class Mailing:

    def __init__(self):
        self._sender = "xxxxx@gmail.com"
        self._password = "password"
        self._body = "Prueba de correo"
        self._subject = "Subject prueba"
        self._receiver = ""
        self._smtpConnection = SMTPConnection()

    def setReceiver(self, receiver):
        self._receiver = receiver

    def getReceiver(self):
        return self._receiver

    def getSender(self):
        return self._sender

    def getPassword(self):
        return self._password

    def getBody(self):
        return self._body

    def getSubject(self):
        return self._subject

    def sendEmail(self, receiver, pathPdf, connection):
        self.setReceiver(receiver)
        message = MIMEMultipart()
        message['From'] = self.getSender()
        message['To'] = self.getReceiver()
        message['Subject'] = self.getSubject()
        message.attach(MIMEText(self.getBody(), 'plain'))
        binary_pdf = open(pathPdf, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pathPdf)
        payload.set_payload(binary_pdf.read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pathPdf)
        message.attach(payload)
        self._smtpConnection.setConnectionSMTP(connection)
        session = self._smtpConnection.getConnectionSMTP()
        session.starttls()
        session.login(self.getSender(), self.getPassword())
        text = message.as_string()
        try:
            session.sendmail("andrescisf29@gmail.com", self.getReceiver(), text)
            mailState = True
        except:
            mailState = False
        session.quit()
        return mailState



