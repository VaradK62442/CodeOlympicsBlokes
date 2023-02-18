# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
for line in  sys.stdin:
    k = int(line.split(' ')[0])
    s = int(line.split(' ')[1])

total = 0
if k*3 == s:
    print(1)
else:
    for x in range(k+1):
        for y in range(k+1):
            for z in range(k+1):
                if (x+y+z)==s:
                    total +=1
    print(total)