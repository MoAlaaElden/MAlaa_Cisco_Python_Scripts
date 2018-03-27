#########################################################################################################	
##      Author = Mohamed Alaa                                                                          ##	
##      Purpose = Simple Telnet session to a Cisco router and executes any command.                    ##
##      Uses = telnetlib, datetime                                                                     ##
##      Created on 2-10-2017                                                                           ##
##      Version 1.0                                                                                    ##
#########################################################################################################

import telnetlib
from datetime import datetime


IP = raw_input("Enter Device IP Add: ")
USERNAME = raw_input("Enter your Username: ")
PASSWORD = raw_input("Enter your Password: ")
#ENABLEPASS = raw_input("Enter your enable password: ")
COMMAND = raw_input("Enter your enable password: ")

tn = telnetlib.Telnet(IP)

tn.read_until(b"Username: ")
tn.write(USERNAME.encode('ascii') + b"\n")
if PASSWORD:
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\n")

start_time = datetime.now()
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "Program started at:", start_time
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
	
tn.write(COMMAND.encode('ascii') + b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

end_time = datetime.now()
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "Program finished at:", end_time


## Save total time in variable total_time

total_time = end_time - start_time

## Print the total time

print 
print "Program took almost:", total_time
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
