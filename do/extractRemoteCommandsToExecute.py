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
    print("playbookname")
    print(playbookname)
    print("ENDplaybookname")
    #print(stringToExtract)
    
    indexArroba = stringToExtract.index('@')
    remoteHost = stringToExtract[indexArroba:-1]
    print("STARTremoteHost")
    print(remoteHost)
    print("ENDremoteHost")
    remoteHost = "root"+remoteHost+".sh"
    
    #print(remoteHost)
    #print(remoteHost)
    indexVirguilla = remoteHost.index('~')
    remote = remoteHost[:indexVirguilla-1]
    #print(remote)
    commandCero = "#!bin/bash"
    print(commandCero)
    commandOne = "scp "+playbookname+" "+ remoteHost
    print(commandOne)
    commandTwo = 'ssh '+remote+' '+'"chmod +x '+playbookname+' && ~/'+playbookname+'"'
    print(commandTwo)
    #scp cloudoffice-setup-iitgq.sh ubuntu@161.35.134.158:~/cloudoffice-setup-iitgq.sh
    #ssh ubuntu@161.35.134.158 "chmod +x cloudoffice-setup-iitgq.sh && ~/cloudoffice-setup-iitgq.sh"
    #ssh root@159.203.126.42 "chmod +x cloudoffice-setup-7gg4.sh" && ~/cloudoffice-setup-7gg4.sh"
    # Closing file
    f.close() 

    file = open("executeOnremote.sh", "w")
    file.write(commandCero)
    file.write("\n")
    file.write(commandOne)
    file.write("\n")
    file.write(commandTwo)
    file.close()

def main():
    create()
if __name__ == "__main__":
    main()
