# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        self._color = 'black'
        
    def display(self,canvas):
        w,h = self.get_dimension()
        canvas.create_oval(self._x-w/2     , self._y-h/2,
                                self._x+w/2, self._y+h/2,
                                fill=self._color)
    
    def update(self,model):
        eaten = model.find(lambda n:self.contains(n.get_location()) and isinstance(n,Prey))
        for stuff in eaten:
            model.remove(stuff)
        return eaten

    def contains(self,xy):
        return self.distance(xy) <= self.get_dimension()[0]/2