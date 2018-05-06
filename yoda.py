#yoda.py
f_num = [int(i) for i in input()]
l_num = [int(i) for i in input()]
it = len(f_num)
diff = len(l_num)-len(f_num)
if diff>0:
    it = len(l_num) #fnum is bigger
    f_num_temp = f_num
    f_num = [0]*abs(diff)
    f_num.extend(f_num_temp) 
elif diff <0:
    it = len(f_num) #lnum is bigger
    l_num_temp = l_num
    l_num = [0]*abs(diff)
    l_num.extend(l_num_temp) 
print(it)

for x in range(0, it):
    if f_num[x] < l_num[x]:
        f_num[x] = ""
    elif f_num[x] > l_num[x]:
        l_num[x] =""
newF = ''.join(map(str,f_num))
newL = ''.join(map(str,l_num))
print(l_num)
print(f_num)
if newF =="":
    newF = "YODA"
else:
    newF = int(newF)
if newL =="":
    newL = "YODA"
else:
    newL = int(newL)

print("{}\n{}".format(newF, newL))


