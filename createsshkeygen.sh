#!bin/bash
rm -f ~/.ssh/id_rsa && ssh-keygen -m PEM -t rsa -b 4096 -N '' -f ~/.ssh/id_rsa