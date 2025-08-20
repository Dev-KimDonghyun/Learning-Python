# 2025.08.20
# 08_loop.py

print('Do you want to start infinite loop? (y/n)')

answer = input()

print(answer)

def inf() :
    num = 0
    
    while True :
        print(f'Infinite {num}')
        num = num + 1

if answer == 'y' or 'Y' :
    inf()
elif answer == 'n' or 'N' :
    print('Okay, Bye.')
else :
    print('ERROR')