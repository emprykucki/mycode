#!/usr/bin/env python3

#Check hostname against expected value

#collect input from user
hostname = input("What value should we set for hostname?")
 
#use lower method to test if input value matches expected
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("The hostname matches expected config")

print("Exiting the script")    
