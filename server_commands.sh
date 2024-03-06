#!/usr/bin/bash
if [ $1 == "0" ];
then
    #hard Restart server
    ssh root@192.168.86.22 'shutdown -r now'
elif [ $1 == "1" ];
then
    #Graceful Stop to server
    ssh root@192.168.86.22 'screen -S minecraft -p 0 -X stuff "say Server will be shutting down^M"'
    ssh root@192.168.86.22 'screen -S minecraft -p 0 -X stuff "stop^M"'
else
    #Check Server Status
    if (ssh root@192.168.86.22 'ps -e -o command | grep -q "^[j]ava -server"');
    then 
        echo "Server is running"
    else
        echo "Server is not running"
    fi
fi
