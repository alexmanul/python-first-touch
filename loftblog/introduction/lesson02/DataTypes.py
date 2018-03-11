num = 5  # integer
num_f = 5.5  # float
string = "Hello!"  # str

print(type(num))
print(type(num_f))
print()

print(num.__class__)
print(num_f.__class__)
print(string.__class__)
print(float(num))
print(int(num_f))

print(7 / 2)
print(7 // 2)
print(7 * 2)
print(7 % 2)
print(7 ** 2)

name1 = "Armen Dzhigarkhanyan"
print(name1[0], name1[1], name1[2], name1[3], name1[4])
print(name1[-1], name1[-2], name1[-3], name1[-4], name1[-5])

name2 = "Vakhtang Kikabidze"
print(name1 + " is Armenian actor")
print(name2 + " is Georgian actor")
print("Avtondil " * 3)

my_list = [1, 2, 3, "Ashot", 5.5]
print(my_list[1])
print(my_list[3])

second_list = [0, 77]
print(my_list + second_list)
print(second_list * 2)

