from carfactory import CarFactory
from datetime import datetime

today = datetime.today().date()
dt_ultima_revisao = datetime.strptime('2021-10-09', '%Y-%m-%d').date()
calliope_car = CarFactory().create_calliope(current_date=today,
                                            last_service_date=dt_ultima_revisao,
                                            current_mileage=50200,
                                            last_service_mileage=45000)

x = calliope_car.needs_service()
print(x)
