# DERS LİNKİ : https://www.youtube.com/watch?v=XKHEtdqhLK8  -  https://www.youtube.com/watch?v=_wZUNiGtkcw&t=1015s

# ----------------------------------STRİNG TANIM-GİRDİLERİ BÜYÜTME--------------------------------------------------------------------------
# firstName = "ertugrul"
# lastName =  "güneş"
# age = 23
# age += 1

# firstNameUpper = firstName.upper() # firstName içindeki string veriyi tüm küçük harflerini büyük harflere çeviriyor.
# print(" HOŞGELDİN "+ firstNameUpper +"\n") # çevrilen büyük yazıyı ekrana yazdırıyoruz.
# print("firstname = " +firstName + "\n" +"lastname = "+ lastName +"\n"+ "age = "+ age) # string olarak tanımlanan verileri konsol ekranına yazdırıyoruz.

# --------------------------------STR-------------------------------------------------------------------------------------------

# print("yaşınız : " + str(age)) # "str" integer olmadan yazarask type error hatası alırız onun için integer veriyi str ile veriyi string veriye çeviyoruz.

# --------------------------------FLOAT-------------------------------------------------------------------------------------------

# height = 250.5 #float bir değerdir
# widht = 300.5 #float bir değerdir
# a = height * widht # alan hesaplama formülü
# print(a)
# print(type(a)) # type(yazılıcak değer) bu tanım çıktının türünü gösterir.

# ---------------------------------BOOLEAN------------------------------------------------------------------------------------------

# dog = True
# cat = False
# print( "DOG :"+str(dog)+"\n"+ "CAT :"+ str(cat))

# ---------------------------------MULTİPLE ASSİGNMENT------------------------------------------------------------------------------------------

# name,surname , age = "erto","güneş","23"
# s = name+ "\n" + surname+ "\n"  + age
# print(s)


# ---------------------------------String Methods------------------------------------------------------------------------------------------

# name = "erto"

# print(len(name)) #uzunluk String'de kaç karakter olduğunu yazdırır.
# print(name.find("o")) #Girilen Stiring'de "r" karakterinin indexsini bulur ve ekrana yazdırır. NOT: İLK HARF 0 DAN BAŞLAR.
# print(name.capitalize()) #String'in ilk harfini büyük yazar.
# print(name.upper()) #String'in tüm karakterlerini büyük yazar.
# print(name.lower()) #String'in tüm karakterlerini büyük yazar.
# print(name.isdigit()) #String'in sayı olup olmadığını yazdırır.(TRUE - FALSE)
# print(name.isalpha()) #String'in sadece harf içerip içemediğini kontrol edip ekran (TRUE - FALSE ) yazdırır.
# print(name.count("e")) #String'in kaçtane "e" karakteri olduğunu ekrana yazdırır.
# print(name.replace("o","a")) #Stringdeki o harfini a çevirip ekrana yazdırır.
# print(name*3) #String'i 3 kez ekrana yazdırır.

# ---------------------------------Type cast------------------------------------------------------------------------------------------

# x = 1  #int
# y = 2.0 #float
# z ="3"  #str

# +str(x) bu şekilde yazarsak int,float,str değerlerin hepsini string'e çevirip ekrana yazdırır.

# print("X is :"+str(x))
# print("Y is :"+str(y))
# print("Z is :"+str(z))

# ---------------------------------User input------------------------------------------------------------------------------------------

# name = input("ADINIZI GİRİNİZ : ")
# age = int(input("YAŞINIZI GİRİNİZ : "))
# dg = str(input("DOĞUM TARİHİNİ GİRİNİZ : "))

# print("\n"+"Yaşınız "+str(age)+" adınız "+name+ "Doğum tarihiniz "+dg)

# ---------------------------------String Slicing------------------------------------------------------------------------------------------

# name ="Ertugrul Gunes" #string tanımlıyoruz
# first_name = name[0] #string sıfırıncı indexsi alıyoruz oda ilk karakterden başlıyor.
# print(first_name) #ekrana yazdırıyoruz.

# first_name = name[0:2] # : kapsayıcı 0dan başlayıp 2 ye kadar olanları çekiyor ama 2 ci dahil olmuyor
# first_name = name[2:] # :2 den başlayıp geri kalan tüm karakterleri yazar.
# print(first_name)

# ---------------------------------Matematik İşlemleri------------------------------------------------------------------------------------------

# x, y = 9, 5

# +++++++++++++++dört işlem+++++++++++++++++++
# print(x + y) #toplama
# print(x - y) #çıkarma
# print(x * y) #çarpma
# print(x / y) #bölme

# print(x // y) #tam sayı bölme sonucunu ekrana yazdırmak için kullanılır.
# print(x % y)  # kalan bulma için yüzde kullanılır.
# print(x ** y) #sayının üstünü almak için kullanılır.

# +++++++++++++++++ örnek çalışma 1++++++++++++++++

# x = int(input("Sayı Giriniz : "))
# y = int(input("Sayı Giriniz : "))

# print(x + y)
# print(x-y)
# print(x*y)
# print(x/y)

# +++++++++++++++++*****Math formül******++++++++++++++++
# print(round(9.8)) #round sayıyı yuvarlamak için kullanılır.
# print(abs(-9)) #abs mutlak değerini alır yani sıfıra olan uzaklığını
#
# import math #math kütüpanesi
# print(math.sqrt(9)) #kare kökü alma

# print(min(10,5,8,7,9,1)) #parentez içine yazılan değerlerin en küçüğünü alma.
# print(max(10,5,8,7,9,1)) #parentez içine yazılan değerlerin en büyüğünü alma.
