import random

random_number = random.randint(1,100)

print(ramdom_number)

game_count = 1

while True:
    
    my_number = int(input("1-100 사이의 숫자를 입력학세요"))
    
    if my_number > ramdom_number:
        print('Down!!')
    elif my_number < ramdom_number:
        print('UP!!')
    else 
        print('축하합니다.')
        break
    
    game_count = game_count + 1