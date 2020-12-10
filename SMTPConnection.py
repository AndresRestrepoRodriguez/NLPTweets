import smtplib


class SMTPConnection:

    def __init__(self):
        self._server = "smtp.gmail.com"
        self._port = 587
        self._sender = "parallud2019@gmail.com"
        self._password = "cudanvidia2019"
        self._connectionSMTP = None

    def setConnectionSMTP(self, connectionSMTP):
        if connectionSMTP is None:
            self._connectionSMTP = smtplib.SMTP(self._server, self._port)
        else:
            self._connectionSMTP = connectionSMTP

    def getConnectionSMTP(self):
        return self._connectionSMTP
