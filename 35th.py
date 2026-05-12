class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def addpoint(self, other):
        x= self.x+other.x
        y= self.y+other.y
        return point(x,y)
    
p1= point(2,3)
p2= point(4,5)

p3=p1.addpoint(p2)

print(p3.x,p3.y)