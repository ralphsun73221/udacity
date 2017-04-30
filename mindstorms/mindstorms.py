import turtle
def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)
        #這可以用來畫三角形

#def draw_square(some_turtle):
    #for i in range(1,5): #這邊編譯器會出現Unused variable'i'的警示，但還是可以執行
        #some_turtle.forward(100)
        #some_turtle.right(90)
        #這串主要用途在於讓原本那一大串重複執行的code可以自動執行四次，並且畫出正方形

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue", "green")
    brad.speed('normal')
    #之前寫成turtle.XXX但發現根本不是這樣寫，要寫成brad.XXX才行
    
    #for i in range(1,5):
        #brad.forward(100)
        #brad.right(90)
        #這邊是另外一種寫法，直接在同樣的fun裡面直接執行迴圈，好處在於可以不用再寫一個fun，但前提是除非這一串只用這一次。
    
    #for i in range(1,37):
        #draw_square(brad)
        #brad.right(10)
    #重複迴圈讓他畫成一個圓形
    #把上面寫好的def拿過來用，把()填入這邊定義的brad，他就會去用上面的fun套用到bard

    draw_triangle(brad)
    

    #angie = turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("yellow")
    #angie.circle(100)
    #另外一串畫圖，用烏龜畫圈圈

    window.exitonclick()

draw_art()