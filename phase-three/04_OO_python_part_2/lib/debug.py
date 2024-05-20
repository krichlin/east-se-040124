import ipdb

from models import Pet, Owner

apollo = Pet(name="Apollo", age=2, breed='Dog')
daisy = Pet(name='Daisy', breed='Cat')

emiley = Owner(name='Emiley', age=29)

ipdb.set_trace()