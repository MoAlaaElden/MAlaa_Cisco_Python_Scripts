#########################################################################################################
##      Author = Mohamed Alaa                                                                          ##
##      Purpose = Simple Telnet session to 10 Cisco routers and config VTY, User and FTP               ##
##      Uses = telnetlib, getpass, datetime                                                            ##
##      Created on 12-10-2017                                                                          ##
##      Version 1.0                                                                                    ##
#########################################################################################################

#!/usr/bin/env python

import getpass
import sys
import telnetlib
from datetime import datetime

user = raw_input("Enter your username: ")
password = getpass.getpass()


start_time = datetime.now()
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "Program started at:", start_time
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

f = open ('Routers-IP-List.txt')

for line in f:
    start_config_time = datetime.now()
    print "Start Configuring Router: ", line, " at ", start_config_time
    HOST = line
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")
    tn.write("username malaa privilege 15 password 0 cisco123\n")
    tn.write("ip ftp username malaa\n")
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
    end_config_time = datetime.now()
    total_config_time = end_config_time - start_config_time
    print "Successfully configured Router : ", HOST,  " Total time taken: ", (total_config_time)
    

end_time = datetime.now()
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "Program finished at:", end_time


## Save total time in variable total_time

total_time = end_time - start_time

## Print the total time

print 
print "Program total time taken:", total_time
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
