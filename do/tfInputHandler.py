import hcl2
import json
import sys
import os
import subprocess as sp

# total arguments
# total arguments
"""
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)
"""

def create():
    with open('do.tfvars', 'r') as file:
        dict = hcl2.load(file)
        #print(dict)
        """
        print("admin_password")
        print(sys.argv[1])
        print("******************")
        print("db_password")
        print(sys.argv[2])
        print("******************")
        print("oo_password")
        print(sys.argv[3])
        print("******************")
        print("do_token")
        print(sys.argv[4])
        print("******************")
        print("do_storageaccessid")
        print(sys.argv[5])
        print("******************")
        print("do_storagesecretkey")
        print(sys.argv[6])
        print("******************")
        print("do_region")
        print(sys.argv[7])
        print("******************")
        print("do_image")
        print(sys.argv[8])
        print("******************")
        print("do_size")
        print(sys.argv[9])
        print("******************")
        print("nc_prefix")
        print(sys.argv[10])
        print("******************")
        print("enable_duckdns")
        print(sys.argv[11])
        print("******************")
        print("duckdns_domain")
        print(sys.argv[12])
        print("******************")
        print("duckdns_token")
        print(sys.argv[13])
        print("******************")
        print("letsencrypt_email")
        print(sys.argv[14])
        print("******************")
        """
        
        dict["admin_password"]=sys.argv[1]
        dict["db_password"]=sys.argv[2]
        dict["oo_password"]=sys.argv[3]
        dict["do_token"]=sys.argv[4]
        dict["do_storageaccessid"]=sys.argv[5]
        dict["do_storagesecretkey"]=sys.argv[6]
        dict["do_region"]=sys.argv[7]
        dict["do_image"]=sys.argv[8]
        dict["do_size"]=sys.argv[9]
        dict["nc_prefix"]=sys.argv[10]
        dict["enable_duckdns"]=sys.argv[11]
        dict["duckdns_domain"]=sys.argv[12]
        dict["duckdns_token"]=sys.argv[13]
        dict["letsencrypt_email"]=sys.argv[14]

        output = sp.getoutput('cat ~/.ssh/id_rsa.pub')
        print (output)
        dict["ssh_key"] = output
        print(dict["ssh_key"])
        
        jsonFile = open("json_variables.tfvars.json", "w+")
        jsonFile.write(json.dumps(dict))
        jsonFile.close()  

def main():
    n = len(sys.argv)
    print("Total arguments passed:", n)
    if n!=15:
        print("Please enter all the parameters")
    else:
        create()
if __name__ == "__main__":
    main()
