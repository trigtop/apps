# coding=UTF-8
# Script to generate the xml files for app

import os
import sys
import md5

def main():
  reload(sys)
  sys.setdefaultencoding('utf8')
  topdir = os.getcwd()

  # app list
  os.chdir(topdir)
  dirs = (os.listdir('.'))
  # final apps text
  appMap_xml = u"["
  # loop thru and add each apps addon.xml file
  for app_dir in dirs:
    try:
      os.chdir(topdir)
      if(not os.path.isdir(app_dir)):
        continue
      if(app_dir.startswith('.')):
        # skip hidden dirs
        continue
      os.chdir(topdir + "/" + app_dir)
      files = (os.listdir('.'))
      filesTmp = []
      for fileTmp in files:
          if(fileTmp.startswith("appname.txt")):
	      filesTmp.insert(0 , fileTmp)
          elif(fileTmp.endswith(".apk") or fileTmp.endswith(".mp4") or fileTmp.endswith(".MOV")):
              filesTmp.append(fileTmp)

      for file in filesTmp:
	  if(file.startswith("appname.txt")):
              f = open(file)
              aPP_NAME_extra = f.readline()
	      #print aPP_NAME_extra
              f.close()
              continue
          if(not file.startswith(app_dir + '-')):
              continue
	  #print file
          app_name = file[0:file.rfind("-")]
	  if(file.endswith(".apk")):
              app_version = file[file.rfind("-")+1:file.rfind(".apk")]
          elif(file.endswith(".mp4")):
              app_version = file[file.rfind("-")+1:file.rfind(".mp4")]
          elif(file.endswith(".MOV")):
              app_version = file[file.rfind("-")+1:file.rfind(".MOV")]
          app_md5 = md5.new(open(file).read()).hexdigest()
          #print app_md5
          app_xml = ""
          app_xml += "{\"aPP_ID\":\"com.trigtop." + app_name + "\","
          app_xml += "\"aPP_NAME\":\"" + app_name + "\","
	  app_xml += "\"aPP_NAME_extra\":\"" + aPP_NAME_extra + "\","
          app_xml += "\"iMAGE_PATH\":\"https://raw.githubusercontent.com/trigtop/apps/Ergo/" + app_name + "/" + app_name + ".png\","
          app_xml += "\"mD5\":\"" + app_md5 + "\","
          app_xml += "\"uRL_PATH\":\"https://raw.githubusercontent.com/trigtop/apps/Ergo/" + app_name + "/" + file + "\","
          app_xml += "\"vER\":\"" + app_version + "\""
          appMap_xml += app_xml.rstrip() + u"},\n"
    except Exception, e:
      # missing or poorly formatted app.xml
      print e
      print "Failed to add xml"
      sys.exit(1)
  # clean and add closing tag
  appMap_xml = appMap_xml.strip() + u"]\n"
  # save file
  try:
    # write data to the file
    os.chdir(topdir)
    open( "appMap.xml", "w" ).write( appMap_xml.encode( "UTF-8" ) )
    print "appMap.xml generated!!!"
    sys.exit(0)
  except Exception, e:
    # oops
    print "An error occurred saving %s file!\n%s" % ( "appMap.xml", e, )
    sys.exit(1)


if __name__ == '__main__':
  main()
