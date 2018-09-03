print("""
you enter a dark room with two doorsself.do you go through
door #1 or door #2?
""")

door=input(">")

if  door=="1":
    print("there is a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1.take the cake.")
    print("2.Scream the bear.")
    print("or maybe you can scare the bear by using fire! please print 'fire'!!!")
    bear=input(">")

    if bear=="1":
        print("the bear eats your  face off.good job!")
    elif bear=="2":
        print("the bear eats your leg.good job!")
    else:
        print(f"well,doing {bear} is properly better.")
        print("Bear run away.")
        #original
        print("you walk and walk.you find a ring!")
        print("""you remind of the lord of rings.suddendly ,you become Gollum!
         ok! now ,you say two words like him usually say.
         print the two  words！！now！
        """)
        two_words=input(">")
        if two_words=="My precious" or two_words=="my precious":
            print("ok!your lord,me .let you go!!haha")
        else:
            print("you become my slave forever.")
elif door=="2":
    print("you stare into the endless abyss at cthulhu's retina.")
    print("1.blueberries")
    print("2.yellow jacket clothespins")
    print("3.understanding revolvers yelling melodies.")
    insanity=input(">")
    if insanity=="1" or insanity=="2":
        print("your body survives powered by a mind of jello.")
        print("Good jobs!")
    else:
        print("the insanity rots your eyes into a pool of muck.")
        print("Good jobs!")
else:
    print("you stumble around and fall on a knife and die.Good jobs!")
