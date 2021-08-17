# Python program for sending email
# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "shivam.bhardwaj9@gmail.com"
# Receivers email
rec_email = "shivam.bhardwaj9@gmail.com"

message = "Best Model is being created... Thank You"
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("shivam.bhardwaj9@gmail.com", "******")
print("Login Success!")
# Send Email
server.sendmail("Shivam Bhardwaj", "shivam.bhardwaj9@gmail.com", message)
print(f"Email has been sent successfully to {rec_email}")
