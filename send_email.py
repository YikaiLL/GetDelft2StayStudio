import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Codes from the following website.
# http://naelshiab.com/tutorial-send-email-python/
def send_email(house_dict,time_string):
    # From one gmail address
    fromaddr = ""
    # To your email address
    toaddr = ""
    msg = MIMEMultipart()	
    msg['From'] = fromaddr
    msg['To'] = toaddr
    # Email subject
    msg['Subject'] = "Delft2Stay Update"

    body=time_string
    for key in house_dict:
        for house_property in house_dict[key]:
            body +='\n'+house_property + ":\t" + house_dict[key][house_property]
        body += '\n--------------------\n'
    # body = "YOUR MESSAGE HERE"

    msg.attach(MIMEText(body, 'plain'))

    # Change to other server if you want, but the port number should also be changed.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Login in with you passport here
    email_pass_port=""

    server.login(fromaddr, email_pass_port)

    # msg = "YOUR MESSAGE!"
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return

