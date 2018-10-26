var1 = "Guru99!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])
print (var1*2)

print (var1 + var2)
print (var1[1])
print (var1[1:4])
print ("u" in var1)
print ("a" in var1)

print (var1[:6])
print (var1[0:6] + var2)

var3 = var2.replace('Testing','Industry')

print (var3)

print (var2.capitalize())

tup1 = (23,42,57,'JAL',);

print(tup1[0:4])

print(tup1[0:3])

print(tup1[0])

print("------------Packing and upacking-------------------")

Iphone7 = ('Apple',2017,'2GB','32GB',);
(Company,Year_of_Manufacture,RAM,ROM) = Iphone7

print(Company)
print(Year_of_Manufacture)
print(RAM)
print(ROM)

print("==================Comparing tuples===========================")

f= (10,25,)
g= (5,58,)


if(f>g): print("F is greater") 
else: print("g is greater")


print("=================each tuple is a key value pair================")

a = {'x':100, 'y':200}
b = list(a.items())
print(b)

print("================Slicing of Tuples===============")


x = ("a", "b","c", "d", "e")
print(x[2:4])

print("=============Dictinary===================")



Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}  
#Dict1 = (18,12,22,25,)
Dict.update({"Sarah":9})

del Dict ['Charlie'] # Remove it and find the difference

Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}

print (Dict['Tiffany'])

print (Dict)


studentX=Boys.copy()
studentY=Girls.copy()

print(studentX)
print(studentY)

#print(Dict1[2])
print("======================Dictinary  test 2 ====================")

Dict1 = {'Sim': 18,'Charliee':12,'Tiffanye':22,'Roberts':25}
Boys1 = {'Sim': 18,'Charlies':12,'Roberts':25}
Girls1 = {'Tiffanye':22}
for key in list(Dict1.keys()):
    if key in list(Boys1.keys()):
        print(True)
    else:       
        print(False)

