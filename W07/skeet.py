 """
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random
from collections import deque
from abc import ABC
from abc import abstractmethod

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_SPEED = 10

TARGET_RADIUS = 30
TARGET_SAFE_RADIUS = 15

class Point:

    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Velocity:

    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0


class FlyingObject(): # I can add ABC if I want abstractmethod

    def __init__(self):
        self.center = Point()       # HAS-A
        self.velocity = Velocity()  # HAS-A
        self.radius = 0.0
        self.alive = True

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    #@abstractmethod  # So I can revise it in the other classes
    def draw(self, ball): # I could use abstractmethod but drawing is overlapping, so I combined to one.
        self.ball = ball
        texture = arcade.load_texture(self.ball)
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.radius*2, self.radius*2, texture)

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT): # boolean for the check_off_screen()
        if self.center.x > SCREEN_WIDTH or self.center.x <0:
            return True
        
        if self.center.y > SCREEN_HEIGHT or self.center.y < 0:
            return True

class Bullet(FlyingObject):

    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.angle = 45

    def draw(self):
        super().draw("bullet.png")
        #texture = arcade.load_texture("bullet.png")
        #arcade.draw_texture_rectangle(self.center.x, self.center.y, self.radius*2, self.radius*2, texture)
        # This was when I did Flyingobject draw() into abstractmethod

    def fire(self, angle):
        self.angle = angle #get the angle from _get_angle_degrees()
        self.center.x = 0
        self.center.y = 0
        self.velocity.dx = math.cos(math.radians(self.angle)) * BULLET_SPEED # dx, dy is changing when the mouse is moving
        self.velocity.dy = math.sin(math.radians(self.angle)) * BULLET_SPEED

class Target(FlyingObject, ABC):

    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = SCREEN_HEIGHT * 4/5
        self.is_hit = False # set as False before hit(). I'm adding for the additional condition
        self.counts = 20
    
    #def draw(self): # I can use abstracmethod, but it is too duplicating except for one. So I rather do this
        #self.ball = ball
        #texture = arcade.load_texture(self.ball)
        #arcade.draw_texture_rectangle(self.center.x, self.center.y, self.radius*2, self.radius*2, texture)

        # I didn't have to make a draw() because super() is already holding it.

    def draw(self, ball1): # always checking the target is hitten or not
        self.ball1 = ball1
        if self.alive == True and self.is_hit == False:
            super().draw(self.ball1) # I can easily draw the target. Need to draw a target
        elif self.alive == True and self.is_hit == True: # self.is_hit becomes True when hit() happens
            self.draw_pop()
            self.counts -= 1 # python is keep drawing, so I don't need any loop to countdown
            if self.counts == 0:
                self.alive = False # Then the target finally dies.

    def draw_pop(self):
        self.velocity.dx = 0 # to draw where the target got hitten
        self.velocity.dy = 0
        super().draw("pop.jpg")
        #return self.alive == False
        
    @abstractmethod # can revise in the other targets
    def hit(self):
        pass

class Standard_Target(Target):

    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.velocity.dx = random.randint(2,5)
        self.velocity.dy = random.randint(-6,2)

    def draw(self): # always checking the target is hitten or not
        super().draw("standard.png")
        #if self.alive == True and self.is_hit == False:
        #    super().draw("standard.png") # I can easily draw the target. Need to draw a target
        #elif self.alive == True and self.is_hit == True: # self.is_hit becomes True when hit() happens
        #    self.draw_pop()
        #    self.count -= 1
        #    if self.count == 0:
        #        self.alive = False # Then the target finally dies.

    def hit(self):
        self.is_hit = True
        #self.alive = False # make the target die
        return 1

class Strong_Target(Target):

    def __init__(self):
        super().__init__()
        self.count = 0 # add count for the hit()
        self.radius = TARGET_RADIUS
        self.velocity.dx = random.randint(1,1)
        self.velocity.dy = random.randint(-2,2)

    def draw(self):
        super().draw("strong.png")

    def hit(self): # duplication
        self.count += 1
        if self.count == 1 or self.count == 2: # self.count <= 2:
            self.alive = True
            self.radius //= 2
            return 1
        elif self.count == 3:
            self.is_hit = True
            #self.alive = False
            #self.count = 0
            return 3
        else:
            return 0

class Safe_Target(Target):

    def __init__(self):
        super().__init__()
        self.radius = TARGET_SAFE_RADIUS
        self.velocity.dx = random.randint(2,5)
        self.velocity.dy = random.randint(-6,2)

    def draw(self):
        super().draw("safe.png")

    def hit(self):
        self.is_hit = True
        #self.alive = False
        return -10


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle() #HAS-A
        self.score = 0

        self.bullets = [] # collect the bullets

        # TODO: Create a list for your targets (similar to the above bullets)

        self.targets = [] # collect the targets

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...

        for target in self.targets: # draw what is in the self.targets = []
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance

        for target in self.targets: # make targets move in self.targets = []
            target.advance()


    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        strongs = Strong_Target() # HAS-A of the targets and collect them into self.targets = []
        standards = Standard_Target()
        safes = Safe_Target()

        # TODO: Decide what type of target to create and append it to the list
        
        num = random.randint(0,2) # randomly chosen targets will be added in self.target = []
        if num == 0:
            self.targets.append(strongs)
        elif num == 1:
            self.targets.append(standards)
        else:
            self.targets.append(safes)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False # additionally, I have to define target's alive. But their lives are different so define
                        self.score += target.hit()  # them in hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT): # If the function is True, if will start
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y) # get from the angle making function

        bullet = Bullet()
        bullet.fire(angle) # send angle to fire()

        self.bullets.append(bullet) # bullet will be added

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)   # angle is made in this way

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()