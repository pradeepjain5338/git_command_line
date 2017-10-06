with open("text.txt","w") as my_file:
  my_file.write("Hey there")
  
if my_file.closed!=True:
  my_file.close()
  
  
print my_file.closed
  