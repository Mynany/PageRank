#Create by Yumeng Yang on 11/10/2018
# -*- coding: utf-8 -*-
import os
import operator
import math

def formGraph(src):
	WordinCollection = {}
	WordinDoc = {}
	docNum = 0
	files = os.listdir(src)
	
	for file in files:
		# print(file)
		docNum += 1
		WordinDoc[file] = {}
		with open(src + "/" + file, "r", errors="ignore") as fin:
			lines = fin.readlines()
			for line in lines:
				words = []
				last = -2
				line = line.strip('\n')
				words += line.split(' ')
				strp = ''
				for word in words: 
					if (word == ''):
						continue
					newword = word.split('_')[0]
					num = word.split('_')[1]
					if newword not in WordinDoc[file]:
						WordinDoc[file][newword] = 1
						if newword not in WordinCollection:
							WordinCollection[newword] = 1
						else:
							WordinCollection[newword] += 1
					else:
						WordinDoc[file][newword] += 1
	# print(WordinDoc)
	# print(WordinCollection)
	files = os.listdir(src)
	
	for file in files:
		gramRate = {}
		with open(src + "/" + file, "r", errors="ignore") as f:
			lines = f.readlines()
			for line in lines:
				words = []
				firstNum = -3
				secondNum = -2
				firstWord = ""
				secondWord = ""
				line = line.strip('\n')
				words += line.split(' ')
				strp = ''
				for word in words:
					if (word == ''):
						continue
					newword = word.split('_')[0]
					num = int(word.split('_')[1])
					rate = WordinDoc[file][newword]/math.log(docNum/WordinCollection[newword],2)
					gramRate[newword] = rate
					if int(num) - secondNum == 1:
						new = secondWord + " " + newword
						secondRate = WordinDoc[file][secondWord]/math.log(docNum/WordinCollection[secondWord],2)
						newrate = rate + secondRate
						gramRate[new] = newrate
						if num - firstNum == 2:
							new = firstWord + " " + secondWord + " " + newword
							firstRate = WordinDoc[file][firstWord]/math.log(docNum/WordinCollection[firstWord],2)
							secondRate = WordinDoc[file][secondWord]/math.log(docNum/WordinCollection[secondWord],2)
							newrate = rate + firstRate + secondRate
							gramRate[new] = newrate
					temp = secondNum
					secondNum = int(num)
					firstNum = temp
					tempword = secondWord
					secondWord = newword
					firstWord = tempword
		sortedRate = sorted(gramRate.items(),key = lambda x:x[1], reverse = True)
		print(sortedRate)
		fout = open("output" + "/" + "TFIDFresult"  + "/" + file, 'w')
		for i in range(len(sortedRate)):
			fout.writelines(sortedRate[i][0])
			fout.writelines("\n")


		

if __name__ == '__main__':
	doc = 'processedDoc'
	formGraph(doc)