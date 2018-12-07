#Create by Yumeng Yang on 11/10/2018
# -*- coding: utf-8 -*-
import os
import operator

def formGraph(src):
	files = os.listdir(src)
	
	for file in files:

		WordinDoc = {}
		WordinDocId = {}
		print(file)
		with open(src + "/" + file, "r", errors="ignore") as fin:
			id = 0
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
					if newword not in WordinDoc:
						WordinDoc[newword] = id
						WordinDocId[id] = newword
						id+=1

		length = len(WordinDoc)
		s = [1 / length for col in range(length)]
		p = [1 / length for col in range(length)]
		w = [[0 for col in range(length)]for row in range(length)]

		with open(src + "/" + file, "r", errors="ignore") as fin:
			lines = fin.readlines()
			for line in lines:
				words = []
				lastNum = -2
				lastWord = ''
				line = line.strip('\n')
				words += line.split(' ')
				strp = ''
				for word in words:
					if (word == ''):
						continue
					newword = word.split('_')[0]
					num = int(word.split('_')[1])
					# modified
					w[WordinDoc.get(newword)][WordinDoc.get(newword)]+=1
					if (num - lastNum == 1):
						w[WordinDoc.get(newword)][WordinDoc.get(lastWord)]+=1
						w[WordinDoc.get(lastWord)][WordinDoc.get(newword)]+=1
					lastNum = num
					lastWord = newword
		loop = 0
		while(loop < 10):
			for i in range(length):
				Sumji = 0;
				for j in range(length):
					SumWjk = 0
					for k in range(length):
						SumWjk = w[j][k] + SumWjk
					if SumWjk != 0:
						Sumji = s[j] * w[i][j] / SumWjk + Sumji
				s[i] = Sumji * 0.85 + 0.15 * p[i]			
			loop += 1

		# print(s)
		result = {}
		result2gram = {}
		result3gram = {}
		realresult = {}
		# 1-gram
		for i in range(len(s)):
			realresult[WordinDocId.get(i)] = s[i]
		# list1gram = sorted(result.items(),key = lambda x:x[1], reverse = True)
		# fout = open("output" + "/" + "list1gram" + "/" + file, 'w')
		# fout.writelines(str(list1gram))

		# 2-gram
		for i in range(len(w) - 1):
			for j in range(i + 1, len(w[i])):
				if w[i][j] != 0:
					value = s[i] + s[j]
					key = WordinDocId.get(i) + " " + WordinDocId.get(j)
					realresult[key] = value
		# list2gram = sorted(result2gram.items(),key = lambda x:x[1], reverse = True)
		# fout = open("output" + "/" + "list2gram"  + "/" + file, 'w')
		# fout.writelines(str(list2gram))
		#3-gram
		for i in range(len(w) - 2):
			for j in range(i + 1, len(w[i]) - 1):
				for k in range(j + 1, len(w[j])):
					if w[i][j] != 0 and w[j][k] != 0:
						value = s[i] + s[j] + s[k]
						key = WordinDocId.get(i) + " " + WordinDocId.get(j) + " " + WordinDocId.get(k)
						realresult[key] = value
		realresult = sorted(realresult.items(),key = lambda x:x[1], reverse = True)
		# print(realresult)
		fout = open("output" + "/" + "result"  + "/" + file, 'w')
		for i in range(len(realresult)):
			# print(realresult[i][0])
			fout.writelines(realresult[i][0])
			fout.writelines("\n")
		# list3gram = sorted(result2gram.items(),key = lambda x:x[1], reverse = True)
		# fout = open("output" + "/" + "list3gram" + "/" + file, 'w')
		# fout.writelines(str(list3gram))
		# for i in range(len(list1gram)):
		# 	print(WordinDocId.get(list1gram[i][0]))
		# print(s.index(max(s)))
		# print(WordinDocId.get(s.index(max(s))))

if __name__ == '__main__':
	doc = 'processedDoc'
	formGraph(doc)