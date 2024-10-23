def kod(n): #функция
    result = ' ' #пременная с результатом
    add_password = [] #список
    pairs = set() #кортеж в котором будет проверяться уникальность чисел
    for i in range(1, 21): #цикл с перебором чисел
        for j in range(i+1, 21): #цикл с перебором чисел
            if n % (i + j) == 0 and ((i, j) not in pairs) and ((j, i) not in pairs): #условие по задаче
                add_password.append((i, j)) #добавление в список уникальных пар
                pairs.add((i, j)) #добавление в кортеж пар
                pairs.add((j, i)) #добавление в кортеж пар
    for password in add_password: #цикл
        result += str(password[0]) + str(password[1]) #добавление пар в результат
    return result #возвращение результата
n = 16 #первая вставка из задачи
password = kod(n) #пеерепенная с функцией
print(f"Число {n} имеет пароль {password}") #вывод на экран
#было тяжеловато если честно