#! /bin/bash

CUR_DIR=`pwd`
python xk_appsTxt_generator.py 
if [ $? -ne 0 ]
then
        echo -e "\033[31m  fail to generate app_xml!!! \033[0m"
        exit
else
		mv appMap.xml apps.txt
        echo -e "\033[32m apps.txt generate successfully \033[0m"
fi
git add -A
#git commit -m 'release 1.1.0'
git commit --amend
git push -f origin Amlogic_S922X:Amlogic_S922X

