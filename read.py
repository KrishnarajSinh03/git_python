#read
f=open("Python/abc.txt","r")
data=f.read()
print("file content:",data)
f.close
#read line      
f=open("Python/abc.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)  
f.close   
#readlines      
f=open("Python/abc.txt","r")
lines=f.readlines()
print("list of lines:",lines)
print("Number of lines:",len(lines)) 
f.close()
#read specific line
f=open("Python/abc.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()