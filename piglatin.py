def piglatin_trans(string):
	last=string[0]
	return(string[1:]+last+"ay")












answer=input("hey there! Enter the word you want to latin translate :").lower()
if len(answer) and answer.isalpha():
   print (piglatin_trans(answer))
else :
   print("Invalid word")
