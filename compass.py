import time
import turtle

xqnum = 0.0
yqnum = 0.0
pqnum = 0.0
xcoord =0 
ycoord = 0.0
p = 0.0
strong_agree = 0.0
mid_agree = 0.0
no_agree = 0.0
conviction = strong_agree + (mid_agree/2)


def a5xanswer():
    global xcoord
    global strong_agree
    global mid_agree
    global no_agree
    inp = input("a, b, c, d or e?\n")
    if inp == "a":
        xcoord += 0.5
        strong_agree += 1
    elif inp == "b":
        xcoord += 0.25
        mid_agree += 1
    elif inp == "c":
        xcoord += 0
        no_agree +=1
    elif inp == "d":
        xcoord += -0.25
        mid_agree += 1
    elif inp == "e":
        xcoord += -0.5
        strong_agree += 1

def e5xanswer():
    global xcoord
    global strong_agree
    global mid_agree
    global no_agree
    inp = input("a, b, c, d or e?\n")
    if inp == "a":
        xcoord += -0.5
        strong_agree += 1
    elif inp == "b":
        xcoord += -0.25
        mid_agree += 1
    elif inp == "c":
        xcoord += 0
        no_agree +=1
    elif inp == "d":
        xcoord += 0.25
        mid_agree += 1
    elif inp == "e":
        xcoord += 0.5
        strong_agree += 1

def a5yanswer():
    global ycoord
    global strong_agree
    global mid_agree
    global no_agree
    inp = input("a, b, c, d or e?\n")
    if inp == "a":
        ycoord += 0.5
        strong_agree += 1
    elif inp == "b":
        ycoord += 0.25
        mid_agree += 1
    elif inp == "c":
        ycoord += 0
        no_agree +=1
    elif inp == "d":
        ycoord += -0.25
        mid_agree += 1
    elif inp == "e":
        ycoord += -0.5
        strong_agree += 1

def e5yanswer():
    global ycoord
    global strong_agree
    global mid_agree
    global no_agree
    inp = input("a, b, c, d or e?\n")
    if inp == "a":
        ycoord += -0.5
        strong_agree += 1
    elif inp == "b":
        ycoord += -0.25
        mid_agree += 1
    elif inp == "c":
        ycoord += 0
        no_agree +=1
    elif inp == "d":
        ycoord += 0.25
        mid_agree += 1
    elif inp == "e":
        ycoord += 0.5
        strong_agree += 1

def p5answer():
    global p
    global strong_agree
    global mid_agree
    global no_agree
    inp = input("a, b, c, d or e?\n")
    if inp == "a":
        p += 0.5
        strong_agree += 1
    elif inp == "b":
        p += 0.25
        mid_agree += 1
    elif inp == "c":
        p += 0
        no_agree +=1
    elif inp == "d":
        p += -0.25
        mid_agree += 1
    elif inp == "e":
        p += -0.5
        strong_agree += 1

def p0answer():
    global p
    global strong_agree
    global mid_agree
    global no_agree
    inp = input("a, b, c, d or e?\n")
    if inp == "a":
        p += -0.5
        strong_agree += 1
    elif inp == "b":
        p += -0.25
        mid_agree += 1
    elif inp == "c":
        p += 0
        no_agree +=1
    elif inp == "d":
        p += 0.25
        mid_agree += 1
    elif inp == "e":
        p += 0.5
        strong_agree += 1

start_time = time.time()

print("a=strongly agree, b=agree, c=unsure, d=disagree, e=strongly disagree")
print("\n")

print("\n")
print("This set of questions are to rate your opinion of the government.")

# Y question 1
print("\n")
print("The government has too much enough power: ")
e5yanswer()
yqnum += 1

# Y question 2
print("\n")
print("Our civil liberties are being ecessively curbed in the name of counter-terrorism: ")
e5yanswer()
yqnum += 1

# Y question 3
print("\n")
print("A person should be able to worship whomever or whatever they want: ")
e5yanswer()
yqnum += 1

# Y question 4
print("\n")
print("The government should, at most, provide emergency services and law enforcement: ")
e5yanswer()
yqnum += 1

# Y question 5
print("\n")
print("The smaller the government, the freer the people: ")
e5yanswer()
yqnum += 1

# Y question 6
print("\n")
print("In times of crisis, safety becomes more important than civil liberties: ")
a5yanswer()
yqnum += 1

# Y question 7
print("\n")
print("Victimless crimes should still be punished: ")
a5yanswer()
yqnum += 1

# Y question 8
print("\n")
print("I’d always support my country, whether it was right or wrong: ")
a5yanswer()
yqnum += 1

# Y question 9
print("\n")
print("Military action that defies international law is sometimes justified: ")
a5yanswer()
yqnum += 1

# Y question 10
print("\n")
print("There should be no restrictions on what firearms can be possesed by the public: ")
e5yanswer()
yqnum += 1



    
## following code is x axis (economic)

print("\n")
print("the next set of questions are to rate your economic stance.")


# xcoord question 1
print("\n")
print("If economic globalisation is inevitable, it should primarily serve humanity rather than the interests of trans-national corporations: ")
e5xanswer()
xqnum += 1

# xcoord question 2 
print("\n")
print("Taxation of the wealthy is a bad idea, society would be better off without it: ")
a5xanswer()
xqnum += 1

# xcoord question 3
print("\n")
print("Organisations and corporations cannot be trusted and need regulating by the government: ")
e5xanswer()
xqnum += 1

# xcoord question 4
print("\n")
print("It is 'human nature' to be greedy: ")
a5xanswer()
xqnum += 1

# xcoord question 5
print("\n")
print("Communism is an ideal economic system: ")
e5xanswer()
xqnum += 1

# xcoord question 6
print("\n")
print("The freer the market the freer the people: ")
a5xanswer()
xqnum += 1

# xcoord question 7
print("\n")
print("Economic inequality is too high in the world: ")
e5xanswer()
xqnum += 1

# xcoord question 8
print("\n")
print("All industry and the bank should be nationalised: ")
e5xanswer()
xqnum += 1

# xcoord question 9
print("\n")
print("The harder you work, the more you progress up the social ladder: ")
a5xanswer()
xqnum += 1

# xcoord question 10
print("\n")
print("Those with the ability to pay should have access to higher standards of medical care: ")
a5xanswer()
xqnum += 1


    
##following code is progressivism axis

print("\n")
print("the next set of questions are to rate progressivism socially.")
print("the lower your score, the more socially conservitive and the higher your score the more socially liberal you are.")

# p question 1
print("\n")
print("Gender is a social construct, not a natural state of affairs: ")
p0answer()
pqnum += 1

# p question 2
print("\n")
print("The current welfare system should be expanded to further combat inequality: ")
p5answer()
pqnum += 1

# p question 3
print("\n")
print("Multiculturalism is bad: ")
p0answer()
pqnum += 1

# p question 4
print("\n")
print("A government that provides for everyone is an inherently good idea: ")
p5answer()
pqnum += 1

# p question 5
print("\n")
print("One cannot be moral without religion: ")
p0answer()
pqnum += 1

# p question 6
print("\n")
print("Homosexuality is against my values: ")
p0answer()
pqnum += 1

# p question 7
print("\n")
print("Transgender individuals should not be able to adopt children: ")
p0answer()
pqnum += 1

# p question 8
print("\n")
print("Laws based on cultural values, rather than ethical ones, aren't justice: ")
p0answer()
pqnum += 1

# p question 9
print("\n")
print("The death penalty should exist for certain crimes: ")
p0answer()
pqnum += 1

# p question 10
print("\n")
print("institutional racism is still a major problem for our society: ")
p5answer()
pqnum += 1

xqtpc = 500/xqnum
yqtpc = 500/yqnum
pqtpc = 500/pqnum

time.sleep(2)

turtle.Screen()
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("PoliticalCompassResults")
wn.setup(width=500, height=500)
wn.tracer(0)

# inner sectors
libright = turtle.Turtle()
libright.speed(0)
libright.color("#c099ea")
libright.shape("square")
libright.penup()
libright.goto(125, -125)
libright.shapesize(stretch_wid = 12.5 , stretch_len = 12.5)

authright = turtle.Turtle()
authright.speed(0)
authright.color("#44aafc")
authright.shape("square")
authright.penup()
authright.goto(125, 125)
authright.shapesize(stretch_wid = 12.5 , stretch_len = 12.5)

libleft = turtle.Turtle()
libleft.speed(0)
libleft.color("#99ec9c")
libleft.shape("square")
libleft.penup()
libleft.goto(-125, -125)
libleft.shapesize(stretch_wid = 12.5 , stretch_len = 12.5)

authleft = turtle.Turtle()
authleft.speed(0)
authleft.color("#fd7574")
authleft.shape("square")
authleft.penup()
authleft.goto(-125, 125)
authleft.shapesize(stretch_wid = 12.5 , stretch_len = 12.5)

# center cross
cross1 = turtle.Turtle()
cross1.speed(0)
cross1.color("white")
cross1.shape("square")
cross1.penup()
cross1.goto(0, 0)
cross1.shapesize(stretch_wid =0.4 , stretch_len = 30)

cross2 = turtle.Turtle()
cross2.speed(0)
cross2.color("white")
cross2.shape("square")
cross2.penup()
cross2.goto(0, 0)
cross2.shapesize(stretch_wid =30 , stretch_len = 0.4)

# outer box
top_out = turtle.Turtle()
top_out.speed(0)
top_out.color("white")
top_out.shape("square")
top_out.penup()
top_out.goto(0, 250)
top_out.shapesize(stretch_wid =0.4 , stretch_len = 30)

bott_out = turtle.Turtle()
bott_out.speed(0)
bott_out.color("white")
bott_out.shape("square")
bott_out.penup()
bott_out.goto(0, -250)
bott_out.shapesize(stretch_wid =0.4 , stretch_len = 30)

left_out = turtle.Turtle()
left_out.speed(0)
left_out.color("white")
left_out.shape("square")
left_out.penup()
left_out.goto(-250, 0)
left_out.shapesize(stretch_wid =30 , stretch_len = 0.4)

right_out = turtle.Turtle()
right_out.speed(0)
right_out.color("white")
right_out.shape("square")
right_out.penup()
right_out.goto(250, 0)
right_out.shapesize(stretch_wid =30 , stretch_len = 0.4)


# lines
def hoz_ln():
    x = 0
    y = -250
    for i in range(20):
        l = turtle.Turtle()
        l.speed(0)
        l.color("white")
        l.shape("square")
        l.penup()
        l.goto(x, y)
        l.shapesize(stretch_wid =0.05 , stretch_len = 30)
        y += 25

def ver_ln():
    x = -250
    y = 0
    for i in range(20):
        l = turtle.Turtle()
        l.speed(0)
        l.color("white")
        l.shape("square")
        l.penup()
        l.goto(x, y)
        l.shapesize(stretch_wid =30 , stretch_len = 0.05)
        x += 25

hoz_ln()
ver_ln()
# ball/dot
xy_ball = turtle.Turtle()
xy_ball.speed(0)
xy_ball.color("red")
xy_ball.shape("circle")
xy_ball.penup()
xy_ball.goto(xcoord*xqtpc, ycoord*yqtpc)

p_ball = turtle.Turtle()
p_ball.speed(0)
p_ball.color("blue")
p_ball.shape("circle")
p_ball.penup()
p_ball.goto(0, p*pqtpc)

xcoord_list1 = [-5, -5, 0, -4, -3, -5, None,  -3, -1, -1, 1, -1, None, -5, -3, -2, -4, -5, -5, None, 0, 1, 3, 3, 3, 4, None, 3, 1, 0, 3, 4, 2]
ycoord_list1 = [5, 5, 5, 4, 3, 2, None, 1, 3, 1, 1, -1, None, 0, -1, -3, -3, -3, -5, None, 5, 3, 2, 3, 5, 5, None, 0, -1, -3, -2, -5, -5]

xcoord_list2 = [-4, -2, -2, -2, -1, -3, None, -1, 1, 1, 3, 1, None, -3, -1, 0, -3, -4, -2, None, 2, 3, 5, 4, 5, 5, None, 5, 3, 2, 4, 5, 5]
ycoord_list2 = [2, 4, 3, 3, 1, 0, None, -1, 1, -1, -1, -3, None, -2, -3, -5, -4, -5, -4, None, 3, 1, 0, 2, 4, 2, None, -2, -3, -5, -3, -3, -4]
# 29 items in total

statement_list = [
    "You're a Communist",
    "You're a National Communist",
    "You're a Totalitarianist",
    "You're a National Socialist",
    "You're a Stalinist",
    "You're a Socialist",
    "You're a Social Democrat",
    "You're a Authoritarianist",
    "You're a Classical Liberal/Centrist",
    "You're a Progressivist (Technologically) ",
    "You're an Activist",
    "You're a Democratic Socialist",
    "You're a Left-Libertarian",
    "You're a Syndicalist",
    "You're a Anarcho-Socialist",
    "You're an Anarcho-Communist",
    "You're an Anarcho-Collectivist",
    "You're a Nationalist",
    "You're a Conservitive",
    "You're a Ultra Capitalist",
    "You're a Traditionalist",
    "You're a Facist",
    "You're a Fundamentalist",
    "You're a Libertarian Capitalist",
    "You're a Libertarian",
    "You're a Mutualist",
    "You're a Right Anarchist",
    "You're an Anarcho Capitalist",
    "You're an Ultra Anarchist"]

for i in range(29):
    if xcoord >= xcoord_list1[i] and xcoord <= xcoord_list2[i] and ycoord <= ycoord_list1[i] and ycoord >= ycoord_list2[i]:
        print(statement_list[i])
        break

print("\n")



def sinfo():
    print(" your x, Y coordinates are:",  " ( ", xcoord, ",", ycoord, " ) \n", "your social progressivism score is:", p, "\n", "Your conviction score is", conviction, "out of 30\n")

sinfo()

print("--- %s seconds ---" % (time.time() - start_time))
sec = ((time.time() - start_time))
print("---", sec/60, "minutes ---")


# Main loop
while True:
    wn.update()
