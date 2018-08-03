#!/usr/bin/python

#2018-07-20T10:54:38-0700 Fri huari4 at gmail dot com testing http://python-xmp-toolkit.readthedocs.io/en/latest/index.html after install of exempi from debian repo
# program is able to read the metadata from files listed as arguments

import sys

# file handler
from libxmp import XMPFiles
# known namespaces registered in python xmp toolkit
from libxmp import consts
# for custom xmp namespaces add them to a dictionary
from libxmp.utils import file_to_dict

# open up an image file but note that relative paths throw an error as in ~/file.jpg


# this function will list the xmp fields and their values
def list_items(key,namespace):
  for elements in namespace:
# namespace_string = str(namespace) if printed in output will display whole blob of xmp_dict. Need to pass the key from the calling function
    namespace_string = str(key)
    output = namespace_string + ": " + elements[0:][0] + " = " + elements[0:][1]
# 2018-07-30T16:35:36-0700 Mon kept getting UnicodeEncodeError so let's ignore it and still get output
    print(output.encode('ascii','ignore'))

# This function will list the namespace and call the list_items function to get the fields and values
def list_dict(dict): 
  for key,value in dict.items():
    print
    print("Namespace:" + key.encode('ascii','ignore'))
    print
    list_items(key,value)


# main program
myFiles = sys.argv[1:]

# 2018-07-31T14:30:54-0700 Tue could use a file extension check for files with actual xmp embedded
#file_extensions = ['.jpg','.gif','.png','.pdf','.psd','.eps','.tif']
#file_extensions = ['.JPG','.gif','.png','.pdf','.psd','.eps','.ai','.jpeg']
# add new fileypes as needed
file_extensions = ['.jpg','.JPG','.gif','.png','.pdf','.psd','.eps','.tif','.ai','.jpeg']


for eachFile in myFiles:
  xmpfile = XMPFiles( file_path=eachFile, open_forupdate=True )

  xmp = xmpfile.get_xmp()

  xmp_dict = file_to_dict( eachFile )

  print
  print("= Filename: " + eachFile + " =")

# let's test for the file extension. If valid then display the xmp, else print "not a valid file type"
# 2018-07-31T17:58:08-0700 Tue this only works if the extension is 4 chars long. What about .jpeg? 
# this works only if assets are in the same directory as script else ../ and ./ will match the index -
# input_file_extension  =  eachFile[eachFile.index('.'):] 
# old way:  input_file_extension  =  eachFile[-4:]


  pos = eachFile.rfind('.',0,-1 )
  input_file_extension  =  eachFile[pos:]
# input_file_extension = eachFile.endswith(file_extensions) and eachFile.rfind('.',0,-1)
  if input_file_extension in file_extensions:
    list_dict(xmp_dict)
  else:
    print("not a valid file type")
