from models.appointment import Appointment

class Procedure:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Procedure name={self.name}>'

    def appointments(self):
        return [appointment for appointment in Appointment.all if appointment.procedure == self]