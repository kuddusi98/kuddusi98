sayi = input("enter number")
count=0
for i in range(len(sayi)):
    if sayi[i]==sayi[-1*(i+1)]:
        count = count + 1
    else:break
if count==len(sayi):
    print("number is palindrome")
else: print("number is not palindrome")
#   12321
#   01234
#-  54321