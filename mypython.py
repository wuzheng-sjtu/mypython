#!/usr/bin/env python
import sys, os
import getopt

_options = [
	'help',
	'version',
	'system',
	'crawler',
]
_short_options = 'hvsc'
help_info="""mypython version 1.0
Copyright 2016 Zheng Wu (14wuzheng@sjtu.edu.cn)

Usage: mypython [options] [filename]
Generate a customed formatted python file

-h --help 	      Display this help information
-v --version      Display the version of this program
-s --system	      Generate a system-related formatted python file
-c --crawler      Generate a crawler-related formatted python file

For bug reporting, please email me <14wuzheng@sjtu.edu.cn>"""

version_info = """mypython version 1.0
Copyright 2016 Zheng Wu (14wuzheng@sjtu.edu.cn)
"""

try:
	opts, args = getopt.getopt(sys.argv[1:], _short_options, _options)
	# the root of file
except getopt.GetoptError as e:
	print (
		"""
{}.
Try 'mypython --help' for more options.""".format(e))
	exit()

if not opts and not args:
	print(help_info)
else:
	for opt, arg in opts:
		#print opt
		if opt in ['-h', '--help']:
			#Display help info
			print (help_info)
		elif opt in ['-v', '--version']:
			#Display version info
			print version_info
		elif opt in ['-s', '--system']:
			#Generate system-related formatted python file
			fileroot = args[0]
			filename = fileroot.split('/')[-1]
			filedir = fileroot[:-len(filename)]
			text = """'#! /usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "Zheng Wu"

import os, sys

reload(sys)
sys.setdefaultencoding("utf-8")
'"""
			if not os.path.exists(filedir):
				os.system('mkdir -p '+filedir)
				print 'Specified directory does not exist, creating it for you...\n'
			os.system('cd '+filedir+' ; '+'echo '+text+' | cat > '+filename+' ; cd -')
			all_bin = os.popen('ls /usr/local/bin/ | sort | uniq').read().split('\n')
			if 'subl' in all_bin:
				os.system('subl '+fileroot)
		elif opt in ['-c', '--crawler']:
			#Generate crawler-related formatted python file
			fileroot = args[0]
			filename = fileroot.split('/')[-1]
			filedir = fileroot[:-len(filename)]
			text = """'#! /usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "Zheng Wu"

import re
from bs4 import BeautifulSoup
from splinter import Browser
import urllib2
import sys, time
import webbrowser

reload(sys)
sys.setdefaultencoding("utf-8")
'"""
			if not os.path.exists(filedir):
				os.system('mkdir -p '+filedir)
				print 'Specified directory does not exist, creating it for you...\n'
			os.system('cd '+filedir+' ; '+'echo '+text+' | cat > '+filename+' ; cd -')
			all_bin = os.popen('ls /usr/local/bin/ | sort | uniq').read().split('\n')
			if 'subl' in all_bin:
				os.system('subl '+fileroot)
	if not opts :
		fileroot = args[0]
		filename = fileroot.split('/')[-1]
		filedir = fileroot[:-len(filename)]
		print filedir
		text = """'#! /usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "Zheng Wu"

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
'"""
		if not os.path.exists(filedir) and filedir:
			print filedir
			os.system('mkdir -p '+filedir)
			print 'Specified directory does not exist, creating it for you...\n'
			os.system('cd '+filedir+' ; '+'echo '+text+' | cat > '+filename+' ; cd -')
		else:
			os.system('echo '+text+' | cat > '+filename)
		all_bin = os.popen('ls /usr/local/bin/ | sort | uniq').read().split('\n')
		if 'subl' in all_bin:
			os.system('subl '+fileroot)

