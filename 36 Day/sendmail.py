# %%
import requests
from datetime import datetime
import inspect
import textwrap
from email.message import EmailMessage
import smtplib

class SendEmail():
    def __init__(self,dict_of_companies_messages) -> None:
        self.dict_of_companies_messages = dict_of_companies_messages

        self.dict_is_not_empty = bool(self.dict_of_companies_messages)
        self._mail_message = ""

        self.create_mail_message()

    @property
    def mail_message(self):
        return self._mail_message
    
    def create_mail_message(self):
        """
        Send Mails via PythonAnywhere: https://www.pythonanywhere.com/
        """
        for key,value in self.dict_of_companies_messages.items():
            self._mail_message += f"\n\n{self.dict_of_companies_messages[key]}\n"

        self._mail_message = inspect.cleandoc(self._mail_message)
        self._mail_message = textwrap.dedent(self._mail_message)


    def send_mails(self, to_addrs_mail, your_email, your_password):
        if self.dict_is_not_empty ==True:
                    ### Send E-Mail to yourself ###
            msg = EmailMessage()
            msg.set_content(self._mail_message)

            msg["Subject"] = "Starke Aktienerhöhung/Verringerung!"
            # msg["From"] = your_email
            msg["To"] = to_addrs_mail

            server = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
            server.login(user=your_email, password=your_password)
            server.send_message(msg)
            server.quit()
        else:
            # Send no mails
            raise ValueError("Dictionary of companies is empty.")