#!/bin/bash

# --------------------------------------------------------
# this script is used to check the gridftp status of SE
# by uploading a localfile.txt to the server to be checked
# and then downloading the file to local as serverfile.txt.
# Then, md5sum is used to check whether there is any diff
# between localfile.txt and serverfile.txt
#----------------------------------------------------------

BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NONE='\033[00m'
BOLD='\033[1m'
UNDERLINE='\033[4m'

# copy grid-certificate to /tmp
cp /home/nih/gridtmp/x509up_u$UID /tmp

# directory that contains localfile.txt  
localdir="/home/nih/VanderbiltTier2/checkHostGridFTPStatus"

# print time when script starts 
echo ''
startTime=`date +%c`
echo -e ${BLUE}"${startTime}"${NONE}

# read host server from hostlist.txt 
while read -r line
do
       echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

       # delete previously generated hash.md5 and serverfile.txt
       FILE1=$localdir/hash.md5
       FILE2=$localdir/serverfile.txt

       if [ -f $FILE1 ]
       then 
              rm $FILE1
       fi
      
       if [ -f $FILE2 ]
       then
              rm $FILE2
       fi

       echo -e "check host:${BLUE}${BOLD}${UNDERLINE} $line ${NONE}" 
      
       # check server with upload and download
       sleep 3s
       curTime=`date +%Y%m%d%H%M%S`      
       FileInServer="fileinserver_${curTime}.txt"
       UPLOAD='globus-url-copy file://$localdir/localfile.txt gsiftp://$line/${FileInServer}'
       DOWNLOAD='globus-url-copy gsiftp://$line/${FileInServer} file://$localdir/serverfile.txt'

       eval $UPLOAD
       sleep 3s
       eval $DOWNLOAD 
       sleep 3s

       if [ ! -f $FILE2 ]
       then 
              echo -e ${RED}${BOLD}"error met for upload and download"${NONE}
              continue
       else 
              echo -e ${GREEN}${BOLD}"upload and download works fine"${NONE}
       fi
     
       # using md5sum to check content of file
       md5sum localfile.txt serverfile.txt > hash.md5

       declare -a hashvalue 
       counter=0
       while read -r content
       do
              hashvalue[$counter]=${content% *}
              echo ${hashvalue[$counter]}
              counter=$((counter+1))
              echo $counter
       done < "hash.md5"

       if [ ${hashvalue[0]} == ${hashvalue[1]} ]
       then
             echo -e ${GREEN}${BOLD}"md5sum match! host in good shape!"${NONE}
       else 
             echo -e ${RED}${BOLD}"md5sum do not match! need to check this host!"${NONE}
       fi
       

done < "hostlist.txt"

# delete all files in serverDir, when number of files > 10
serverDir="/lio/lfs/cms/se-test"
fileNum=$(find ${serverDir} -maxdepth 1 -type f|wc -l)
if (( ${fileNum} > 10 ))
then
       rm ${serverDir}/fileinserver_*.txt
fi

echo ''
