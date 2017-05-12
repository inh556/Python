class Car:
    speed =0
    def drive(self, distance):
        time = distance /self.speed
        print '%.2f' % time
car1 =Car()
car1.speed = 60
car1.drive(100.0)

car2 = Car()
car2.speed =150.0
car2.drive(100.0)
