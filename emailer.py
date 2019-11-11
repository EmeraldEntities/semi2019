import email, smtplib, ssl
import csv

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #login
    server.login('rhhsstuco.contact@gmail.com', open('email-password.txt', 'r').read())
    
    #read csv
    with open("attendees.csv",'r') as file:
        reader = csv.reader(file)
        for first, last, email in reader:
            filename = '%s_%s.png' %(first,last)
            
            #create message
            msg = MIMEMultipart()
            msg['Subject'] = "Hey %s, Your Semi Ticket Has Arrived!"%first
            msg['From'] = "RHHS StuCo <rhhsstuco.contact@gmail.com>"
            msg['To'] = email
            message = """<p>Greetings from StuCo!&nbsp;</p>
<p>You can pick up your semi ticket today (Monday) in the Front Foyer.</p>
<p>Attached is a digital copy of your ticket in case you forget or lose your physical ticket so save it to your phone! There is no need to print it.</p>
<p><strong>Important Info For Semi</strong></p>
<ul>
<li>This Thursday (November 14th, 2019)</li>
<li>6:30 pm - 10:30 pm</li>
<li>Bellagio Boutique Event Centre (8540 Jane St, Concord, ON L4K 5A9)</li>
<li>Bring ticket and student id</li>
</ul>
<p>See you soon!&nbsp;</p>
<p>StuCo 2019-2020&nbsp;</p>
<p>--</p>
<p style="line-height: 1;"><strong>RHHS Student Council</strong></p>
<p style="line-height: 1;">IG/Twitter: @rhhs_stuco</p>
<p style="line-height: 1;">Website: rhhsstuco.ca</p>
<p style="line-height: 1;"><em>Sapere Aude</em></p>"""
            msg.attach(MIMEText(message, 'html'))

            #attach ticket
            with open('tickets/'+filename, 'rb') as a_file:
                part = MIMEApplication(a_file.read(), Name=filename)
            part['Content-Disposition'] = 'attachment; filename="%s"' % filename
            msg.attach(part)

            #send email
            server.sendmail(msg['From'], email, msg.as_string())
            print(f"Sending email to {first}")

#close server
server.close()
print('all done!')