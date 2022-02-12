#!/bin/bash

sudo apt-get install curl

PUBLIC_IP=`curl -Ls ipinfo.io/ip`

PRIVATE_IP=`hostname -I`

# Read the split words into an array
# based on space delimiter
read -ra IPS <<< "$PRIVATE_IP"


echo -e  "\n\n" "To establish SSH tunelling execute below command on client machine:"

echo -e "\n"   "  Public IPs:"

echo -e "\n"     "    ssh -L 5901:127.0.0.1:5901 -N -f -l $USER $PUBLIC_IP" 

echo -e "\n"    "  Private IPs:"


# Print each value of the array by using
# the loop
for IP in "${IPS[@]}";
do
    echo -e "\n"     "    ssh -L 5901:127.0.0.1:5901 -N -f -l $USER $IP"
done

echo -e  "\n" "After tunnel creation use vnc viewer to connect to 127.0.0.1:5901" "\n" 

