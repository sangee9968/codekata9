n=input()
m=list(n)
for i in range(0,len(m)+1,2):
  print(m[i],end="")
print(end=" ")  
for j in range(1,len(m)+1,2):
  #print result
  print(m[j],end="")
  
