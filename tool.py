#!/usr/bin/python3

def getList(s):
	p = s.split(',')
	ls = list()
	for i in p:
		if '-' in i:
			l, r = map(int, i.split('-'))
			ls += list(range(l, r + 1))
		else:
			ls.append(int(i))
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