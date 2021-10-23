#importing parent class
from animal import Animal

def catFunc():
    catOne  =   Animal('Phebe',2,'female')
    catTwo  =   Animal('tini',4,'male')

    catOne.description()
    catTwo.description()

if __name__ == '__main__':
    x = Animal('ok')
    x.description() 
    catFunc()