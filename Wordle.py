from random import randint
import sys
rword=randint(0,1)
o=1

f=["python","english"]
def wordle_2():
    o=0
    w="~~~~~"

    for i in range(10):
        print(f"Слово из {len(f[rword])} букв.Осталось {10-i} попыток")
        o=0
        w=input()
        if len(w) != len(f[rword]):
            print("Недопустимая длина слова(-1 попытка)")
            continue
        y=f[rword]

        for m in range(len(f[rword])):
            if w[m] != y[m]:
                print(" "*(m-1),"*")
                o=o+1

        print(o)
        if o == 0:
            break
    return(o)

o=wordle_2()
if o !=0:
    print("Ты проиграл")
    sys.exit()
else:
    print("win")