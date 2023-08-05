# being with python shebang
#!usr/bin/env python

#  import the subprocess module
import subprocess

#  variable that will replace instance of interface with value eth0
#  will ask for user input as to which interface we are changing
#  use raw_input if needing to run in python 2.7
interface = input("interface >")
#  variable (container) will replace MAC address with new_mac string
#  will ask for user input as to new MAC Address
#  use raw_input for python 2.7
new_mac = input("new MAC >")
#  print statement with string (anything inside quotes is a string literal) that will test our variable
#  plus symbol is to indicate it was successful
print("[+] Changing MAC address for " + interface + " to " + new_mac)

#  subprocess module
#  subprocess script inside of parenthesis
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)