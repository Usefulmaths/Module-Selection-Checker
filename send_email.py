import smtplib

def send_email(content, TO, FROM, password): 
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login(FROM, password)

	msg = "\r\n".join([
	  "From: %s" % (FROM),
	  "To: %s" % TO,
	  "Subject: Module Selection Available",
	  "",
	  content
	 ])

	mail.sendmail(FROM, TO, msg)
	mail.close()