class Convert:
    def seconds(self,s):
        self.s=s
    def to_convert(self):
        self.hours=self.s/3600
        self.minutes=self.s/60
        self.day=self.s/86400
    def display(self):
        print("Hours:",self.hours)
        print("Minutes:",self.minutes)
        print("Day:",self.day)
c=Convert()
c.seconds(86400) 
c.to_convert()
c.display()