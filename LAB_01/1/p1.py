file=open("input.txt","r")
content=file.read()
print(content)

file2=open("output.txt","w")

file2.write(content)

file2.close()
file.close()


