import Modules

a=Modules.Calculator()
a.greet()
print(a.add(10,20))
print(a.sub(10,20))
print(a.mul(10,20))

from Modules import Calculator

a=Calculator()

from Modules import * 

a=Calculator

from Modules import Calculator as sum

a=Calculator    