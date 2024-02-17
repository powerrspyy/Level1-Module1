
def setup():
    # 1. Use the size function to set the size of your sketch
    size(844,600)
    global back
    global car_left
    global car_right
    global frog
    global frog_x
    global frog_y
    global car_3
    global car_4
    global car_5
    global game_over

    frog_x = 300
    frog_y = 530
    back = loadImage("froggerBackground.png")
    car_left = Car(300,435, 160, -1)
    car_right = Car(300,360, 160, 2)
    car_3 = Car(300,210, 160, -3)
    car_4 = Car(300,135,160,4)
    car_5 = Car(300, 285, 160, -5)
    frog = loadImage("frog.png")
    frog.resize(75,75)
    game_over = loadImage("download.png")
    game_over.resize(844,600)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    
def draw():
    global frog_x,frog_y
    global car_left,car_right
    global game_over
    background(back)
    image (frog,frog_x,frog_y)
    # 4. Use the background function to draw the background
    car_list = [car_right,car_left, car_3, car_4, car_5]
    for car in car_list:
        car.update()
        car.draw()
    for car in car_list:
        inter = intersects(car)
        if inter == True:
            frog_x = 300
            frog_y = 530
    # if frog.y < 100:
    #     image(game_over, 0,0)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    # global frog_x, frog_y
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    
    # 9. Create more car objects of different lengths, speed, and size
def intersects(car):
    if frog_y > car.y and frog_y < car.y + 50 and frog_x + 50 > car.x and frog_x < car.x + car.length:
        return True
    else:
        return False
    
def keyPressed():
    global frog_x,frog_y
    if key == CODED:
        if keyCode == UP:
            frog_y -= 77
        elif keyCode == LEFT:
            frog_x -= 77
        elif keyCode == RIGHT:
            frog_x += 77
        elif keyCode == DOWN:
            frog_y += 77
class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
