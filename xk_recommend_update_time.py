# coding=UTF-8
# Script to generate the xml files for app

import os
import sys
import md5
import time

def main():
  reload(sys)
  sys.setdefaultencoding('utf8')

    
  try:
    #获得当前时间时间戳 
    now = int(time.time()) 
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S" 
    timeStruct = time.localtime(now) 
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct) 
    print strTime
    open( "app_recommend_update_time.txt", "w" ).write(strTime)
    print "app_recommend_update_time.txt generated!!!"
  except Exception, e:
    # missing or poorly formatted app.xml
    print e
    print "Failed to add xml"
    sys.exit(1)

if __name__ == '__main__':
  main()
