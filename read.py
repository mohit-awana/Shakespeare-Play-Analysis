from nltk.tokenize import sent_tokenize, word_tokenize
import PyPDF2
import csv
import pandas as pd      
doc=['Antony_&_cleopatra','King_Lear','Julius-Caesar','Hamlet','Romeo-and-Juliet','Othello','Macbeth']
keywords=['antony','augustus','cleopatra','brutus','julius']
lst={}
lst1={}

df=pd.DataFrame()
# creating pdf object
for document in doc:
	for keyword in keywords:
		lst[keyword]=0
	pdfobj = open('/home/Mohit/Documents/trse/shakepear\'s_plays/'+document+'.pdf', 'rb')

	# creating pdf reader object
	pdfRead = PyPDF2.PdfFileReader(pdfobj)
	 
	# printing no. of pages in a file
	count=pdfRead.numPages 
	# creating a page object
	for i in range(count+1):
		try:
			pageObj = pdfRead.getPage(i)
			#extracting text
			extract=pageObj.extractText()
			extract=extract.replace('\t','')
			extract=extract.replace('\n','')
			sentences=sent_tokenize(extract)
			for sentence in sentences:
				for keyword in keywords:
					if keyword in sentence.lower():
						lst[keyword]=1
						break
		except:
			pass
	print("document scanned are :"+document)
	lst1[document]=lst.values()
	pdfobj.close()
lst1['characters']=keywords
df = pd.DataFrame.from_dict(lst1)
df=df[['characters','Antony_&_cleopatra','King_Lear','Julius-Caesar','Hamlet','Romeo-and-Juliet','Othello','Macbeth']]
df=df.set_index('characters')
df.to_csv('output.csv')
print(df)