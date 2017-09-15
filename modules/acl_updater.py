#!/usr/bin/python3

import sys
import os

def add_ip(acl_file, ip):
    print("Adding IP!")
    with open(acl_file, "r+") as f:
        f.seek(0,2)
        f.write("\n" + ip)
    return "DONE!"

def del_ip(acl_file, ip):
    print("Deleting IP!")
    with open(acl_file,"r+") as f:
        for line in f.readlines():
            if ip not in line:
                f.write(line)
    return "DONE!"

def read_acl(acl_file):
    with open(acl_file,"r") as f:
        for line in f.readlines():
            print("Line: ",line)
    return "DONE!"

while True:
    print("\n\n-------------------------------")
#    print("1. Add IP")
#    print("2. Del IP")
    print("1. Modify ACL")
    print("2. Read ACL")
    print("3. Show ACLs")
    print("4. Exit")
    opt = input("\n>_ ")
    if opt == "1":
        print("1. Add IP")
        print("2. Del IP")
        oper = input("\n>_ ")
        if oper == "1":
            acl = input("File Name: ")
            ip = input("IP Address: ")
            if os.path.isfile(acl):
                add_ip(f,acl)
                print("DONE!")
        elif oper == "2":
            acl = input("\nFile Name: ")
            ip = input("\nIP Address: ")
            if os.path.isfile(acl):
                del_ip(acl,ip)
                print("DONE!")
        else:
            print("Wrong Option!...")
    elif opt == "2":
        acl = input("\nFile Name: ")
        ip = input("\nIP Address: ")
        if os.path.isfile(acl):
            del_ip(acl,ip)
            print("DONE!")
        else:
            print("ACL does not exist...")
    elif opt == "3":
        acl = input("\nFile Name: ")
        if os.path.isfile(acl):
            read_acl(acl)
            print("DONE!")
        else:
            print("ACL does not exist...")
    elif opt == "4":
        print("Bye!")
        sys.exit(0)
    else:
        print("Wrong option! (@#$&!)")

