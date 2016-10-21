#The Freezer is a Prey that shares the movement 
#    pattern and size of a ball. Unlike the ball, 
#    the Freezer moves at a speed of 2. When the 
#    Freezer is within 50 units of a Hunter, the 
#    Freezer will "freeze" the Hunter, preventing 
#    it from moving for the duration of the simulation.
#    The Freezer is represented by the cyan color.

from prey import Prey
import model
from hunter import Hunter
from pulsator import Pulsator

class Freezer(Prey):
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,2)
        self.randomize_angle()
        self._color = 'cyan'
        
    def update(self,model):
        freeze = model.find(lambda x:isinstance(x,Hunter) and self.distance(x.get_location()) <= 50)
        if freeze:
            for unlucky_hunter in freeze:
                hunterX,hunterY = unlucky_hunter.get_location()
                hunter_w, hunter_h = unlucky_hunter.get_dimension()
                frozen = Pulsator(hunterX,hunterY)
                frozen.set_dimension(hunter_w,hunter_h)
                model.remove(unlucky_hunter)
                model.add(frozen)
        self.move()
        self.wall_bounce()
            
        
    def display(self,canvas):
        canvas.create_oval(self._x-Freezer.radius      , self._y-Freezer.radius,
                                self._x+Freezer.radius, self._y+Freezer.radius,
                                fill=self._color)
        