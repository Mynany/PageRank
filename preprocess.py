#Create by Yumeng Yang on 11/10/2018

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
# NN NNS NNP NNPS JJ
	files = os.listdir(src)
	for file in files:
		result = []
		print(file);
		with open(src + "/" + file, "r", errors="ignore") as fin:
			punctuations = ',.%'
			lines = fin.readlines()
			for line in lines:
				words = []
				line = line.strip('\n')
				words += line.split(' ')
				strp = ''
				num = -1
				for word in words:
					num = num + 1 
					if(word.endswith("NN") or word.endswith("NNS") or word.endswith("NNP") or word.endswith("NNPS") or word.endswith("JJ")):
						word = word.split('_')[0];
					else:
						continue
					if word in punctuations:
						num = 0
						continue
					if word.lower() in stop: 
						continue
					word = ps.stem(word.lower())
					word = word + '_' + str(num)

					print(word)
					strp = ''.join(word)
					result.append(strp)
					result.append(' ')
		# print(result)
		fout = open(output + "/" + file, 'w')
		fout.writelines(result)

if __name__ == '__main__':
	doc = 'www/abstracts'
	preprocessed_doc = 'output'
	preprocess(doc, preprocessed_doc)