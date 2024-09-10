"""
بازي سنگ ، کاغذ ، قيچي با پايتون و کمک اعداد رندوم بنويسيد .

"""


##colors = ["red", "green", "blue", "crimson", "yellow", "sky"]
##colors.sort(key=lambda x: -1*len(x))
##print(colors)

print("====================")

##evens = []
##for i in range(355, 400):
##    if i % 2 ==0:
##        evens.append(i)
##
##print(evens)
##
##ev = [i for i in range(355, 400)]
##print(ev)



##info = {"name": "mojtaba", "city": "karaj", "age": 38}
##
##for i in info:
##    print(i)


print("====================")

##print(info.keys())
##for i in info.keys():
##    print(i)

##print(info.values())
##for i in info.values():
##    print(i)

##print(info.items())
##for key, value in info.items():
##    print(f"key == {key}.........value : {value}")


##a , b = 10, 60
##print(a, b)


##numbers = []
##
##while (current := input("please enter a number : ")) != "0":
##    numbers.append(current)
##    
##
##print(numbers)



##print(a := 50)



import random as rn
##for i in range(10):
##rn.seed(8)
##    print(rn.random())
print(rn.randint(10000, 404144))

print(rn.randrange(40, 90))


colors = ["red", "green", "blue", "crimson", "yellow", "sky",
          "white", "black"]
human = ["mojtaba", "armin", "mobina", "kasra", "saman", "aryan"]
cars = ["benz", "bmw", "pride", "neysan", "fotgoon"
        , "gari", "lamborghini"]

def shuffle(iterable):
    for i in range(3):
        rn.shuffle(iterable)
    

def pool(car_list, human_list, color_list):
    shuffle(car_list)
    shuffle(human_list)
    shuffle(color_list)
    return f"{rn.choice(human_list)} has won {rn.choice(color_list)} {rn.choice(car_list)}"

for i in range(6):
    print(pool(cars, human, colors))
    
def add(a, b):
    return a+b
print(add(3, 6))



print("====================")

gun = [0,0,0,0,0,1,0]
for i in range(3):
    rn.shuffle(gun)

player_one = input("player one : ")
player_two = input("player two: ")

turn = rn.randint(1, 3)
print(turn)
if turn == 1:
    p1 = player_one
    p2 = player_two
else:
    p1 = player_two
    p2 = player_one


trigger = gun.pop() 

while len(gun) > 0 :
    
    if trigger == 0:
        print(f"{p1} shoot {p2}")
        spare = p1
        p1 = p2
        p2 = spare
        trigger = gun.pop() 
    else:
        print(f"{p1} killed {p2}")
        break
        
    
































##rn.shuffle(colors)
##print(colors)

##choice = rn.randint(0, len(colors)-1)
##print(colors[choice])

##print(rn.choice(colors))

##print(rn.choices(colors, k=10, weights=[50,0,0,0,50,0]))




























































































    
