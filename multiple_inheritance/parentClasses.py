#############################
class Vehicle:
    speed = 0 
    
    def drive(self,speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed =0 
        print('stopped')

    def display(self):
        print(f'he is driving at {self.speed} speed')


class Freezer:
    temp = 0
    def freeze(self,temp):
        self.temp = temp
        print('freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')


