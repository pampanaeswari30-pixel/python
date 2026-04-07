class Convert:
    def read_inches(self,inches):
        self.inches=inches
    def to_feets(self):
        self.feets=self.inches/12
    def display(self):
        print("Inches:",self.inches)
        print("Feets:",self.feets)
c=Convert()
c.read_inches(96)
c.to_feets()
c.display()