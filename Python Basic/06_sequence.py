# 2025.08.20
# 06_sequence.py

x = ['apple', 'banana', 'orange', 'grapes', 'mango', 'pineapple', 'strawberry', 'blueberry', 'watermelon', 'peach', 'kiwi', 'cherry']

# ['APPLE' ,'KIWI']

def way01() :
    apple_value = x[x.index('apple')].upper()
    kiwi_value = x[x.index('kiwi')].upper()

    list_value = [apple_value, kiwi_value]

    print(list_value)

def way02() :
    list_value = []

    for i in range(len(x)) :
        if x[i] == 'apple' or x[i] == 'kiwi' :
            list_value.append(x[i].upper())

    print(list_value)

way01()
way02()