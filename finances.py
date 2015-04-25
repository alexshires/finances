#! usr/bin/env python


import pandas as pd
import numpy as np

"""file format = name, cost, date, real(0) or expected(1), scenario=(0,....)"""

class Item:
	def __init__(_name,_cost,_date,_real=False,_scenario=0):
		self.name = _name
		self.cost = _cost
		self.date = _date
		self.real = _real
		self.scenario = _scenario
	def write(f):
		line = "%s\t%s\t%s\t%s\t%s\n" % (self.name, self.cost, self.date, self.real, self.scenario)
		f.write(line)


def recreate_file():
	"""recreates file"""
	f = open('finances.data','w')
	f.write("Name\tCost\tDate\tReal\tScenario")
	f.close()
	

def writeItem(item):
	#writes to file
	f = open('finances.data', 'a')
	item.write(f)
	f.close()
	
def readFile(filename):
	print "reading" , filename
	df = None
	if os.path.exists(filename):
		df = pd.read_csv(filename, sep='\t')
	return df
	
def plot(incdf, outdf, scenario=0):
	
	
def process_file(costfilename, incfilename):
	costdata = readFile(costfilename)
	incdata = readFile(incfilename)
	print costdata
	print incdata
	#calculate cumulative values
	#calculate balance as a function of time
	#find number of scenarios
	#plot income, costs, balance for each
	return

	
if __name__ == '__main__':
	import time
	from argparse import ArgumentParser
	parser = ArgumentParser()
	parser.add_argument("-r", "--recreate", dest='recreate', default=False, action='store_true', help="recreate file")
	parser.add_argument("-p", "--process", dest='process', default=False, action='store_true', help="process file")
	parser.add_argument("-c", "--costfile", dest='costfile', default='finances.data', type=str, help="filename")
	parser.add_argument("-i", "--incfile", dest='incfile', default='income.data', type=str, help="filename")
	parser.add_argument("-s","--start", dest='start', default='010515', type=str, help="filename")
	parser.add_argument("-e","--end", dest='end', default='011015', type=str, help="filename")
	options = parser.parse_args()
	import os
	print os.getcwd()
	#windows
	if os.sys.platform == 'win32' :
		basedir = os.path.join( "C:\\", "Users", "Alex", "Documents", "GitHub", "finances")
		print basedir
		print "does filepath exist", os.path.exists(basedir)
	else :
		print "running on linux"
		exit()
	
	if options.recreate:
		recreate_file()
	
	if options.process:
		process_file(os.path.join(basedir,options.costfile), 
					 os.path.join(basedir,options.incfile))
		