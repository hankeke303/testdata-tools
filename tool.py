#!/usr/bin/python3

lleft = ''

def ssmake(s):
	return lleft + str(s)

def mkstring(s):
	return '\'' + s + '\''

def clearstring(s):
	return s.replace('__FSDR_ACA__HYZX__YQL__HKK___', '-')

def getList(s):
	global lleft
	p = s.split(',')
	ls = list()
	for i in p:
		i = i.replace(' ', '')
		i = i.replace('\\-', '__FSDR_ACA__HYZX__YQL__HKK___')
		if '-' in i:
			if '(' in i:
				lleft, rright = i.split('(')
				rright = rright[:-1]
				l, r = map(int, rright.split('-'))
				ls += map(ssmake, range(l, r + 1))
			else:
				l, r = map(int, i.split('-'))
				ls += map(str, list(range(l, r + 1)))
		else:
			ls.append(i)
	ls = list(map(clearstring, ls))
	return ls

fl = open("data.yml", "w")
input_pre = input("Input-pre: ")
input_suf = input("Input-suf: ")
if (input_suf == ''):
	input_suf = 'in'
output_pre = input("Output-pre: ")
if (output_pre == ''):
	output_pre = input_pre
output_suf = input("Output-suf: ")
if (output_suf == ''):
	output_suf = 'out'

n = input("Numbers of subtasks: ")
if n == '':
	n = 0
n = int(n)
lst = range(0, n)

if n > 0:
	fl.write('subtasks:\n')
	for i in lst:
		tasks = input("subtask-" + str(i + 1) + ": ")
		pre, detail = tasks.split(":")
		
		if "(" in pre:
			sc, tp = pre.split("(")
			tp = tp.split(")")[0]
			fl.write('  - score: ' + sc + '\n')
			if tp != "mul" and tp != "min" and tp != "max" and tp != "sum":
				print("Type Error!")
				fl.truncate(0)
				fl.close()
				exit()
			fl.write('    type: ' + tp + '\n')
		else:
			fl.write('  - score: ' + pre + '\n')
			fl.write('    type: ' + 'min' + '\n')
		
		ls = getList(detail)
		fl.write('    cases: ' + str(ls) + '\n')
	fl.write('\n')

fl.write('inputFile: \'' + input_pre + '#.' + input_suf + '\'\n')
fl.write('outputFile: \'' + output_pre + '#.' + output_suf + '\'\n')
fl.close()