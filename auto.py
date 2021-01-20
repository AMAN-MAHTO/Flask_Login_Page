

l=[15,6,13,22,3,52,2]
print('Orignal list: ',l)
#insertion shorting

for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j >= 0 and key < l[j]:
        l[j+1] = l[j]
        j-=1
    else:
        l[j+1]=key
print(l)

# bubble shorting

n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        
print(l)













# import pyautogui
# import time

# an=[11001,11002,11003,11004,11005,11006,11007,11008,11009,11010]
# nm=['Aman','Kamlesh','Bhanu','Addesh','Atul','Kapil','Kat','Anuska','Ria','Bauua']
# se=['A','B','C','D','E','F','G','H','I','J']
# rn=[1,2,3,4,5,6,7,8,9,10]
# ad=['Delhi','Tamilnadu','Kerla','Jor Bhag','Malivia Nagar','Janak pure','Rohini','Hauz khas','Nagloi','Madhay pradas',]
# time.sleep(5)
# for i in range(len(an)):
#     pyautogui.typewrite(f'insert into student values ({an[i]},"{nm[i]}",11,"{se[i]}",{rn[i]},"{ad[i]}");')
#     pyautogui.press('enter')
