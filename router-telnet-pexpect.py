#########################################################################################################	
##      Author = Mohamed Alaa                                                                          ##	
##      Purpose = Telnet and Configure Cisco Router with pexpect                                       ##
##      Uses = netmiko, ConnectHandler, datetime                                                       ##
##      Created on 28-9-2017                                                                           ##
##      Version 1.0                                                                                    ##
#########################################################################################################

import pexpect

# request your inputs

IP = raw_input("Enter Device IP Add: ")
user = raw_input("Enter your telnet Username: ")
password = raw_input("Enter your telnet Password: ")
enablepass = raw_input("Enter your enable password: ")
enable = ("ena")
command = ("sh ip int bri")

telnet = 'telnet ' + IP

#Login to the switch
t=pexpect.spawn(telnet)
t.expect('Username:')
t.sendline(user)
t.expect('Password:')
t.sendline(password)
t.expect('>')
t.sendline(enable)
t.expect('Password:')
t.sendline(enablepass)
t.expect('#')

#Send the command
t.sendline('command')
t.expect('#')
data = t.before

#Closing the Telnet Connection
t.sendline('exit')
t.expect('>')
t.sendline('exit')
t.expect(pexpect.EOF)

#Opening the file and writing the data to it
f = open('routeroutput', 'w')
f.write(data)
f.close()
