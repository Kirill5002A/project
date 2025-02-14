import time
import random
import sys

def start_of_game():
    print("Ты проснулся посреди леса около разбившегося самолёта, на твоих часа сейчас вторник 7:30 утра (Ты был без сознания всю ночь. Вы должны были прилететь в понедельник в 23:00). \nПоследнее что ты помнишь это как ты садился на этот самолёт в аэропорту маленькой деревни в тайге. И тут ты скорее всего понял, что об этом не будут сразу сообщать спасателям, поэтому спасатели прибудут только через неделю...")
    time.sleep(7)

    print("На борту был ещё 1 человек и пилот, но ни одного из них ты не нашел")
    print("Твой телефон был разбит, поэтому ты не можешь кому-либо позвонить...")
    time.sleep(4)

    print("Ты решил осмотреться и нашел записку на клочке бумаги:")
    print("Пройди 500 метров на север.")
    time.sleep(3.5)

    print("Ты отправился туда.")

    for i in range(5):
        print(f"Ты придешь через {5-i} секунд")
        time.sleep(1)
        
    print("Ты увидел озеро с шалашом, а рядом лежала приставка похожая на тетрис. На ней была записка на которой написано: 'она подскажет путь' и ты решил его узнать.")
    time.sleep(4.5)

    print("'Приветствую это игра угадай число. Угадай число от 1 до 100'")
    print("Число выбрано, можно начинать!")
    check_number()

secret_number = random.randint(1,100)
print(secret_number) # Для тестирования

def guess_the_number():    
    while True:
        try:
            print(f"Введите число от 0 до 100: ")
            num = int(input())
            if num > 100 or num < 0:
                print("'Это некорректное число!'")
            else:
                return num
                            
        except ValueError:
            print("Введите целое число!")

def check_number():
    while True:
        user_number = guess_the_number() 
        if user_number > secret_number:
            print(f"Ваше число {user_number} больше загаданного.")
        elif user_number < secret_number:
            print(f"Ваше число {user_number} меньше загаданного.")
        else:
            print(f"'Поздравляем вы угадали число {secret_number}. Идите к холму на востоке'")
            middle_of_game()
            break
        
def middle_of_game():
    print("Вы взглянули на смарт часы")
    print("'Вторник 13:16 заряд 97%'")
    time.sleep(2)

    print("Ты хотел уже начать идти, но резко начался дождь, и ты остался в шалаше")

    for i in range(5):
        print(f"Ожидание окончания дождя {5-i}")
        time.sleep(1)
        
    print("'Вторник 18:45 заряд 90%'")
    time.sleep(3)

    print("Пока был дождь ты проголодался, поэтому ты пошел к самолету, и нашел там 3 сухпайка")
    print("Ты съел один, и у тебя осталось еды еще на 2 дня. Потом ты пошел к шалашу")
    print("'Вторник 21:40 заряд 82%'")

    time.sleep(3)
    print("Уже стемнело, и ты пошел спать")

    for i in range(10):
        print(f"Ты спишь {10-i} (эта ночь будет безопасной)")
        time.sleep(1)
        
    print("'Среда 7:13 ||'Заряд 70%'||'")
    time.sleep(3)

    print("Ты умылся в озере и пошел к холму")

    for i in range(5):
        print(f"Ты придешь через {5-i} секунд")
        time.sleep(1)
        
    print("Когда ты пришел ты увидел недавно потушеный костер")
    time.sleep(1)

    print("Ты услышал шаги (ты не знаешь человек это или животное)")

    key_question = input("Будешь убегать?: Да/Нет (y/n) ").lower()

    if not key_question == "да":
        print("Вы решили не убегать.")
        time.sleep(1)
        
        print("Это был тот самый пассажир. Его зовут Джон.")
        time.sleep(1)
    
        print("Он сказал, что он виделся с пилотом и, что он пошел искать деревню на западе в 35км от вас")
        time.sleep(2)
        
        print("Вы решили поискать его вместе")
        print("'Среда 15:30 ||'Заряд 60%'||")
        time.sleep(3)
        
        print("Вы пришли к шалашу, поели и решили поискать чего-нибуль полезного в самолете")
        print("'Среда 21:20 ||'Заряд 50%'||")
        time.sleep(3)
        
        print("Вы нашли 2 батарейки и содрали ткань с сидений чтобы ей укрываться и решили лечь спать")
        time.sleep(0.5)

        for i in range(5):
            print(f"Ты спишь {5-i} (у тебя плохое предчувствие)")
            time.sleep(1)
            
        print("'Четверг 01:42 ||'Заряд 40%'||")
        time.sleep(3)

        print("Тебя разбудил Джон, и ты увидел что к вам пришел Интеллектуальный Медведь")
        time.sleep(2)

        print('Медвель сказал: "Если разгадаешь мою загадку, то я вас отпущу!"')
        
        boss_fight()
        
    else:
        not_a_very_good_ending_to_the_game()        

def boss_fight():
    random_number_puzzles = random.randint(0, 2)

    list_of_answer = ["пила", "самолет", "пылесос"]
    list_of_suggestion = ["Зубы остры, да не волк, я дрова готовлю впрок", "Крылья есть, а всё ж не птица, он по небу быстро мчится", "Длинный хобот, но не слон, чистоту наводит он"]
    
    answer_on_suggestion = list_of_answer[random_number_puzzles]

    print(list_of_suggestion[random_number_puzzles])
    
    users_answer_to_the_riddle = input("Ваш ответ (постарайтесь быть грамотным🙃): ").lower()

    if users_answer_to_the_riddle == answer_on_suggestion:
        print("Хорошо, я вас отпускаю.")
        good_ending_to_the_game()
    else:
        print("Неправильно! \nВас сьел Интелектуальный Медведь...")
        time.sleep(0.5)
        print("Игра окончена на плохой концовке...")
        sys.exit()

def gallows_game():
    random_num_for_question = random.randint(0, 2)

    tips_on_answer = ["Программа переводящая код в машинный", "летающий транспорт", "предмет, который выводит изображение на монитор"]
    true_answer = ["компилятор", "самолет", "видеокарта"]
    
    random_question = tips_on_answer[random_num_for_question]
    random_answer = true_answer[random_num_for_question]

    list_letter = list(random_answer)  

    print(list_letter)

    encrypted_word = ' '.join(['_' for _ in list_letter])
    print(f"Слово: {encrypted_word}")
    time.sleep(1)
    guessed_letters = [] 
    
    heart = '❤️'
    number_of_hearts = 6

    lives = heart * number_of_hearts
    
    print(f"Количество жизней 💓: {lives}  ({number_of_hearts})")
    time.sleep(1)

    print(f"Подсказка: {random_question}")

    while number_of_hearts > 0:
        user_answer_on_mystery = input("Введите букву: ").lower()

        if len(user_answer_on_mystery) == 1 and user_answer_on_mystery.isalpha():
            if user_answer_on_mystery in guessed_letters:
                print("Вы уже угадали эту букву.")
                continue
            
            guessed_letters.append(user_answer_on_mystery)

            if user_answer_on_mystery in list_letter:
                print("Правильно!")
                
                encrypted_word = ' '.join([letter if letter in guessed_letters else '_' for letter in list_letter])
                print(f"Слово: {encrypted_word}")

                if '_' not in encrypted_word:
                    print("Поздравляем! Вы угадали слово!")
                    break
            else:
                number_of_hearts -= 1
                print(f"Неправильно! Осталось попыток: {heart * number_of_hearts}  ({number_of_hearts})")
        else:
            print("Введите одну букву.")

    if number_of_hearts == 0:
        print(f"Вы исчерпали все попытки! Загаданное слово было: {random_answer}")

        
def not_a_very_good_ending_to_the_game():
    print("Ты так и не смог найти смелости вернуться туда... Ты выживал 2 недели в лесу пока тебя не нашли спасатели.")
    time.sleep(2)
    
    print("Игра окончена на не лучшей концовке!")
            
def good_ending_to_the_game():
    print("Интеллектуальный Медведь ушел и вы легли спать")
    print("'Четверг 8:10 ||'Заряд 20%'||")
    print("После тяжелой ночи, вы пошли искать пилота на западе")


    for i in range(10):
        print(f"Вы идете {10-i}")
        time.sleep(1)
    print("'Четверг 14:20 ||'Заряд 3 %'||")
    time.sleep(3)

    print("Пройдя где-то 10 км вы нашли лагерь где ночевал пилот, и у вас разрядились часы")
    time.sleep(3)

    print("Позже вы нашли и самого пилота")
    time.sleep(1)
    print("У него была спутниковая рация, но при падении он потерял батарейки")
    time.sleep(1)
    print("Вы дали ему батарейки и позвали на помощь по рации...")
    time.sleep(2)

    print("Джон предложил вам сыграть в виселицу, чтобы время быстрее пролетело!")
    time.sleep(1)

    answer_on_gallows = input("Хотите сыграть с Джоном в игру?: Да/Нет (y/n): ").lower()
    
    if answer_on_gallows in ['yes', 'да', 'y', 'д']:
        print("Добро пожаловать! Это игра виселица!")
        time.sleep(1)
        gallows_game()
    
    else:
        print("Вы отказались.")

    print("'Четверг 18:09 ||'Идет зарядка 25%'||")
    time.sleep(3)

    print("За вами прилетели спасатели на вертолете, и вы летите в ближайший город.")
    print("Игра окончена на хорошей концовке. Поздравляем!")

def wordle():
    rword=random.randint(0,6)
    o=0

    print("Подсказка: '*'- буквы нет в загаданном слове,")
    print("'+'- буква есть в этом слове, но стоит не на своем месте")
    f=["python","english","print","version","ocean","input","random"]
    o=0
    w="~~~~~"

    for i in range(10):
        print(f"Слово из {len(f[rword])} букв.Осталось {10-i} попыток")
        o=0
        o1=0
        w=input(" ").lower()

        if len(w) != len(f[rword]):
            print("Недопустимая длина слова(-1 попытка)")
            continue
        y=f[rword]

        for m in range(len(f[rword])):
            if w[m] != y[m]:
                if w[m] not in y:
                    print(" "*(m),"*")
                    o=o+1
                else:
                    print(" "*(m),"+")
                    o1=o1+1

        print(f"В слове нет {o} букв")
        print(f"Стоит не на своем месте {o1} букв")
        if o == 0:
            if o1 ==0:
                break
    return(o,w)
    
while True:
    print("______________________________________________________________")
    print("|                                                            |")
    print("|                                                            |")
    print("|Добро пожаловать! Это консольная игра - выживалка с сюжетом.|")
    print("|У нас также есть еще одна игра.                             |")
    print("|Чтобы ее начать введите wordle на слелующей строке          |")
    print("|                                                            |")
    print("|                                                            |")
    print("|____________________________________________________________|")
    start_the_game_q = input("Хотите начать игру (Да/Нет (y/n)): ").lower()
    if start_the_game_q =="wordle":
        o,w=wordle()
        if len(w)<2:
            print("Ты проиграл")
            sys.exit()
        else:
            if o !=0:
                print("Ты проиграл")
                sys.exit()
            else:
                print("win")

    if start_the_game_q in ['yes', 'да', 'y', 'д']:
        start_of_game()
    else:
        print("Надеемся что вы еще поиграете в нашу игру! 🙁")
        break
    
    print("Хотите сыграть еще раз? 😉")
    
    continuation_the_game_q = input("Да/Нет (y/n): ").lower()
    
    if continuation_the_game_q in ['yes', 'да', 'y', 'д']:
        start_of_game()
    else:
        print("До скорых встреч! 😉")
        break