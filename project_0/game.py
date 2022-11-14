import numpy as np
number = np.random.randint(1, 100)
count = 0

while True:
    count += 1
    predict_number = int(input('Введите число '))
    
    if number > predict_number:
        print('Введите число  больше')
        
    elif number < predict_number:
        print('Введите число меньше')
    
    else:
        print(f'Верно, это число = {predict_number}, за {count} попыток')
        break
        


