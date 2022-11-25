import re


car_plates = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]\w?\d{3}\w{2}\d{2,3}\b')
taxi_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]\w{2,3}\d{4,5}\b')
print(private_pattern.findall(car_plates))
print(taxi_pattern.findall(car_plates))
