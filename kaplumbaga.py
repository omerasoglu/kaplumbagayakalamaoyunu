import turtle
import random
screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Kaplumbağa Yakalama Oyunu")
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(0, 250)
score_pen.write(f"Skor: {score}", align="center", font=("Arial", 24, "bold"))
t = turtle.Turtle()
t.shape("turtle")
t.color("brown")
t.penup()
t.speed(0)
def move_turtle():
    global t
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
move_turtle()
def catch_turtle(x, y):
    global t, score, score_pen
    # Kaplumbağanın yakalanıp yakalanmadığını kontrol et
    if t.distance(x, y) < 20:
        # Skoru bir artır
        score += 1
        score_pen.clear()
        score_pen.write(f"Skor: {score}", align="center", font=("Arial", 24, "bold"))
        # Kaplumbağayı yeni bir konuma götür
        move_turtle()

screen.onclick(catch_turtle)
timer = 20
timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.goto(0, -250)
timer_pen.write(f"Kalan Süre: {timer}", align="center", font=("Arial", 24, "bold"))

def countdown():
    global timer, timer_pen
    if timer == 0:
        timer_pen.clear()
        timer_pen.write("Oyun Bitti!", align="center", font=("Arial", 24, "bold"))
        return
    timer -= 1
    timer_pen.clear()
    timer_pen.write(f"Kalan Süre: {timer}", align="center", font=("Arial", 24, "bold"))
    screen.ontimer(countdown, 1000)
countdown()
screen.mainloop()
