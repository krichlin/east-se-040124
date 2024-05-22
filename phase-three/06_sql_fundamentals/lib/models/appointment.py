class Appointment:
    all = []

    def __init__(self, date, doctor_name, pet, procedure):
        self.date = date
        self.doctor_name = doctor_name
        self.pet = pet
        self.procedure = procedure

        Appointment.add_new_appointment(self)

    @classmethod
    def add_new_appointment(cls, new_appointment):
        cls.all.append(new_appointment)

    def __repr__(self):
        return f"<Appointment date={self.date} pet={self.pet}>"