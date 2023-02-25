print("hello world")
  # جمل الادخال
  # x=input ( )
  # print(x) ---- متغير
# print("x") ---- ثابت
#  arithmetic operations (OPR):  != :لا يساوي
#                               هل  يساوي : = =

x=3
print(x)
print("3")

x="huthaifa"
print(x)
print("hjaj")
print(909)
print("515")
print("MAAN")
print("hello world")
x="the kingdom of jordan"
print(x)
print(52152)

#
 #   عندنا انواع ل ال ( DATA TYPE ) مثال :

A=5
B=6
C=A+B
print(C)

# هون بنتعامل معها كلمات وحروف لانها موضوعه بين ( " رقم " )
a="5"
b="6"
print(a+b)

# ما هي شروط تسمية المتغير
#  اي متغير لازم يبلش في حرف//
#  اي متغير يكون خياره (True) لازم يكتب اول حرف من (True)كبير//

var1=True # --- & False,---صح او غلط
var2=13 # --- Integer (INT):عدد صحيح
var3=1.5 # --- Floot (FLO):فاصلة عشرية
var4="h" # --- String (STR):أحرف

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print("program start")

# هون  عملنا هيك عشان نحول ال Input الى علامه (Integer)عدد صحيح بنعرفه ع انه علامه (MARK)---

mark =input()  # معناها مدخل ---
mark =int(mark)
 # بعد اي (IF) بنحط ( : )

if mark<=49:
    print("F")
    print("WEAK")

if mark>=50:

   print("pass")
   print("well done")

if mark>=55:

    print("C")
    print("good")

if mark>=60:

    print("B")
    print("very good")

if mark>=95:

    print("A+")
    print("EXCELLENT")

if mark < 60 :
    print("fail")
print("program end")

print("program start")

mark =input()
mark = int(mark)

if mark>=50:
    print("pass")

else:
    print("fail")
print("program end")

print("hello please add your mark")

mark= input()
mark=int(mark)

if mark >=0 and mark <=100:
    print("valid")

else:
    print("invalid")
print("thank you")






mark= input()
mark=int(mark)

if mark > 100 or mark < 0:
    print("invalid")
    print("this is wrong")
elif mark <= 50:
     print("pass")
else:
    print("fail")
print("thank you")

#######################

mark_1 = int(input("pleas input second mark\n"))
mark_2 = int(input("pleas input second mark\n"))
mark_3 = int(input("pleas input second mark\n"))

if mark_1 <0 or mark_1 >100:
    print("mark 1 is invalid")

elif mark_2 < 0 or mark_2 > 100:
        print("mark 2 is invalid")

elif mark_3 <0 or mark_3 >100:
    print("mark 3 is invalid")

else:
    avg=(mark_1 + mark_2 + mark_3)/3
    print("your avg is"+ str(avg))


    ########################



    print("your avg is" + str(avg))
    if avg >= 90:
        print("A")

    elif avg>=80:
        print("B")

    elif avg>=70:
        print("C")

    elif avg>=80:
        print("D")

    else:
        print("F")

###################################
marks=[]
print(type(marks))
marks=[67, 78, 77]
print(marks)
print(marks[1])
marks.appand(88)
marks.appand("Hello")
marks.severse()
size=len(marks)
print((marks[1:4]))

A =(10, 20, 30, 40, 30, 20)
B=[10, 20, 30, 40]
C={10, 20, 30}
print(B)
print(len(B))
print(C)
C.append(295)
print(C)
print(len(C))
print(A)
print(len(A))
A.add(30)
print(A)

dictenery={

    "AYL": "MAAN",
    "MARJ ALHMAM": "AMMAN",
    "AYLA": "AQABA",
    "BASTA": "Ma'an",

}
dictenery["MAAN"]
print(dictenery["AYL"])
print(dictenery)

####################


for i in range (5):
     print (b)
if i== 4:
     print ("Hi")
print("The end of the program")