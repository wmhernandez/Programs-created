#!/usr/bin/env python

# home ip address checker.  Regular, 1/wk checker, for outside accessing.

# send an info request to the my address website.
# How do I access the google info, directly?

import socket
import sys
import email
import smtplib
import urllib.request, urllib.parse, urllib.error  #  this from 12.5 Bsoup section
# from bs4 import BeautifulSoup
import ssl
import datetime
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#---------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------


# *****  basic email send *******

msg = email.message_from_string(theip.decode())
# print(type(theip.decode()))

msg['From'] = " XXXXXXXXXX"
msg['To'] = "XXXXXXXXXXXX"
msg['Subject'] = "IP program test successful"

s = smtplib.SMTP("smtp.live.com",587) #email server connection.  This is set for hotmail.com
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('XXXXXXXX', 'XXXXXXXX')

s.sendmail("XXXXXXXXXXXXXX", "XXXXXXXXXXXXX", msg.as_string())

s.quit()

 #---------------------------------------------------------------------------------------
