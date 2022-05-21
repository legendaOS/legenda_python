class mashine:
    def __init__(self):
        self.v = 2
        self.km = 0
        self.c = 2
        
    def go(self, hours = 1):
        self.km += self.v * hours
        
    def info(self):
        print(self.km, self.c)
        
    def avary(self):
        self.c -= 1

s = mashine()
s.go()
s.avary()
s.go(4)
s.info()



