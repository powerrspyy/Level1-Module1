"""
Create a single player Pong game
"""
from Ball import Ball
from Paddle import Paddle
global started
started = False
global ball
global paddle
global score
global speed

def setup():
    
    global ball
    global paddle
    global score
    global speed
    score = 0
    speed = 0
    # 1. Set the size of your window to at least width = 800, height = 600
    
    size(800,600)
    
    # 2. Make a global ball variable, for example:
    # 3. Initialize your ball variable to a new Ball(), for example:
    ball = Ball()
    
    # 4. Make a global paddle variable.
    # 5. Initialize your paddle variable to a new Paddle() for example:
    paddle = Paddle(x=350, y = 550)
    
    
def draw():
    global ball, paddle, score, speed
    if not started:
        textSize(32)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        return
    
    # 6. Use the background() function to set the background color.
    #    background(0) will set a classic black background
    background(0)
    # 7. Call the ball object's update() and draw() methods.
    #    Do you see the ball moving on the screen?
    ball.update()
    ball.draw()
    # 8. Call the paddle object's update() and draw() methods.
    #    Do you see the paddle on the screen?
    paddle.update()
    paddle.draw()
    # 11. Finish the code in keyPressed() and keyReleased() first!
    #     Call the ball object's collision() method and pass the
    #     paddle object as an input variable.
    #     Does the ball bounce off the paddel?
    ball.collision(paddle)
    # 12. End the game when the ball goes below the bottom of the screen.
    #     You can use noLoop() to freeze the game and text() to print text
    #     on the screen.
    if ball.y > 600:
        noLoop()
        textSize(32)
        fill(255,255,255)
        text("Game Over", width/3,200)
        final = "Score: " + str(score)
        text(final, width/3, 400)
    if speed < ball.speed:
        score += 1
        pass
    speed = ball.speed
    # 13. Figure out how to add a score to the game so every bounce off
    #     the paddle increases the player socre

    # *EXTRA*
    # Can you figure out how to make a 2 player pong game with paddles on
    # the left and right on the screen?
    
    pass

# 9. Change paddle.x_speed when the LEFT or RIGHT arrow keys are pressed.
#    Does the paddle move?
def keyPressed():
    if key == 's':
        global started
        started = True 
    elif key == CODED:
        if keyCode == LEFT:
            paddle.x_speed = -10
        if keyCode == RIGHT:
            paddle.x_speed = 10


# 10. Set paddle.x_speed to 0 when the LEFT or RIGHT arrow keys are released.
#     Does the paddle stop when the keys are released?
def keyReleased():
    global paddle
    if key == CODED:
        paddle.x_speed = 0
