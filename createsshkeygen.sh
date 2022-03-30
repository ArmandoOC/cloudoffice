#!bin/bash
rm -f ~/.ssh/id_rsa && ssh-keygen -m PEM -t rsa -b 2048 -N '' -f ~/.ssh/id_rsa