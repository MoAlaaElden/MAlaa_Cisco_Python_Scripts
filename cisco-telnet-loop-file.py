#########################################################################################################	
##      Author = Mohamed Alaa                                                                          ##	
##      Purpose = Simple Telnet session to 10 Cisco routers and config VTY, User and FTP               ##
##      Uses = telnetlib, datetime, getpass, sys                                                       ##
##      Created on 12-10-2017                                                                          ##
##      Version 1.0                                                                                    ##
#########################################################################################################

#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your username: ")
password = getpass.getpass()

f = open ('Routers-IP-List.txt')

for line in f:
    print "Configuring Router " + (line)
    HOST = line
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")
    tn.write("username malaa privilege 15 password 0 cisco123\n")
    tn.write("ip ftp password password123\n")
    tn.write("line vty 0 5\n")
    tn.write("no password\n")
    tn.write("login local\n")
    tn.write("length 0\n")
    tn.write("transport input all\n")
    tn.write("end\n")
    tn.write("wr\n")
    tn.write("sh run | se vty\n")
    tn.write("sh run | i user\n")
    tn.write("sh run | i ftp\n")
    tn.write("exit\n")

    print tn.read_all()
