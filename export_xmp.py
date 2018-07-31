#!/usr/bin/python
# This script leverages the great work from the Python Xmp Toolkit https://github.com/python-xmp-toolkit/python-xmp-toolkit 
#2018-07-20T10:54:38-0700 Fri huari4 dot gmail dot com testing http://python-xmp-toolkit.readthedocs.io/en/latest/index.html after install of exempi from debian repo
# program is able to read the metadata from files listed as arguments

import sys

from libxmp import XMPFiles

from libxmp import consts

from libxmp.utils import file_to_dict

# open up an image file but note that relative paths throw an error as in ~/file.jpg

def list_items(key,namespace):
  for elements in namespace:
    # namespace_string = str(namespace) if printed in output will display whole blob of xmp_dict. Need to pass the key from the calling function
    namespace_string = str(key)
    output = namespace_string + ": " + elements[0:][0] + " = " + elements[0:][1]
    # 2018-07-30T16:35:36-0700 Mon kept getting UnicodeEncodeError so let's ignore it and still get output
    print(output.encode('ascii','ignore'))

def list_dict(dict): 
  for key,value in dict.items():
    print
    print("Namespace:" + key.encode('ascii','ignore'))
    print
    list_items(key,value)


# main program
myFiles = sys.argv[1:]

# 2018-07-31T14:30:54-0700 Tue could use a file extension check for files with actual xmp embedded
# file_extensions = ['.jpg','.gif','.png','.pdf','.psd','.eps','.tif']
for eachFile in myFiles:
  xmpfile = XMPFiles( file_path=eachFile, open_forupdate=True )

  xmp = xmpfile.get_xmp()

  xmp_dict = file_to_dict( eachFile )

  print
  print("= Filename: " + eachFile + " =")
  list_dict(xmp_dict)
