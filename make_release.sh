#! /bin/bash

CUR_DIR=`pwd`
python xk_appsTxt_generator.py 
if [ $? -ne 0 ]
then
        echo -e "\033[31m  fail to generate app_xml!!! \033[0m"
        exit
else
        echo -e "\033[32m repoMap generate successfully \033[0m"
		mv appMap.xml apps.txt
fi
git add -A
git commit -m 'release 1.0.0'
git push -f origin master:master

