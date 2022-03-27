"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others

This program implements the asteroids game.
"""
import arcade
from abc import ABC
from abc import abstractmethod
import random
import math

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 30

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 20

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 10

class Point:

    def __init__(self):
        self.x = 0.0 # the initial center of the object
        self.y = 0.0

class Velocity:

    def __init__(self):
        self.dx = 0.0 # the initial speed of the object
        self.dy = 0.0

class FlyingObject(): # basic class for the moving objects on the screen

    def __init__(self):
        self.center = Point() # HAS-A
        self.velocity = Velocity() #  HAS-A
        self.radius = 0.0
        self.alive = True
        self.texture = "" # to draw
        self.degree = 0.0
        self.angle = 0.0

    def advance(self): # makes an boject move
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def wrap(self, SCREEN_WIDTH, SCREEN_HEIGHT): # Checking the object's center going out the screen
        if (self.center.x < 0) or (self.center.x > SCREEN_WIDTH):
            return True
        
        if (self.center.y < 0) or (self.center.y > SCREEN_HEIGHT):
            return True

    def draw(self): # draw an object
        texture = arcade.load_texture(self.texture)
        self.degree += self.angle
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.radius*2, self.radius*2, texture, self.degree)

class Astroid(FlyingObject, ABC): # basic and derived class for the astroids

    def __init__(self):
        super().__init__()
        self.center.x = random.choice(range(BIG_ROCK_RADIUS, SCREEN_WIDTH - BIG_ROCK_RADIUS))
        self.center.y = random.choice([BIG_ROCK_RADIUS, SCREEN_HEIGHT - BIG_ROCK_RADIUS])
        self.velocity.dx = random.choice([-BIG_ROCK_SPEED, BIG_ROCK_SPEED])
        self.velocity.dy = random.choice([-BIG_ROCK_SPEED, BIG_ROCK_SPEED])
        
    @abstractmethod
    def split(self): # use the same name, same parameter, same return
        pass

class LargeAst(Astroid):

    def __init__(self):
        super().__init__()
        self.texture = "big.png"
        self.radius = BIG_ROCK_RADIUS
        self.angle = BIG_ROCK_SPIN
        
    def split(self): # splits the Large astroids center, and ramdomly added the velocity
        return [MidAst(self.center.x, self.center.y, self.velocity.dx + math.cos(math.radians(self.degree*random.uniform(0,359))) * 2, self.velocity.dy + math.sin(math.radians(self.degree*random.uniform(0,359))) * 2), MidAst(self.center.x, self.center.y, self.velocity.dx - math.cos(math.radians(self.degree*random.uniform(0,359))) * 2, self.velocity.dy - math.sin(math.radians(self.degree*random.uniform(0,359))) * 2), SmallAst(self.center.x, self.center.y, self.velocity.dx * 3, self.velocity.dy * 3)]

class MidAst(Astroid):

    def __init__(self, center_x, center_y, vel_dx, vel_dy):
        super().__init__()
        self.center.x = center_x
        self.center.y = center_y
        self.velocity.dx = vel_dx
        self.velocity.dy = vel_dy
        self.texture = "medium.png"
        self.radius = MEDIUM_ROCK_RADIUS
        self.angle = MEDIUM_ROCK_SPIN

    def split(self):  # splits the Mid astroids center, and ramdomly added the velocity
        return [SmallAst(self.center.x, self.center.y, self.velocity.dx + math.cos(math.radians(self.degree*random.uniform(0,359))) + 2, self.velocity.dy + math.sin(math.radians(self.degree*random.uniform(0,359))) + 2), SmallAst(self.center.x, self.center.y, self.velocity.dx - math.cos(math.radians(self.degree*random.uniform(0,359))) - 2, self.velocity.dy - math.sin(math.radians(self.degree*random.uniform(0,359))) - 2)]

class SmallAst(Astroid):

    def __init__(self, center_x, center_y, vel_dx, vel_dy):
        super().__init__()
        self.center.x = center_x
        self.center.y = center_y
        self.velocity.dx = vel_dx
        self.velocity.dy = vel_dy
        self.texture = "small.png"
        self.radius = SMALL_ROCK_RADIUS
        self.angle = SMALL_ROCK_SPIN

    def split(self): # return the empty list
        return []

class ShipVelocity(): # velocity for the ship

    def __init__(self):
        self._dx = 0.0
        self._dy = 0.0
 
    @property                  # limiting the ships velocity
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, dx):
        if dx > 15:
            self._dx = 15
        elif dx < -15:
            self._dx = -15
        else:                 # if it is not above both
            self._dx = dx

    @property
    def dy(self):
        return self._dy
    
    @dy.setter
    def dy(self, dy):
        if dy > 15:
            self._dy = 15
        elif dy < -15:
            self._dy = -15
        else:
            self._dy = dy

class Ship(FlyingObject):

    def __init__(self):
        super().__init__()
        self.texture = "ship.png"
        self.center.x = SCREEN_WIDTH // 2
        self.center.y = SCREEN_WIDTH // 2
        self.radius = SHIP_RADIUS
        self.velocity = ShipVelocity() # HAS-A velocity
        self.count = 30
        self.pop_alive = True

    def draw(self): # draw a ship 90 degrees turned in the beginning.
        texture = arcade.load_texture(self.texture)
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.radius*2, self.radius*2, texture, self.degree - 90)

    def draw_pop(self): # draw pop where the ship dies, so velocity becomes zero and stays a while
        self.velocity.dx = 0
        self.velocity.dy = 0
        if self.pop_alive:
            self.count -= 1
            texture = arcade.load_texture("pop.jpg")
            arcade.draw_texture_rectangle(self.center.x, self.center.y, self.radius*2, self.radius*2,texture)
            if self.count == 0:
                self.pop_alive = False

    def move_thurst(self): # add speed where the ship head is pointing. 
        self.velocity.dx += math.cos(math.radians(self.degree)) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.sin(math.radians(self.degree)) * SHIP_THRUST_AMOUNT

    def move_dethurst(self): # subtract speed where the ship head is pointing
        self.velocity.dx -= math.cos(math.radians(self.degree)) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.sin(math.radians(self.degree)) * SHIP_THRUST_AMOUNT

    def turn_left(self): # changes the degree
        self.degree += (SHIP_TURN_AMOUNT + 2)

    def turn_right(self): # changes the degree
        self.degree -= (SHIP_TURN_AMOUNT + 2)
        
class Bullet(FlyingObject):

    def __init__(self):
        super().__init__()
        self.texture = "laser.png"
        self.center.x = SCREEN_WIDTH // 2
        self.center.y = SCREEN_WIDTH // 2
        self.counts = BULLET_LIFE
        self.radius = BULLET_RADIUS
        self.velocity.dx = BULLET_SPEED
        self.velocity.dy = BULLET_SPEED
        #self.counts_three = 80

    def draw(self): # draw a bullet for self.count much long
        if self.alive == True:
            self.counts -= 1
            texture = arcade.load_texture(self.texture)
            arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.degree)
            if self.counts == 0:
                self.alive = False

class Item(FlyingObject):

    def __init__(self):
        super().__init__()
        self.texture = "3B.jpg"
        self.center.x = random.uniform(5, SCREEN_WIDTH-5)
        self.center.y = random.uniform(5, SCREEN_WIDTH-5)
        self.radius = 30
        self.velocity.dx = random.uniform(2, 5)
        self.velocity.dy = random.uniform(-3, 3)

    def draw(self): # draw a bullet for self.count much long
        texture = arcade.load_texture(self.texture)
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.radius * 2, self.radius * 2, texture, self.degree)

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set() # a set that doesn't record the repeating elements

        # TODO: declare anything here you need the game class to track

        #self.ship = Ship() # HAS-A

        #self.item = Item()

        #self.bullets = []

        #self.astroids = []

        #self.create_ast()

        #self.count = 6 # for the bullet

        #self.counts = 200 # for item

        self.setup()

    def setup(self): # restart everything

        self.ship = Ship() # HAS-A

        self.item = Item()

        self.bullets = []

        self.astroids = []

        self.create_ast()

        self.count = 6 # for the bullet pixel

        self.counts = 200 # for item


    def on_draw(self): # draw infinitely
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        if self.ship.alive:
            self.ship.draw() # keep draw the ship until it dies

        if not self.ship.alive: # when the ship dies, draw pop
            self.ship.draw_pop()

        if self.item.alive: # item appears a little later
            self.counts -= 1
            if self.counts < 0:
                self.item.draw()

        # if self.item.alive:
        for bullet in self.bullets: # draw bullets when the ship is alive 
            if self.ship.alive:
                bullet.draw()

        for astroid in self.astroids: # draw astroids that are made
            astroid.draw()

    def create_ast(self): # create the initial numbers of astroids       
        # large = LargeAst(): the same pointer 
        for i in range(INITIAL_ROCK_COUNT):
            large = LargeAst() # making different pointers
            self.astroids.append(large)
        # print(self.astroids)

    def update(self, delta_time): # keep checking what is happening like a while loop
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        self.ship.advance()
        # TODO: Tell everything to advance or move forward one step in time
        for bullet in self.bullets:
            bullet.advance()

        for astroid in self.astroids:
            astroid.advance()

        self.item.advance()

        # TODO: Check for collisions
        self.check_collisions()

        self.check_off_screen()

    def check_collisions(self): # check collisions
        
        #new_astroids = [] # for the astroids split function list
        for bullet in self.bullets:
            for astroid in self.astroids:
                if bullet.alive and astroid.alive:
                    too_close = bullet.radius + astroid.radius
                    if (abs(bullet.center.x - astroid.center.x) < too_close) and (abs(bullet.center.y - astroid.center.y) < too_close):
                        bullet.alive = False
                        astroid.alive = False
                        self.astroids += astroid.split() # because self.astroid is outside the loop, it doesn't run infinitely
                        #new_astroids += astroid.split() when astroid dies, call split() and add to the outside the for loop list so I can add
                        #astroid.split()
                
        for astroid in self.astroids:        
            if astroid.alive and self.ship.alive:
                too_close_ship = self.ship.radius + astroid.radius
                if (abs(self.ship.center.x - astroid.center.x) < too_close_ship) and (abs(self.ship.center.y - astroid.center.y) < too_close_ship):
                    self.ship.alive = False 
                    astroid.alive = False
                    self.astroids += astroid.split()
        
        if self.item.alive and self.ship.alive:
            too_close = self.item.radius + self.ship.radius
            if (abs(self.item.center.x - self.ship.center.x) < too_close) and (abs(self.item.center.y - self.ship.center.y) < too_close):
                self.item.alive = False
                self.ship.radius = 40

        self.cleanup_zombies()
        #self.astroids += new_astroids

    def cleanup_zombies(self): # removes bullet and astroids
        
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for astroid in self.astroids:
            if not astroid.alive:
                self.astroids.remove(astroid)

    def check_off_screen(self): # bullets, astroids, ship can wrap the screen
        for bullet in self.bullets:
            if bullet.wrap(SCREEN_WIDTH, SCREEN_HEIGHT):
                if bullet.center.x < 0:
                    bullet.center.x = SCREEN_WIDTH
                elif bullet.center.x > SCREEN_WIDTH:
                    bullet.center.x = 0
                if bullet.center.y < 0:
                    bullet.center.y = SCREEN_HEIGHT
                elif bullet.center.y > SCREEN_HEIGHT:
                    bullet.center.y = 0
        
        for astroid in self.astroids:
            if astroid.wrap(SCREEN_WIDTH, SCREEN_HEIGHT):
                if astroid.center.x < 0:
                    astroid.center.x = SCREEN_WIDTH
                elif astroid.center.x > SCREEN_WIDTH:
                    astroid.center.x = 0
                if astroid.center.y < 0:
                    astroid.center.y = SCREEN_HEIGHT
                elif astroid.center.y > SCREEN_HEIGHT:
                    astroid.center.y = 0
        
        if self.ship.wrap(SCREEN_WIDTH, SCREEN_HEIGHT):
            if self.ship.center.x < 0:
                self.ship.center.x = SCREEN_WIDTH
            elif self.ship.center.x > SCREEN_WIDTH:
                self.ship.center.x = 0
            if self.ship.center.y < 0:
                self.ship.center.y = SCREEN_HEIGHT
            elif self.ship.center.y > SCREEN_HEIGHT:
                self.ship.center.y = 0

        if self.item.wrap(SCREEN_WIDTH, SCREEN_HEIGHT):
            if self.item.center.x < 0:
                self.item.center.x = SCREEN_WIDTH
            elif self.item.center.x > SCREEN_WIDTH:
                self.item.center.x = 0
            if self.item.center.y < 0:
                self.item.center.y = SCREEN_HEIGHT
            elif self.item.center.y > SCREEN_HEIGHT:
                self.item.center.y = 0

    def check_keys(self): # key becomes true it will do what in 'if'
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            self.ship.move_thurst()

        if arcade.key.DOWN in self.held_keys:
            self.ship.move_dethurst()

        if arcade.key.R in self.held_keys:
            self.setup()

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys: # everything is same with ship
            bullet = Bullet()
            bullet_1 = Bullet() # to make bullet individually
            bullet_2 = Bullet()
            if self.item.alive:
                bullet.center.x = self.ship.center.x
                bullet.center.y = self.ship.center.y
                bullet.velocity.dx = self.ship.velocity.dx + math.cos(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet.velocity.dy = self.ship.velocity.dy + math.sin(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet.degree = self.ship.degree

                if len(self.bullets) == 0:       # Make the bullet not overlap
                    self.bullets.append(bullet)
                if len(self.bullets) > 0:        # Keep getting called by update()
                    self.count -= 1
                    if self.count == 0:
                        self.bullets.append(bullet)
                        self.count = 6           # reset the count. count should place outside of the loop(update()) --> place in init()

            if not self.item.alive:
                bullet.counts = 80 # extend the bullet lives
                bullet_1.counts = 80
                bullet_2.counts = 80
                bullet.center.x = self.ship.center.x
                bullet.center.y = self.ship.center.y
                bullet.velocity.dx = self.ship.velocity.dx + math.cos(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet.velocity.dy = self.ship.velocity.dy + math.sin(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet.degree = self.ship.degree

                bullet_1.center.x = self.ship.center.x + 25 * math.cos(math.radians(self.ship.degree + 90)) # the left bullet
                bullet_1.center.y = self.ship.center.y + 25 * math.sin(math.radians(self.ship.degree + 90))
                bullet_1.velocity.dx = self.ship.velocity.dx + math.cos(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet_1.velocity.dy = self.ship.velocity.dy + math.sin(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet_1.degree = self.ship.degree

                bullet_2.center.x = self.ship.center.x - 25 * math.cos(math.radians(self.ship.degree + 90)) # the right bullet 
                bullet_2.center.y = self.ship.center.y - 25 * math.sin(math.radians(self.ship.degree + 90))
                bullet_2.velocity.dx = self.ship.velocity.dx + math.cos(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet_2.velocity.dy = self.ship.velocity.dy + math.sin(math.radians(self.ship.degree)) * BULLET_SPEED
                bullet_2.degree = self.ship.degree

                if len(self.bullets) == 0: 
                    self.bullets.extend([bullet, bullet_1, bullet_2]) # use extend for a list append
                if len(self.bullets) > 0: 
                    self.count -= 1
                    if self.count == 0:
                        self.bullets.extend([bullet, bullet_1, bullet_2])
                        self.count = 6 
            #if len(self.bullets) == 0:
            #    self.bullets.append(bullet)
            #elif len(self.bullets) > 0:
            #    for bullet_1 in self.bullets:
            #        close_bullet = bullet_1.radius + self.ship.radius
            #        bullet_ship_dis = ((bullet_1.center.x - self.ship.center.x)**2 + (bullet_1.center.y - self.ship.center.y)**2)**0.5
            #        if bullet_ship_dis > close_bullet:
            #if len(self.bullets) == 0:       # Make the bullet not overlap
            #    self.bullets.append(bullet)
            #if len(self.bullets) > 0:        # Keep getting called by update()
            #    self.count -= 1
            #    if self.count == 0:
            #        self.bullets.append(bullet)
            #        self.count = 6           # reset the count. count should place outside of the loop(update()) --> place in init()


    def on_key_press(self, key: int, modifiers: int): # adding pressed keys in the set()
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        # if self.ship.alive:
        self.held_keys.add(key)

            #if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
               
                #bullet = Bullet()
                #self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int): # removing released keys in the set()
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()