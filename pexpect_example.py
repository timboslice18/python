import pexpect
import getpass
import os
import sys
import re
import logging


def main():
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
	userName = "tsurento"
	def enterPassword():
		while True: # repeat forever
			pwd = getpass.getpass('Enter password:')
			password_again = getpass.getpass('Confirm password:')
			if pwd != password_again:
				print 'Password and confirmation do not match.Please try again!!'
			else:
				return pwd	
    password = enterPassword()
	
	child = pexpect.spawn ('ssh %s@%s' % (userName, switchName))
	#expect 1 of 3.
	#password prompt means everything worked and script is waiting for password to be sent
	#ssh: means ...
	#(yes/no) means it is waiting for an SSH known_host. In this case we send yes & then expect the password prompt. Password var is then sent
	o = child.expect(['password', 'ssh: ', '(yes/no)'])
	if o == 0:
		child.sendline (password)
	elif o == 1:
		logging.debug('%s was unable to log into %s due to a timeout.' % (userName, switchName))
		raise Exception("Cannot reach hostname '%s'" % (switchName))
	elif o == 2:
		logging.debug("%s created a new SSH key for host %s. " % (userName, switchName))
	   child.sendline ('yes')
		child.expect ('password: ')
		child.sendline (password)
	#child.sendline (password)
	#Gather output of 'sh lldp neigh' & 'sh cdp neigh' and send to <cdp|lldp>Verification()
	child.expect ('#')
	print "user has logged in"	

main()

