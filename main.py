import turtle

ebra = turtle.Turtle()
print(ebra.shape()) #default classic shape of th poiniter
ebra.shape("turtle") #change to turtle shape
print(ebra.color()) #color of turtle and pen
ebra.forward(100)
ebra.color("red")
ebra.forward(100)
ebra.backward(100) #backward movement
ebra.tilt(55) #angle change

#bacground color
wn=turtle.Screen()
wn.bgcolor("blue")

#tile change
wn.title('Ebrahim')

#bg pic
wn.bgpic("") #must me in same folder

