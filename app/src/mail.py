from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import os

if __name__ == "__main__":
    pass


def read_recipients_list():
    recipients = []
    with open("./email_list.txt") as file:
        lines = file.readlines()
        for line in lines:
            recipients.append(line.strip("\n"))
        file.close()
    return recipients


def send_email(gpu_name: str, url: str, price: float):
    recipients = read_recipients_list()
    message = MIMEMultipart("alternative")
    message["Subject"] = "GPU-bot v1.2"
    message["From"] = os.environ.get("GMAIL")
    message["To"] = ", ".join(recipients)

    text = """\
    GPU Available!
    {}
    For {}
    {}
    """.format(gpu_name, str(price), url)
    html = """\
    <html>
        <body>
        <h2>{}</h2>
        <h3></h3>
        <h3>For {}</h3>
        <h3><a href="{}">{}</a></h3>
        </body>
    </html>""".format(gpu_name, str(price), url, url)

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    port = 465
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(message["From"], password=os.environ.get("PASSWORD"))
        server.sendmail(message["From"], recipients, message.as_string())
        print("Mail send")
        server.quit()
