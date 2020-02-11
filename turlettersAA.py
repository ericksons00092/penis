import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.pu()

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.forward(-700)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
        tur.setheading(0)
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
       
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.pu()

        

        

    elif letter == "C":
        tur.pu()
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
        tur.pd()
        tur.circle(20,-180)
        tur.right(-90)
        tur.right(-90)
        tur.pu()
    elif letter == "D":
        tur.setheading(0)
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
        tur.circle(20,180)
        tur.right(-90)
        tur.right(-90)
        tur.pu()
        tur.right(90)
        tur.right(90)
        tur.forward(-10)
        tur.right(-90)
        tur.right(-90)


        tur.right(-90)
        tur.forward(-40)
        tur.right(90)
     

    elif letter == "E":

       
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)

        tur.right(-90)
        tur.right(-90)

        tur.right(90)

        tur.pu()
    elif letter == "F":
        tur.pu()
        tur.setheading(0)
        tur.forward(110)
        tur.pd()

        tur.backward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(-90)
        tur.forward(20)
        tur.backward(20)
        tur.right(90)
        tur.forward(20)
        tur.backward(40)
        tur.right(-90)
        tur.forward(20)
        tur.pu()
        tur.right(-90)
        tur.forward(-40)
        tur.right(90)

    elif letter == "G":
        tur.pd()
        tur.forward(-1)
        tur.right(-90)
        tur.forward(10)
        tur.right(-90)
        tur.forward(10)
        tur.forward(-10)
        tur.right(-90)
        tur.forward(10)
        tur.right(90)
        tur.circle(-20,180)
        tur.pu()
        		
    elif letter == "H":
        tur.right(90)
        tur.forward(40)
        tur.forward(-20)
        tur.right(90)
        tur.forward(-20)
        tur.right(90)
        tur.forward(-20)
        tur.forward(40)
        tur.right(90)
        tur.pu()
    elif letter == "I":
        tur.right(90)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-90)
        tur.pu()
    elif letter == "J":
        tur.right(90)
        tur.forward(20)
        tur.circle(-30,70)
        tur.circle(-30,-70)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(90)
        tur.pu()
        
        
        
        
    elif letter == "K":
        tur.right(90)
        tur.forward(20)
        tur.right(35)
        tur.forward(-20)
        tur.forward(10)
        tur.right(90)
        tur.forward(-20)
        tur.forward(20)
        tur.right(-35)
        tur.right(-90)
        tur.right(35)
        tur.forward(10)
        tur.right(-90)
        tur.right(-35)
        tur.right(-90)
        tur.forward(-20)
        tur.forward(20)
        tur.forward(20)
        tur.right(90)
        tur.pu()
    elif letter == "L":
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
        tur.forward(20)
        tur.forward(-20)
        tur.right(-90)
        tur.forward(40)
        tur.right(90)
        tur.pu()
    elif letter == "M":
        tur.right(90)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-45)
        tur.forward(20)
        tur.right(-45)
        tur.right(-45)
        tur.forward(20)
        tur.right(45)
        tur.right(45)
        tur.right(45)
        tur.forward(40)
        tur.forward(-40)
        tur.right(45)
        tur.forward(20)
        tur.right(45)
        tur.right(45)
        tur.forward(20)
        tur.right(-45)
        tur.right(-45)
        tur.right(-45)
        tur.right(-45)
        tur.right(-45)
        tur.pu()

        
    
    elif letter == "N":
        tur.right(90)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-25)
        tur.forward(45)
        tur.right(25)
        tur.forward(-40)
        tur.forward(40)
        tur.right(-25)
        tur.forward(-45)
        tur.right(-90)
        tur.right(25)
        tur.pu()

        
   
    elif letter == "O":
        tur.circle(-20,360)
        tur.pu()
    elif letter == "P":
        tur.forward(20)
        tur.circle(-10,180)
        tur.forward(20)
        tur.right(-90)
        tur.forward(-20)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-90)
        tur.pu()
    elif letter == "Q":
        tur.circle(-20,180)
        tur.right(-90)
        tur.circle(20,70)
        tur.circle(20,-70)
        tur.right(90)
        tur.circle(-20,180)
        tur.pu()
    elif letter == "R":
        tur.forward(20)
        tur.circle(-10,180)
        tur.forward(20)
        tur.right(-90)
        tur.forward(-20)
        tur.forward(20)
        tur.right(-45)
        tur.forward(25)
        tur.forward(-25)
        tur.right(45)
        tur.forward(20)
        tur.forward(-40)
        tur.right(-90)
        tur.pu()
    elif letter == "S":
        tur.circle(-20,140)
        tur.circle(20,140)
        tur.pu()
    elif letter == "T":
        tur.forward(20)
        tur.right(-90)
        tur.forward(-40)
        tur.forward(40)
        tur.right(90)
        tur.forward(20)
        tur.forward(-40)
        tur.pu()
    elif letter == "U":
        tur.right(90)
        tur.forward(20)
        tur.circle(20,180)
        tur.forward(20)
        tur.forward(-20)
        tur.circle(20,-180)
        tur.forward(-20)
        tur.right(-90)
        tur.pu()
        
    elif letter == "V":
        tur.right(90)
        tur.right(-45)
        tur.forward(40)
        tur.right(45)
        tur.right(45)
        tur.forward(-40)
        tur.forward(40)
        tur.right(45)
        tur.right(45)
        tur.forward(40)
        tur.right(45)
        tur.right(90)
        tur.pu()
    elif letter == "W":
        tur.right(90)
        tur.right(-45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.right(45)
        tur.right(45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(-40)
        tur.right(-45)
        tur.pu()

    elif letter == "X":
        tur.right(-45)
        tur.forward(40)
        tur.forward(-20)
        tur.right(-45)
        tur.forward(-20)
        tur.forward(40)
        tur.right(90)
        tur.pu()
    elif letter == "Y":
        tur.right(-45)
        tur.forward(20)
        tur.forward(-20)
        tur.right(45)
        tur.right(45)
        tur.right(45)
        tur.forward(20)
        tur.forward(-20)
        tur.right(-45)
        tur.forward(-20)
        tur.right(45)
        tur.right(-90)
        tur.pu()

    elif letter == "Z":
     tur.forward(20)
     tur.right(-45)
     tur.forward(-30)
     tur.right(45)
     tur.forward(20)

     tur.forward(-20)
     tur.right(-45)
     tur.forward(30)
     tur.right(-45)
     tur.right(-45)
     tur.right(-45)
     tur.forward(20)
     tur.right(-90)
     tur.right(-90)
     tur.pu()
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(45)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(50)
#    turtleLetter("S",tur)






    letters = [ "a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for l in letters:
        turtleLetter(l.upper(),tur)
        tur.forward(55)
        tur.pd()

    window.exitonclick()
import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.pu()

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.forward(-700)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
        tur.setheading(0)
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
       
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.pu()

        

        

    elif letter == "C":
        tur.pu()
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
        tur.pd()
        tur.circle(20,-180)
        tur.right(-90)
        tur.right(-90)
        tur.pu()
    elif letter == "D":
        tur.setheading(0)
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
        tur.circle(20,180)
        tur.right(-90)
        tur.right(-90)
        tur.pu()
        tur.right(90)
        tur.right(90)
        tur.forward(-10)
        tur.right(-90)
        tur.right(-90)


        tur.right(-90)
        tur.forward(-40)
        tur.right(90)
     

    elif letter == "E":

       
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(-90)
        tur.right(-90)
        tur.right(-90)

        tur.right(-90)
        tur.right(-90)

        tur.right(90)

        tur.pu()
    elif letter == "F":
        tur.pu()
        tur.setheading(0)
        tur.forward(110)
        tur.pd()

        tur.backward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(-90)
        tur.forward(20)
        tur.backward(20)
        tur.right(90)
        tur.forward(20)
        tur.backward(40)
        tur.right(-90)
        tur.forward(20)
        tur.pu()
        tur.right(-90)
        tur.forward(-40)
        tur.right(90)

    elif letter == "G":
        tur.pd()
        tur.forward(-1)
        tur.right(-90)
        tur.forward(10)
        tur.right(-90)
        tur.forward(10)
        tur.forward(-10)
        tur.right(-90)
        tur.forward(10)
        tur.right(90)
        tur.circle(-20,180)
        tur.pu()
        		
    elif letter == "H":
        tur.right(90)
        tur.forward(40)
        tur.forward(-20)
        tur.right(90)
        tur.forward(-20)
        tur.right(90)
        tur.forward(-20)
        tur.forward(40)
        tur.right(90)
        tur.pu()
    elif letter == "I":
        tur.right(90)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-90)
        tur.pu()
    elif letter == "J":
        tur.right(90)
        tur.forward(20)
        tur.circle(-30,70)
        tur.circle(-30,-70)
        tur.right(-90)
        tur.right(-90)
        tur.forward(20)
        tur.right(90)
        tur.pu()
        
        
        
        
    elif letter == "K":
        tur.right(90)
        tur.forward(20)
        tur.right(35)
        tur.forward(-20)
        tur.forward(10)
        tur.right(90)
        tur.forward(-20)
        tur.forward(20)
        tur.right(-35)
        tur.right(-90)
        tur.right(35)
        tur.forward(10)
        tur.right(-90)
        tur.right(-35)
        tur.right(-90)
        tur.forward(-20)
        tur.forward(20)
        tur.forward(20)
        tur.right(90)
        tur.pu()
    elif letter == "L":
        tur.right(90)
        tur.forward(40)
        tur.right(-90)
        tur.forward(20)
        tur.forward(-20)
        tur.right(-90)
        tur.forward(40)
        tur.right(90)
        tur.pu()
    elif letter == "M":
        tur.right(90)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-45)
        tur.forward(20)
        tur.right(-45)
        tur.right(-45)
        tur.forward(20)
        tur.right(45)
        tur.right(45)
        tur.right(45)
        tur.forward(40)
        tur.forward(-40)
        tur.right(45)
        tur.forward(20)
        tur.right(45)
        tur.right(45)
        tur.forward(20)
        tur.right(-45)
        tur.right(-45)
        tur.right(-45)
        tur.right(-45)
        tur.right(-45)
        tur.pu()

        
    
    elif letter == "N":
        tur.right(90)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-25)
        tur.forward(45)
        tur.right(25)
        tur.forward(-40)
        tur.forward(40)
        tur.right(-25)
        tur.forward(-45)
        tur.right(-90)
        tur.right(25)
        tur.pu()

        
   
    elif letter == "O":
        tur.circle(-20,360)
        tur.pu()
    elif letter == "P":
        tur.forward(20)
        tur.circle(-10,180)
        tur.forward(20)
        tur.right(-90)
        tur.forward(-20)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-90)
        tur.pu()
    elif letter == "Q":
        tur.circle(-20,180)
        tur.right(-90)
        tur.circle(20,70)
        tur.circle(20,-70)
        tur.right(90)
        tur.circle(-20,180)
        tur.pu()
    elif letter == "R":
        tur.forward(20)
        tur.circle(-10,180)
        tur.forward(20)
        tur.right(-90)
        tur.forward(-20)
        tur.forward(20)
        tur.right(-45)
        tur.forward(25)
        tur.forward(-25)
        tur.right(45)
        tur.forward(20)
        tur.forward(-40)
        tur.right(-90)
        tur.pu()
    elif letter == "S":
        tur.circle(-20,140)
        tur.circle(20,140)
        tur.pu()
    elif letter == "T":
        tur.forward(20)
        tur.right(-90)
        tur.forward(-40)
        tur.forward(40)
        tur.right(90)
        tur.forward(20)
        tur.forward(-40)
        tur.pu()
    elif letter == "U":
        tur.right(90)
        tur.forward(20)
        tur.circle(20,180)
        tur.forward(20)
        tur.forward(-20)
        tur.circle(20,-180)
        tur.forward(-20)
        tur.right(-90)
        tur.pu()
        
    elif letter == "V":
        tur.right(90)
        tur.right(-45)
        tur.forward(40)
        tur.right(45)
        tur.right(45)
        tur.forward(-40)
        tur.forward(40)
        tur.right(45)
        tur.right(45)
        tur.forward(40)
        tur.right(45)
        tur.right(90)
        tur.pu()
    elif letter == "W":
        tur.right(90)
        tur.right(-45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.right(45)
        tur.right(45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.forward(-40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(40)
        tur.right(-45)
        tur.right(-45)
        tur.forward(-40)
        tur.right(-45)
        tur.pu()

    elif letter == "X":
        tur.right(-45)
        tur.forward(40)
        tur.forward(-20)
        tur.right(-45)
        tur.forward(-20)
        tur.forward(40)
        tur.right(90)
        tur.pu()
    elif letter == "Y":
        tur.right(-45)
        tur.forward(20)
        tur.forward(-20)
        tur.right(45)
        tur.right(45)
        tur.right(45)
        tur.forward(20)
        tur.forward(-20)
        tur.right(-45)
        tur.forward(-20)
        tur.right(45)
        tur.right(-90)
        tur.pu()

    elif letter == "Z":
     tur.forward(20)
     tur.right(-45)
     tur.forward(-30)
     tur.right(45)
     tur.forward(20)

     tur.forward(-20)
     tur.right(-45)
     tur.forward(30)
     tur.right(-45)
     tur.right(-45)
     tur.right(-45)
     tur.forward(20)
     tur.right(-90)
     tur.right(-90)
     tur.pu()
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(45)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(50)
#    turtleLetter("S",tur)






    letters = [ "a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for l in letters:
        turtleLetter(l.upper(),tur)
        tur.forward(55)
        tur.pd()

    window.exitonclick()
