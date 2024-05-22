import ipdb

from models.owner import Owner
from models.pet import Pet
from models.appointment import Appointment
from models.procedure import Procedure

emiley = Owner(name='Emiley', age=29)
ayva = Owner(name='Ayva', age=17)

apollo = Pet(name="Apollo", age=2, breed='Dog', owner=emiley)
bailey = Pet(name="Bailey", age=11, breed='Dog', owner=emiley)
daisy = Pet(name='Daisy', breed='Fish', owner=ayva)

pr1 = Procedure(name='Allergy relief')
pr2 = Procedure(name='Annual check')
pr3 = Procedure(name='Ears relief')

a1 = Appointment(date='May 20, 2024', doctor_name='Dr. Ross', pet=bailey, procedure=pr1)
a2 = Appointment(date='May 20, 2024', doctor_name='Dr. Bailey', pet=apollo, procedure=pr2)
a3 = Appointment(date='April 20, 2024', doctor_name='Dr. Grey', pet=apollo, procedure=pr3)
a4 = Appointment(date='May 17, 2023', doctor_name='Dr. Bailey', pet=daisy, procedure=pr2)
a5 = Appointment(date='May 15, 2022', doctor_name='Dr. House', pet=bailey, procedure=pr1)

ipdb.set_trace()