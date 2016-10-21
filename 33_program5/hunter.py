# A Hunter is both a Mobile_Simulton and a Pulsator: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    hunting = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        w,h = self.get_dimension()
        Mobile_Simulton.__init__(self,x,y,w,h,0,5)
        self.randomize_angle()
        
    def update(self,model):
        eaten = Pulsator.update(self,model)
        on_the_hunt = model.find(lambda x: isinstance(x,Prey) and self.distance(x.get_location()) <= Hunter.hunting)
        if on_the_hunt:
            unlucky_one = min([(self.distance(x.get_location()),x) for x in on_the_hunt])
            huntX, huntY = self.get_location()
            preyX, preyY = unlucky_one[1].get_location()
            self.set_angle(atan2(preyY-huntY,preyX-huntX))
        self.move()
        return eaten
        
