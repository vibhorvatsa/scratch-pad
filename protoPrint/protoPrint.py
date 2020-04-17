from __future__ import print_function
import sys

def printIndent(currentIndent, mode, indent=2):
	indentStr = ''
	for step in range(int(currentIndent/indent)):
		indentStr += (' ' * (indent-1)) + "|"
	indentStr=indentStr[:-1]
	print(indentStr, end='') 
	
def protoPrint(msg, startDelim='{', endDelim='}', indent=2):
	currentIndent = 0
	newLine=False
	prevCh = ''
	insideString = False
	for ch in msg:
		if newLine and ch==' ':
			prevCh = ch
			continue
		if(ch == endDelim):
			currentIndent -= indent
			print()
			printIndent(currentIndent, mode='end')
			print(ch, end='')
			newLine=True
		elif(ch==startDelim):
			print()
			printIndent(currentIndent, mode='start')
			print(ch, end='')
			currentIndent += indent
			newLine=True
		elif(ch==' ' and (not prevCh==':') and not insideString):
			newLine = True
		else:
			if(newLine):
				print()
				printIndent(currentIndent, mode='normal')
				ch = ch.lstrip()
				newLine=False		
			print(ch, end='')
			if(ch=='"' and insideString):
				insideString = False
			elif(ch=='"' and not insideString):
				insideString = True
		prevCh = ch
	
def stdinProtoPrint():
	msg = sys.stdin.read()
	protoPrint(msg)

if __name__=="__main__":
	stdinProtoPrint()
