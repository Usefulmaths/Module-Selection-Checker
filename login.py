from splinter import Browser
from bs4 import BeautifulSoup
import time
import datetime

from send_email import send_email
from secret import get_UCL_username
from secret import get_UCL_password
from secret import get_gmail_username
from secret import get_gmail_password

UCL_username = get_UCL_username()
UCL_password = get_UCL_password()
gmail_username = get_gmail_username()
gmail_password = get_gmail_password()

anchor_condition = 37
sleep_time = 300

browser = Browser('chrome')

while anchor_condition <= 37:
		print "Visiting UCL Portico..."
		browser.visit('https://evision.ucl.ac.uk/urd/sits.urd/run/siw_lgn')
		print "Typing in Username:", UCL_username
		browser.find_by_name('MUA_CODE.DUMMY.MENSYS.1').fill(UCL_username)
		print "Typing in Password..."
		browser.find_by_name('PASSWORD.DUMMY.MENSYS.1').fill(UCL_password)
		print "Logging in..."
		browser.find_by_name('BP101.DUMMY_B.MENSYS.1').first.click()
		print "Navigating to Study..."
		browser.find_by_id('U_MYSTS').first.click()

		soup = BeautifulSoup(browser.html, 'html.parser')
		anchor_condition = len(soup.select('a'))

		if(anchor_condition == 37):
			now = datetime.datetime.now()
			print "%s:%s:%s: Found %s anchor tags -- Module Selection still not implemented." % (now.hour, now.minute, now.second, condition)
			print "Sleeping for %s seconds..." % (sleep_time)
			print "\n"
			time.sleep(sleep_time)
		else: break

now = datetime.datetime.now()
print "%s:%s:%s: SUCCESS!! Module Selection is now available" % (now.hour, now.minute, now.second)
print "Sending email..."
send_email("Module Selection is Available!!!", "zcaplel@ucl.ac.uk", gmail_username, gmail_password)
print "Email sent"