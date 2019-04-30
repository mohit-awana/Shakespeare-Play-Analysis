import csv
import pandas as pd
df=pd.read_csv('output.csv')
df1=df.set_index('characters')
totalplays=list(df1)
def anthony():
	#anthony AND augustus AND NOT cleopatra
	result={}
	a = [x&y for x, y in zip(df1.loc['antony'].values,df1.loc['augustus'].values)]
	b = [x & ~y for x, y in zip( a , df1.loc['cleopatra'].values)]
	result = dict(zip(totalplays,b))
	lst=[]
	print(result)
	for play, value in result.iteritems():
	    if value == 1:
	        lst.append(play)
	if not lst:
		print("no match exist")
	else:
		print("match founded:",lst)

def brutus():
	#Brutus OR Julius AND Augustus
	result={}
	a = [x|y for x, y in zip(df1.loc['brutus'].values,df1.loc['julius'].values)]
	b = [x & y for x, y in zip( a , df1.loc['augustus'].values)]
	result = dict(zip(totalplays,b))
	lst=[]
	print(result)
	for play, value in result.iteritems():
	    if value == 1:
	        lst.append(play)

	if not lst:
		print("no match exist")
	else:
		print("match founded:",lst)

print("find Anthony AND Augustus AND NOT Cleopatra")
anthony()
print("Brutus OR Julius AND Augustus")
brutus()
