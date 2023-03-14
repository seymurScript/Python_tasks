
#Tam ədədlərin qiymətlərinin yerini dəyişmək

a = int(input("1-ci eded: "))
b = int(input("2-ci eded: "))

#Burada ededlerin yerini deyişirik
a, b = b, a

#çıxışa verende görerik ki ededlerin yeri dəyişilib.
print("1-ci eded:", a)
print("2-ci eded:", b)
