from twilio.rest import Client
import smtplib


twilio_api_key = ""
twilio_account_sid = ""
twilio_auth_token = ""
verify_sid = ""
twilio_phone_number = "+"
my_email = ""
my_password = ""


class NotificationManager:
    def __init__(self):
        self.client = Client(twilio_account_sid, twilio_auth_token)

    def send_msg(self, message):
        print("Sending Message...")
        message = self.client.messages.create(
            from_=twilio_phone_number,
            body=message,
            to="phone_number"
        )

    def send_emails(self, emails, message):
        try:
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=my_email, password=my_password)

        except smtplib.SMTPAuthenticationError:
            print("Authentication error")

        except smtplib.SMTPException as e:
            print("An exception occured", e)

        else:
            for email in emails:
                from_addr = my_email
                to_addrs = email
                subject = "New Low Price Flight"
                email_body = f"{subject}\n\n{message}".encode("utf-8")
                connection.sendmail(from_addr, to_addrs, email_body)

        finally:
            connection.quit()
