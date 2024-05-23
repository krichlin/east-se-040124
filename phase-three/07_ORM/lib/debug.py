import ipdb

from models.owner import Owner
from models.pet import Pet


emiley = Owner(name='Emiley', age=29)
ayva = Owner(name='Ayva', age=17)

apollo = Pet(name="Apollo", age=2, breed='Dog', owner=emiley)
bailey = Pet(name="Bailey", age=11, breed='Dog', owner=emiley)
daisy = Pet(name='Daisy', breed='Fish', owner=ayva)

ipdb.set_trace()