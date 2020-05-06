import pickle
file=open('training_data','r')
dictionary=[]
for line in file:
	tokens=line.split()
	for token in tokens:
		stoken=token.lower()
		if stoken not in dictionary:
			dictionary.append(stoken)

file2=open('dictionary','wb')
dictionary.append('</d>')
dictionary.append('<unk>')
thisdict={}
count=0
for word in dictionary:
	thisdict[word]=count
	count=count+1

pickle.dump(thisdict,file2)
file.close()
file2.close()






