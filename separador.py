segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(segundos)

dias = segundos // 86400
sobra_dias = segundos % 86400

horas = sobra_dias // 3600
sobra_horas = sobra_dias % 3600

minutos = sobra_horas // 60
seg = sobra_horas % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", seg, "segundos.")