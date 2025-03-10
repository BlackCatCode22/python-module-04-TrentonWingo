inp=input('Enter a file name: ')
try:
    fhand=open(inp)
except:
    print('Bad file name')
    quit()
count=0
for line in fhand:
       count+=1
       x=line.split()
       print(x[1])
print('There were',count,'lines that start with From in the file:',inp)
