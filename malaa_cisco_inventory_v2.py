#########################################################################################################
##      Author = Mohamed Alaa                                                                          ##
##      Purpose = Cisco inventory for list of devices.                                                 ##
##      Uses = telnetlib, getpass, re, datetime                                                        ##
##      Created on 19-10-2017                                                                          ##
##      Version 2.0                                                                                    ##
#########################################################################################################


#!/usr/bin/python

'''Simple script to telnet into a number of devices and check inventory'''

import telnetlib
import getpass
import re
from datetime import datetime

#Check for devices.txt and read into string
devices=[]
try:
    with open('devices.txt') as file:
        pass
except IOError as e:
    print("\ndevices.txt does not exist or unreadable, exiting now")
    exit()

f = open('devices.txt')
for line in f:
    devices.append(line.rstrip())
    
#Check if report.txt exists. If so, ask if we want to overwrite it    
try:
    with open('report.txt') as file:
        choice = raw_input("\nreport.txt already exists. Do you want to overwrite it? [y/n]: ")
        while choice not in ["y","n"]:
            choice = input("Invalid choice! Do you want to overwrite report.txt? [y/n]: ")
        if choice == "n":
            print("\nExiting now")
            exit()
        else:
            print("\nreport.txt will be overwritten!")
            f = open('report.txt', 'w')
            f.close()
except IOError as e:
    pass


#Get username and password
user = raw_input("\n\nEnter your username: ")
password = getpass.getpass(prompt="Enter your password: ")
#enablepass = getpass.getpass(prompt="Enter your enable password: ")

start_time = datetime.now()

#Log into host, run commands, echo output, write output to file
for device in devices:
    try:
        tn = telnetlib.Telnet(device,23,5)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"\n")
        en = (tn.read_some().decode('ascii'))
        if ">" in en:
            tn.write(b"enable\n")
            tn.write(enablepass.encode('ascii') + b"\n")
        print 
        print 
        print
        print "Checking ",device
        tn.write(b"terminal length 0\n")  
        tn.write(b"show run | include hostn\n")
        tn.write(b"show ver | include IOS\n")
        tn.write(b"show inventory\n")
        tn.write(b"exit\n")
        output = re.split(r'[,\n]*', (tn.read_all().decode('ascii')))   # Split string into list. Separate on both commas and newlines
        f = open('report.txt','a')
        print 
        print "Device IP: ",device
        f.write("\nDevice IP: "+device+"\n")
        for i in output:                                                # Iterate through output and print and write required information
            if "hostname" in i:
                print(i.lstrip())
                f.write(i.lstrip()+"\n")
            elif "ersion" in i:
                print(i.lstrip())
                f.write(i.lstrip()+"\n")
            elif "PID:" in i:
                print(i.lstrip())
                f.write(i.lstrip()+"\n")
            elif "SN:" in i:
                print(i.lstrip())
                f.write(i.lstrip()+"\n")
        f.close()
    except:
        print("\n\nUnable to log into or resolve",device)

end_time = datetime.now()

print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
total_time = end_time - start_time
print 
print "Program took almost:", total_time
print 
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
