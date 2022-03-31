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
    print("****stringToExtract")
    print(stringToExtract)
    #cloudoffice-setup-7gg4d.sh root@159.203.126.42:~/cloudoffice-setup-7gg4d
    print(indexSh)
    playbookname = stringToExtract[0:indexSh] +".sh"
    playbookname = playbookname.strip()
    print("playbookname")
    print(playbookname)
    print("ENDplaybookname")
    #print(stringToExtract)

    print("****444444stringToExtract")
    print(stringToExtract)
    
    indexArroba = stringToExtract.index('@')
    remoteHost = stringToExtract[indexArroba:]
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
    print("commandOne")
    commandOne = 'echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config'
    print(commandOne)
    #commandOne = "scp "+playbookname+" "+ remoteHost
    commandTwo = "scp "+playbookname+" "+ remote+":~/"
    print(commandTwo)
    print(remote)
    commandThree = 'ssh '+remote+' '+'"chmod +x '+playbookname+' && ~/'+playbookname+'"'
    print(commandThree)
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
    file.write("\n")
    file.write(commandThree)
    file.close()

def main():
    create()
if __name__ == "__main__":
    main()
