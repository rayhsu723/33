import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Freezer


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
sim_type = None
simultons = set()


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons
    running     = False
    cycle_count = 0
    simultons = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    if running == False:
        start()
        update_all()
        stop()
    if running == True:
        update_all()
        stop()



#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global sim_type
    sim_type = kind
#     print(sim_type)


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if sim_type == None:
        print('Select a button first in order to create desired object')
    elif sim_type == 'Remove':
        for x in find(lambda n:n.contains((x,y))):
            simultons.discard(x)
    elif sim_type == 'Special':
        simultons.add(Freezer(x,y))
    else:
        simultons.add(eval(sim_type + '(' + str(x) + ',' + str(y) + ')'))

#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.discard(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return {stuff for stuff in simultons if p(stuff)}


#call update for every simulton in the simulation
def update_all():
    global running
    if running:
        global cycle_count,world
        cycle_count += 1
        original_sim = set(simultons)
        for stuff in original_sim:
            if stuff in simultons:
                stuff.update(sys.modules[__name__])
                


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    for stuff in simultons:
        stuff.display(controller.the_canvas)
        
    controller.the_progress.config(text=str(len(simultons))+" simultons/"+str(cycle_count)+" cycles")

