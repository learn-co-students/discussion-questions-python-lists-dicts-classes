import ipdb

from lib.review_question_car_class import Car

volvo_lightning = Car(make="Volvo", model="Lightning")
Car.all
volvo_lightning.make
volvo_lightning.model
Car.brake()
volvo_lightning.drive()

ipdb.set_trace()
