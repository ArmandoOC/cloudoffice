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

    enableDuckDnsDomainToPyboxDroplet=sys.argv[1]
    duckdnsPyboxDomain = sys.argv[2]
    duckdns_token = sys.argv[3]

    commandCero = 'echo url="https://www.duckdns.org/update?domains='+duckdnsPyboxDomain+'&token='+duckdns_token+'&ip=" | curl -k -o ~/duckdns/duck.log -K -'
    if enableDuckDnsDomainToPyboxDroplet==1:
        file = open("assignDuckdnDomainToPyboxDroplet.sh", "w")        
        file.write(commandCero)
        file.close()

        commandOne = 'chmod 700 assignDuckdnDomainToPyboxDroplet.sh'
        output = sp.getoutput(commandOne)
        print(output)

        commandTwo = 'bash assignDuckdnDomainToPyboxDroplet.sh'
        output = sp.getoutput(commandTwo)
        print(output)

        print("****************************************************************************")
        print("****************************************************************************")
        print("****************************************************************************")
        print("Please wait 1 minute aprox and then enter to your pybox domain in your browser.")
        print("****************************************************************************")
        print("****************************************************************************")
        print("****************************************************************************")

def main():
    n = len(sys.argv)
    print("Total arguments passed:", n)
    if n!=4:
        print("Please enter all the parameters")
    else:
        print("****************************************************************************")
        print("****************************************************************************")
        print("****************************************************************************")
        print("Hello.. please wait")
        print("****************************************************************************")
        print("****************************************************************************")
        print("****************************************************************************")
        create()
if __name__ == "__main__":
    main()
