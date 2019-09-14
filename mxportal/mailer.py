from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import get_template


class Mailer(object):
    def __init__(self, from_email=None):
        self.connection = mail.get_connection()
        self.from_email = from_email

    def send_messages(self, subject, template, context, to_emails):
        messages = self.generate_messages(subject, template, context, to_emails)
        self.send_mail(messages)

    def send_mail(self, messages):
        self.connection.open()
        self.connection.send_messages(messages)
        self.connection.close()

    def generate_messages(self, subject, template, context, to_emails):
        messages = []
        message_template = get_template(template)
        for recipient in to_emails:
            message_content = message_template.render(context)
            message = EmailMessage(subject, message_content, to=[recipient], from_email=self.from_email)
            message.content_subtype = 'html'
            messages.append(message)

        return messages
