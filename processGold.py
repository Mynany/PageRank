#Create by Yumeng Yang on 11/13/2018

import os
import operator

def preprocess(src, output): 
	import re
	from nltk.stem import PorterStemmer
	from nltk.tokenize import sent_tokenize, word_tokenize
	from nltk import word_tokenize
	from nltk.corpus import stopwords

	stop = set(stopwords.words('english'))
	ps = PorterStemmer()
	files = os.listdir(src)
	for file in files:
		result = []
		print(file);
		with open(src + "/" + file, "r", errors="ignore") as fin:
			lines = fin.readlines()
			for line in lines:
				words = []
				line = line.strip('\n')
				words += line.split(' ')
				strp = ''
				for word in words:
					if word.lower() in stop: 
						continue
					word = ps.stem(word.lower())
					print(word)
					strp = ''.join(word)
					result.append(strp)
					result.append(' ')
				result.append('\n')
		# print(result)
		fout = open(output + "/" + file, 'w')
		fout.writelines(result)

if __name__ == '__main__':
	doc = 'www/gold'
	preprocessed_doc = 'processedGold'
	preprocess(doc, preprocessed_doc)