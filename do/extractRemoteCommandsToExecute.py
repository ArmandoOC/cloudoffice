import json
import re

from click import command

def create():
    # Opening JSON file
    f = open('output.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    extract = data["cloudblock-output"]["value"]
    #print(extract)

    left = "scp"
    right = ".sh\nssh"

    stringToExtract= extract[extract.index(left)+len(left):extract.index(right)]
    indexSh = stringToExtract.index('.sh')
    #print(indexSh)
    playbookname = stringToExtract[0:indexSh] +".sh"
    playbookname = playbookname.strip()
    print(playbookname)

    #print(stringToExtract)
    
    indexArroba = stringToExtract.index('@')
    remoteHost = stringToExtract[indexArroba:-1]
    #print(remoteHost)
    remoteHost = "root"+remoteHost+".sh"
    
    #print(remoteHost)
    #print(remoteHost)
    indexVirguilla = remoteHost.index('~')
    remote = remoteHost[:indexVirguilla-1]
    #print(remote)
    commandOne = "scp "+playbookname+" "+ remoteHost
    print(commandOne)
    commandTwo = 'ssh '+remote
    print(commandTwo)
    commandThree = '"chmod +x '+playbookname+' && ~/'+playbookname+'"'
    print(commandThree)
    #scp cloudoffice-setup-iitgq.sh ubuntu@161.35.134.158:~/cloudoffice-setup-iitgq.sh
    #ssh ubuntu@161.35.134.158 "chmod +x cloudoffice-setup-iitgq.sh && ~/cloudoffice-setup-iitgq.sh"

    # Closing file
    f.close() 

    file = open("executeOnremote.sh", "w")
    file.write(commandOne)
    file.write("\n")
    file.write(commandTwo)
    file.write("\n")
    file.write(commandThree)
    file.close()

def main():
    create()
if __name__ == "__main__":
    main()
