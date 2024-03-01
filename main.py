# #gets hour
# int(input("Какой сейчас час?"))
# #gets day
# day = int(input("Какой сейчас день?"))
# #gets month
# month = int(input("Какой сейчас месяц?"))
# #hets year
# year = int(input("Какой сейчас год?))
# #gets all
# print("Сейчас", day,"часов" month,"месяцев" year, "года)
# a = int(5.99999)
# print(a)
# x = str(5)
# print(type(x))
# x = float(input())
# print(x)
# a = "Hello"
# b = "Artem"
# print(a + " " + b)
# numbers = 0123456789
# letters = "Я програмист"
# print(nummbers + letters)
# a = '5'
# b = '4'
# print(a + b)
# a = "hello"
# b = 5
# c = a*b
# print(c)
print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы:")

# Допиши код вместо "..."
qestions = [
 " 1. Как называется компания, которая создается для развития новой идеи или инновационного продукта? Правильно!",
"2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли? Правильно!",
"3. Как называется капитал, который дают инвесторы на развитие стартапа? Правильно!",
"4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций? Правильно!",
"5. Какой план создают перед тем, как открывать стартап и занимать деньги? Правильно!",
"6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги? Правильно!",
]
answers = [
 " 1:Стартап"
"2:Инвестор"
"3:Инвестиция"
"4:MVP"
"5;Бизнес-план"
"6:Конкуренты"
"7:Прибыль"
]

print(qestions[0])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
else:
    print("Неправильно.")

print(qestions[1])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[1].lower():
    print("Правильно!")
else:
    print("Неправильно.")

print(qestions[2])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[2].lower():
    print("Правильно!")
else:
    print("Неправильно.")

print(qestions[3])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[3].lower():
    print("Правильно!")
else:
    print("Неправильно.")
print(qestions[4])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[4].lower():
    print("Правильно!")
else:
    print("Неправильно.")

print(qestions[5])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[5].lower():
    print("Правильно!")
else:
    print("Неправильно.")

print(qestions[6])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[6].lower():
    print("Правильно!")
else:
    print("Неправильно.")

print(qestions[7])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[7].lower():
    print("Правильно!")
else:
    print("Неправильно.")
