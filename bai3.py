fullname = input("Họ và tên em là:")
print ("",fullname);

def Thuannghich(n):
    str1 = str(n);     
    str2 = str1[::-1]; 
    if (str1 == str2):
        return True;
    else:
        return False;
 
a = int(input("Nhập số nguyên dương a = "));
print("Tổng các chữ số của", a , "là", Thuannghich(a));
