from parentClasses import Vehicle,Freezer

class FreezeTruck(Vehicle,Freezer):
    def display(self):
        print(f'{issubclass(FreezeTruck,Freezer)} is a freezer')
        print(f'{issubclass(FreezeTruck,Vehicle)} is a vehicle')

        # super(Freezer,self).display()
        # super(Vehicle,self).display()
        Freezer.display(self)
        Vehicle.display(self)


t = FreezeTruck()
t.drive(50)
t.freeze(2)

print('-'*20)
t.display()