# Home ip address checker.  This app reaches out to the website, ipecho.net, and gathers the listed home ip
# It then logs in to an existing email account and uses it to send the ip data to listed emails.

import datetime
import email
import smtplib
import socket
# from bs4 import BeautifulSoup
import ssl
import sys
import urllib.error  # this from 12.5 BeautifulSoup section
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# ---------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------

thedate = datetime.date.today()
fhand = urllib.request.urlopen('http://ipecho.net')

with open("NewTextFile testing.txt", "w") as text_file:
    text_file.write("File opened ")
    text_file.write(thedate.strftime('%m/%d/%Y') + "\n" + "\n")
    for line in fhand:
        text_file.write(line.decode() + "\n")
text_file.close()
# --------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------

fhand = urllib.request.urlopen('http://ipecho.net')
for dataline in fhand:
    if b'Your IP is ' in dataline:
        wordsinline = dataline.split()
        ipfraglength = len(wordsinline[3])
        ipend = wordsinline[3].find(b'<')
        theip = wordsinline[3][:ipend]
        print('The ip today,', thedate.strftime('%m/%d/%Y'), 'is ', theip.decode())
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# basic email send set for Hotmail.com

msg = email.message_from_string(theip.decode())

msg['From'] = "XXXX@XXXX"
msg['To'] = "XXXX@XXXX"
msg['Subject'] = "IP program test successful"

s = smtplib.SMTP("smtp.live.com", 587)  # This set to hotmail.com
s.ehlo()
s.starttls()
s.ehlo()
s.login('XXXXXX@XXXXXX', 'XXXXXXX')

s.sendmail("XXXX@XXXX", "XXXXXXXX@XXXXX", msg.as_string())

s.quit()

# ----------------------------------------------------------------------------------------
