class Things:
    pass

class Inanimate (Things):
    pass

class Animate (Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals (Animate):
    def breathe (self):
        print ('Hi is breathing')
    def move (self):
        print ('He is moving')
    def eat_food (self):
        print ('He is eating')

class Mammals (Animals):
    def feed_young_with_milk (self):
        print ('He is feeding young with milk')

class Girafes (Mammals):
    def find_food (self):
        self.move()
        print ('I found eat')
        self.eat_food()
    def eat_leaves_from_trees (self):
        self.eat_food()
    def dance_a_jig (self):
        self.move()
        self.move()
        self.move()
        self.move()
#    def __init__ (self, sports):
#        self.giraffe_sport = sports

    def left_foot_forward (self):
        print ('Left foot forward')
    def left_foot_back (self):
        print ('Left foot back')
    def right_foot_forward (self):
        print ('Right foot forward')
    def right_foot_back (self):
        print ('Right foot back')

    def dance (self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.right_foot_forward()


reginald = Animals()
harold = Girafes()

harold.dance()
