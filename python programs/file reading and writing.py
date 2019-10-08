#writing and appending
text="Sample text to save\n New Line!"
saveFile= open('exampleFie.txt','w')
saveFile.write(text)
saveFile.close()

text2="\nADDED TEXT"
file=open("exampleFie.txt",'a')
file.write(text2)
file.close()
	
read1=open("exampleFie.txt",'r').read()
print(read1)