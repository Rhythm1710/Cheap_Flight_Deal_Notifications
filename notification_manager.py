from twilio.rest import Client
import smtplib


twilio_api_key = "808bda379c3f358d866ed5fbc998ae10"
twilio_account_sid = "AC6a916389b78ca018a9adb995df46d0b1"
twilio_auth_token = "a1b991364599966ff76d02100421a9de"
verify_sid = "VAca0ddccc627c2790286225993d571109"
twilio_phone_number = "+15734961771"
my_email = "rhythm.hacker17@gmail.com"
my_password = "xkkxieymtseyzcqu"


class NotificationManager:
    def __init__(self):
        self.client = Client(twilio_account_sid, twilio_auth_token)

    def send_msg(self, message):
        print("Sending Message...")
        message = self.client.messages.create(
            from_=twilio_phone_number,
            body=message,
            to="+919996844460"
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
