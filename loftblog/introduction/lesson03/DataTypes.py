my_t = (1, 2, 3, 4)  # tuple
my_t1 = 1, 2, 3, 4  # tuple
print(type(my_t))
print(type(my_t1))

my_t2 = ()
my_t3 = (50,)
print(my_t[0])
print(my_t[1:3])
del my_t2

my_d = {"city": "Moscow"}  # dict
print(my_d)
print(type(my_d))

my_d1 = {1: "Armen", 2: "Vakhtang", 3: [1, 2, 3]}  # dict
print(my_d1)
print(type(my_d1))
print(my_d1[3])

my_d1[4] = "Ushangi"
print(my_d1)
del my_d1[3]
print(my_d1)

my_d1.clear()
print(my_d1)

del my_d1
print(my_d1)
