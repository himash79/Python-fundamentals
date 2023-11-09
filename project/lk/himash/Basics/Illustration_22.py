# Inheritance :
# Technically it's can be able to access parent class properties.
# Able to do same as other language.

print('Regular Inheritance ====================================')
class Mobile01:
    def call(self):
        print('Able to Call')

class Mobile02(Mobile01):
    def bluetooth(self):
        print('Able to Bluetooth')

mobile = Mobile02()
mobile.bluetooth()
mobile.call()

print('Multiple Inheritance ====================================')
class Mobile01:
    def call(self):
        print('Able to Call')

class Mobile02:
    def bluetooth(self):
        print('Able to Bluetooth')

class Mobile03(Mobile02, Mobile01):
    def video(self):
        print('Able to Video')

mobile = Mobile03()
mobile.bluetooth()
mobile.call()
mobile.video()

print('Multi Level Inheritance ====================================')
class Mobile01:
    def call(self):
        print('Able to Call')

class Mobile02(Mobile01):
    def bluetooth(self):
        print('Able to Bluetooth')

class Mobile03(Mobile02):
    def video(self):
        print('Able to Video')

mobile = Mobile03()
mobile.bluetooth()
mobile.call()
mobile.video()