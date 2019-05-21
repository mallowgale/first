f1 = open('words.txt')
words = f1.readlines()

letters = 'qwertyuiopasdfghjklzxcvbnm-1234567890'

check = input()

count = 0 #переменная для подсчета количества предлагаемых слов(max 3 для удобства)
for word in words:
    if (check + '\n') == word:
        print('Правильно')
        count = -1
        break

if count == 0:
    print ('Возможно вы имели в виду:')
    for word in words:
          buff = check
          for i in range(len(check)):
                check = buff
                for letter in letters:
                    check = check[0:i] + letter + check[i+1:]# замена буквы
                    for line in words:
                        if check + '\n' == line:
                            print(check)
                            count += 1
                        if count == 3:
                            break
                    if count == 3:
                        break
                if count == 3:
                    break
f1.close()