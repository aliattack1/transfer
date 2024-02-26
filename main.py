import random as r
import turtle as t
def set():
    t.speed(100000000000000)
    global al
    global food
    global loc
    global clothes
    global est
    global words
    al = []
    food = []
    loc = []
    clothes = []
    est = []
    words =[]
set()

def al():
    words = al
    play()

def food():
    words = food
    play()

def loc():
    words = loc
    play()

def clo():
    words = clothes
    play()

def es ():
    words = est
    play()


def st3():
    t.pu()
    t.forward(450)
    t.pd()
    t.forward(-450/2)
    t.pu()
    t.forward(-450 / 4)
    t.pd()
    t.forward(-450 / 2)
    t.pu()
    t.forward(-450 / 4)
    t.pd()
    t.forward(-450 / 2)
    t.pu()
    t.home()
    t.pd()

def st4():
    t.pu()
    t.forward(900/14)
    t.pd()
    t.forward(900/7)
    t.pu()
    t.forward(900/7)
    t.pd()
    t.forward(900/7)
    t.pu()
    t.forward(-900)
    t.pu()
    t.pd()
    t.forward(900 / 7)
    t.pu()
    t.forward(900 / 7)
    t.pd()
    t.forward(900 / 7)

def st5():
    t.pd()
    t.forward(50)
    t.pu()
    t.forward(100)
    t.pd()
    t.forward(100)
    t.pu()
    t.forward(100)
    t.pd()
    t.forward(100)
    t.pu()
    t.forward(-900)
    t.pd()
    t.forward(100)
    t.pu()
    t.forward(100)
    t.pd()
    t.forward(100)
    t.pu()
    t.forward(100)
    t.pd()
    t.forward(50)

def st6():
    t.pu()
    t.forward(900/22)
    t.pd()
    t.forward(900/11)
    t.pu()
    t.forward(900 / 11)
    t.pd()
    t.forward(900 / 11)
    t.pu()
    t.forward(900 / 11)
    t.pd()
    t.forward(900 / 11)
    t.pu()
    t.forward(-900)
    t.pd()
    t.forward(900 / 11)
    t.pu()
    t.forward(900 / 11)
    t.pd()
    t.forward(900 / 11)
    t.pu()
    t.forward(900 / 11)
    t.pd()
    t.forward(900 / 11)

def st7():
    t.pd()
    t.forward(900/26)
    t.pu()
    t.forward(900/13)
    t.pd()
    t.forward(900 / 13)
    t.pu()
    t.forward(900 / 13)
    t.pd()
    t.forward(900 / 13)
    t.pu()
    t.forward(900 / 13)
    t.pd()
    t.forward(900 / 13)
    t.pu()
    t.forward(-900)
    t.pd()
    t.forward(900/13)
    t.pu()
    t.forward(900 / 13)
    t.pd()
    t.forward(900 / 13)
    t.pu()
    t.forward(900 / 13)
    t.pd()
    t.forward(900 / 13)
    t.pu()
    t.forward(900 / 13)
    t.pd()
    t.forward(900 / 13/2)




def play():
    word = r.choice(words)
    wordl = (len(word) - 1)
    if wordl == 3:
        st3()
    elif wordl == 4:
        st4()
    elif wordl == 5:
        st5()
    elif wordl == 6:
        st6()
    elif wordl == 7:
        st7()
    t.pu()
    t.home()

    def turn():
        wordi = [str(word) for word in str(word)]
        sas = t.textinput('guess game', 'enter a charecter')

        def a():
            t.left(-90)
            t.forward(25)
            t.forward(-50)
            t.left(70)
            t.forward(-50)
            t.forward(125)
            t.left(40)
            t.forward(-125)
        def std(a,b):
            nd = a
            md = b
            if md == (3):
                if nd == 1:
                    t.pu()
                    t.forward(-225*3/2)
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 2:
                    t.pu()
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 3:
                    t.pu()
                    t.forward(225 * 3 / 2)
                    t.left(90)
                    t.forward(100)
                    t.pd()
            if md == (4):
                if nd == 1:
                    t.pu()
                    t.forward(-2700 / 7)
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 2:
                    t.pu()
                    t.forward(-900 / 7)
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 3:
                    t.pu()
                    t.forward(900 / 7)
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 4:
                    t.pu()
                    t.forward(-2700 / 7)
                    t.left(90)
                    t.forward(100)
                    t.pd()
            if md == (5):
                if nd == 1:
                    t.pu()
                    t.forward(-400)
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 2:
                    t.pu()
                    t.forward(-200)
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 3:
                    t.pu()
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 4:
                    t.pu()
                    t.forward(200)
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 5:
                    t.pu()
                    t.forward(400)
                    t.left(90)
                    t.forward(100)
                    t.pd()
            if md == (6):
                if nd == 1:
                    t.pu()
                    t.forward(-450+(900/11*1))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 2:
                    t.pu()
                    t.forward(-450 + (900 / 11 * 2))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 3:
                    t.pu()
                    t.forward(-450+(900/11*3))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 4:
                    t.pu()
                    t.forward(-450 + (900 / 11 * 4))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 5:
                    t.pu()
                    t.forward(-450+(900/11*5))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 6:
                    t.pu()
                    t.forward(-450 + (900 / 11 * 6))
                    t.left(90)
                    t.forward(100)
                    t.pd()
            if md == (7):
                if nd == 1:
                    t.pu()
                    t.forward(-450 + (900 / 13 * 0))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 2:
                    t.pu()
                    t.forward(-450 + (900 / 13 * 2))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 3:
                    t.pu()
                    t.forward(-450 + (900 / 13 * 4))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 4:
                    t.pu()
                    t.forward(-450 + (900 / 13 * 6))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 5:
                    t.pu()
                    t.forward(-450 + (900 / 13 * 8))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 6:
                    t.pu()
                    t.forward(-450 + (900 / 13 * 10))
                    t.left(90)
                    t.forward(100)
                    t.pd()
                elif nd == 7:
                    t.pu()
                    t.forward(-450 + (900 / 13 * 12))
                    t.left(90)
                    t.forward(100)
                    t.pd()
        def pr(chn):
            ch = (wordi[chn-1])
            if ch == 'a':
                a()
        def app(a,b):
            ki = wordi[a]
            std(a,b)
            pr(ki)
        def do3():
            if sas == (wordi[0]):
                app(1,3)
            if sas == (wordi[1]):
                app(2,3)
            if sas == (wordi[2]):
                app(3,3)

        def do4():
            if sas == (wordi[0]):
                app(1,4)
            if sas == (wordi[1]):
                app(2,4)
            if sas == (wordi[2]):
                app(3,4)
            if sas == (wordi[3]):
                app(4,4)

        def do5():
            if sas == (wordi[0]):
                app(1,5)
            if sas == (wordi[1]):
                app(2,5)
            if sas == (wordi[2]):
                app(3,5)
            if sas == (wordi[3]):
                app(4,5)
            if sas == (wordi[4]):
                app(5,5)
        def do6():
            if sas == (wordi[0]):
                app(1,6)
            if sas == (wordi[1]):
                app(2,6)
            if sas == (wordi[2]):
                app(3,6)
            if sas == (wordi[3]):
                app(4,6)
            if sas == (wordi[4]):
                app(5,6)
            if sas == (wordi[5]):
                app(6,6)

        def do7():
            if sas == (wordi[0]):
                app(1,7)
            if sas == (wordi[1]):
                app(2,7)
            if sas == (wordi[2]):
                app(3,7)
            if sas == (wordi[3]):
                app(4,7)
            if sas == (wordi[4]):
                app(5,7)
            if sas == (wordi[5]):
                app(6,7)
            if sas == (wordi[6]):
                app(7,7)
        if wordl == 3:
            do3()
        elif wordl == 4:
            do4()
        elif wordl == 5:
            do5()
        elif wordl == 6:
            do6()
        elif wordl == 7:
            do7()
    turn()

def game():
    daste = int(t.textinput('word finding game', '1 for all 2 for food 3 for locations 4 for clothes 5 for estelah '))
    if daste == 1:
        al()
    elif daste == 2:
        food()
    elif daste == 3:
        loc()
    elif daste == 4:
        clo()
    elif daste == 5:
        es()


































































def start():
    fas = int(t.textinput('word finding game', 'enter 1 for exit and 2 for play'))
    if fas == 2:
        game()
    elif fas == 1:
        quit()


start()
t.done()