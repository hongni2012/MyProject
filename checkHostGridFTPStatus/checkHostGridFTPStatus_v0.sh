#!/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NONE='\033[00m'
BOLD='\033[1m'
UNDERLINE='\033[4m'

cp /home/nih/gridtmp/x509up_u$UID /tmp

localdir="/home/nih/VanderbiltTier2/checkHostGridFTPStatus"
targetdir="/home/nih/web/checkSEGridFTP"

#echo "Time : "`date +%Y%m%d%H%M%S` >> $targetdir/test.txt
startTime=`date +%Y%m%d%H%M%S`
echo -e ${BLUE}"Time ${startTime}"${NONE}

while read -r line
do
       echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
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

       #echo "check host: $line" >> $targetdir/test.txt
       echo -e "check host:${BLUE}${BOLD}${UNDERLINE} $line ${NONE}" 

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

       md5sum localfile.txt serverfile.txt > hash.md5

       declare -a hashvalue 
       counter=0
       while read -r content
       do
              hashvalue[$counter]=${content% *}
              #echo ${hashvalue[$counter]} >> $targetdir/test.txt
              echo ${hashvalue[$counter]}
              counter=$((counter+1))
              #echo $counter >> $targetdir/test.txt
              echo $counter
       done < "hash.md5"

       if [ ${hashvalue[0]} == ${hashvalue[1]} ]
       then
             #echo "match!" >> $targetdir/test.txt
             echo -e ${GREEN}${BOLD}"md5sum match! host in good shape!"${NONE}
       else 
             #echo "do not match!" >> $targetdir/test.txt
             echo -e ${RED}${BOLD}"md5sum do not match! need to check this host!"${NONE}
       fi
       

done < "hostlist.txt"

# delete all files, when number of files exceed 10
serverDir="/lio/lfs/cms/se-test"
fileNum=$(find ${serverDir} -maxdepth 1 -type f|wc -l)
if (( ${fileNum} > 10 ))
then
       rm ${serverDir}/fileinserver_*.txt
fi
