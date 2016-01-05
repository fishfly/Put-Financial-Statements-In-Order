#coding=utf-8

import sys,os

def main():
	# ensure that we can get the path
	if len(sys.argv)<2:
		print "Usage: python sortFinancialReports.py [path]\n"
		return

	path = sys.argv[1]

	for root, dirs, files in os.walk(path):
		for file in files:
			fpath = root + "\\" + file
			print fpath
			rename(fpath)

def rename(fpath):
	month_r = fpath.rfind("\\")
	month_l = fpath.rfind("\\", 0, month_r)

	month = fpath[month_l+1:month_r]

	fpath_dir = fpath[:month_r]

	year_r = fpath.rfind("\\", 0, month_l+1)
	year_l = fpath.rfind("\\", 0, year_r)

	year = fpath[year_l+1:year_r]

	new_name = "Serpurity-" + year + "." + month + "-"

	fpath_x = fpath.decode('gbk').encode('utf8')

	name = ""

	if fpath_x.find("资产负债")!=-1:
		name = new_name + "balance sheet"
	elif fpath_x.find("科目余额")!=-1:
		name = new_name + "account balance"
	elif fpath_x.find("现金流量")!=-1:
		name = new_name + "cash flow statement"
	elif fpath_x.find("利润表")!=-1:
		name = new_name + "income account"
	elif fpath_x.find("损益表")!=-1:
		name = new_name + "income account"

	if name!="":
		postfix = fpath[fpath.rfind("."):]

		name += postfix

		name = fpath_dir + "\\" + name

		print "-> " + name

		os.rename( fpath, name )
	else:
		pass

	return
	
main()