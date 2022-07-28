import random
from turtle import Turtle, Screen
import time
import sys

def print(words):
  words
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()


t = Turtle()
w = Turtle()
w.hideturtle()
w.color('blue')

s = Screen()

t.speed(0)
t.width(20)



def start_game():
  
  wordbank = ['sandwich', 'house', 'pizza', 'grape', 'nba2k', 'minecraft', 'joemama', 'askew', 'bite', 'mario', 'wario', 'luigi', 'computer'] 
  word = random.choice(wordbank)
  guess = '_ ' * len(word)
  print(guess)
  lives = 11

  while lives > 0 and guess.find('_') != -1: 
    digit = (input('Enter a letter: '))[0:1]
    changed = False
    for x in range(len(word)):
      if word[x:x+1] == digit:
        changed = True
        guess =  guess[0:2*x] + digit + guess[2*x + 1:]
    print (guess)
    if changed == False:
      lives -= 1
      print('The letter is not in the word, you lost a life\n')
      draw_limbs(lives)
    else:
      print ('The letter is correct\n')
    w.clear()
    w.penup()
    w.goto(-120,50)
    w.pendown()
    w.write( 'You have ' + str(lives) + ' lives', font = ('Sans', 40, 'italic'))
    

  w.penup()
  w.goto(-120,50)
  w.pendown()
  w.clear()
  if lives == 0:
    w.write(' You Lost, Game Over ', font=("Garamond", 40, "italic"))
  else:
    w.write(' You Won, Hurray ', font=("Garamond", 40, "italic"))

def draw_limbs(num):
  if num == 10:
    draw_head()
  elif num == 9:
    draw_eyes()
  elif num == 8:
    draw_nose()
  elif num == 7:
    draw_mouth()
  elif num == 6:
    draw_neck()
  elif num == 5:
    draw_arm(1)
  elif num == 4:
    draw_arm(0)
  elif num == 3:
    t.forward(190)
  elif num == 2:
    draw_leg(1)
  elif num == 1:
    draw_leg(0)
  

def draw_head():
  t.width(1)
  t.setheading(180)
  t.begin_fill()
  t.circle(40, steps = 250)
  t.end_fill()

def draw_eyes():
  t.hideturtle()
  t.setheading(270)
  t.width(1)
  t.fillcolor('white')
  t.forward(20)
  t.right(90)
  t.forward(15)
  t.begin_fill()
  t.circle(5, steps = 200)
  t.end_fill()

  t.right(180)
  t.forward(30)
  t.right(180)

  t.begin_fill()
  t.circle(5, steps = 200)
  t.end_fill()

  t.forward(15)
  t.left(90)
  t.forward(20)

def draw_nose():
  t.begin_fill()
  t.left(30)
  t.forward(10)
  t.right(120)
  t.forward(10)
  t.right(120)
  t.forward(10)
  t.right(150)
  t.forward(40)
  t.end_fill()
  

def draw_mouth():
  t.right(180)
  t.forward(30)
  t.left(90)
  t.forward(20)
  t.left(90)
  t.pencolor('white')
  t.circle(20, 180)

def draw_neck():
  t.left(90)
  t.penup()
  t.forward(20)
  t.left(90)
  t.forward(30)
  t.pendown()
  t.width(5)
  t.pencolor('black')
  t.forward(40)
  
def draw_arm(arm_number):
  if arm_number == 1:
    t.right(70)
    t.forward(60)
    t.left(60)
    t.forward(60)
    t.backward(60)
    t.right(60)
    t.backward(60)
    t.left(70)
  elif arm_number == 0:
    t.left(70)
    t.forward(60)
    t.right(60)
    t.forward(60)
    t.backward(60)
    t.left(60)
    t.backward(60)
    t.right(70)
    
def draw_leg(leg_number):
  if leg_number == 1:
    t.right(35)
    t.forward(100)
    t.backward(100)
    t.left(35)
  elif leg_number == 0:
    t.left(35)
    t.forward(100)
    t.backward(100)
    t.right(35)
    

def draw_post():
  t.penup()
  t.goto(-200, -200)
  t.pendown()
  t.fd(200)
  t.back(100)
  t.left(90)
  t.fd(400)
  t.rt(90)
  t.fd(300)
  t.rt(90)
  t.fd(80)

draw_post()
start_game()