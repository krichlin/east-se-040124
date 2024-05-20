import ipdb

from models.owner import Owner
from models.pet import Pet

apollo = Pet(name="Apollo", age=2, breed='Dog')
daisy = Pet(name='Daisy', breed='Fish')

emiley = Owner(name='Emiley', age=29)
ayva = Owner(name='Ayva', age=17)

ipdb.set_trace()