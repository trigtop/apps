# Script to generate the xml files for app

import os
import sys

def main():
  # app list
  dirs = (os.listdir('.'))
  # final apps text
  appMap_xml = u"["
  # loop thru and add each apps addon.xml file
  for app_dir in dirs:
    try:
      if(not os.path.isdir(app_dir)):
        continue
      if(app_dir.startswith('.')):
        # skip hidden dirs
        continue
      files = (os.listdir(app_dir))
      for file in files:
          if(not file.startswith(app_dir + '-')):
              continue
          app_name = file[0:file.rfind("-")]
          app_version = file[file.rfind("-")+1:file.rfind(".apk")]
          app_xml = ""
          app_xml += "{\"aPP_ID\":com.trigtop." + app_name + ","
          app_xml += "\"aPP_NAME\":" + app_name + ","
          app_xml += "\"iMAGE_PATH\":\"https://raw.githubusercontent.com/trigtop/apps/master/" + app_name + "/" + app_name + ".png\"" + ","
          app_xml += "\"uRL_PATH\":\"https://raw.githubusercontent.com/trigtop/apps/master/" + app_name + "/" + file + "\","
          app_xml += "\"vER\":" + app_version
          appMap_xml += app_xml.rstrip() + u"},\n"
    except Exception, e:
      # missing or poorly formatted app.xml
      print "Failed to add xml"
      sys.exit(1)
  # clean and add closing tag
  appMap_xml = appMap_xml.strip() + u"]\n"
  # save file
  try:
    # write data to the file
    open( "appMap.xml", "w" ).write( appMap_xml.encode( "UTF-8" ) )
    print "appMap.xml generated!!!"
    sys.exit(0)
  except Exception, e:
    # oops
    print "An error occurred saving %s file!\n%s" % ( "appMap.xml", e, )
    sys.exit(1)


if __name__ == '__main__':
  main()
