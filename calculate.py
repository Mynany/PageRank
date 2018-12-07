# Created by Yumeng Yang on 11/14/2018

import os
import operator

def calculate(gold, result):
	sum = 0
	rd = [0]*10
	files = os.listdir(gold)
	fileNum = 0
	for file in files:
		if not file.startswith('.'):
			pairResult = []
			pairGold = []
			fileNum += 1
			with open(result + "/" + file, "r", errors="ignore") as fresult:
				lines = fresult.readlines()
				# i = 0
				for line in lines: 
					# if i == 10:
					# 	break
					newline = line.strip("\n")
					pairResult.append(newline)
					# i+=1
			# print(pairResult)
			with open(gold + "/" + file, "r", errors="ignore") as fin:
				lines = fin.readlines()
				for line in lines:
					newline = line.strip("\n").strip(" ")
					pairGold.append(newline)
					# if pairGold in pairResult:
					# 	print(pairResult.index(pairGold))
					# 	print(pairGold)
					# 	print(pairResult[pairResult.index(pairGold)])
			
			
			for i in range(10):
				for k in range(i):
					if k >= len(pairResult):
						break
					if pairResult[k] in pairGold:
						rd[i] = 1/(k + 1) + rd[i]
						# print(rd[i])
						break

			# print(sum)
	# print(sum)
	print(fileNum)
	for i in range(10):
		print(rd[i] / fileNum)

						

if __name__ == '__main__':
	result = 'output/result'
	tfidf = 'output/TFIDFresult'
	preprocessed_doc = 'processedGold'
	calculate(preprocessed_doc, tfidf)