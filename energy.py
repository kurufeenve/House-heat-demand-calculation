import matplotlib.pyplot as plt

# Specific heat capacity of parafin wax kJ/(kg*K). Different sources give from ~2.5 (https://en.wikipedia.org/wiki/Paraffin_wax) up to 3.2 (all other websites)
paraffin_wax_c = (2.14 + 2.9) / 2

# Enthalpy (heat) of fusion kJ/kg. https://en.wikipedia.org/wiki/Paraffin_wax
paraffin_wax_faze_change_H = (200 + 220) / 2

# In my opinion 350C is max safe T for paraffin wax. Boiling T is > 370C
# if there are any ignition sources nearby we should consider lower end of flash point temperature
# and max safe temperature should be lowered to 190C
# https://en.wikipedia.org/wiki/Paraffin_wax
paraffin_wax_T_max = 350

# deg. C. In my opinion this is minimum usable T for water heating
paraffin_wax_T_min = 40 

# total energy capacity for paraffin wax for the temperature defferential including fase change in the 40 to 60 C temperature interval per 1kg
paraffin_wax_total_E_capacity = (paraffin_wax_T_max - paraffin_wax_T_min) * paraffin_wax_c

house_E_usage = 50 # kWh of heat per day
efficiency = 0.8 # efficiency of converting electricity into heat
house_E_demand = house_E_usage / efficiency
koef = 1
komfort_T_outside = 15 # temperature when we use to turn on the heating
days_in_month = 30
E_demand = list()

# kWh/month by 10kW solar farm (koef = 1)
# average monthly energy production by PV cells in Kyiv city
# headed towards south, angle 38 degrees, efficiency of the system 86%, PV cells efficiency ~20%
# info taken from https://joule.net.ua/ua/articles/yak-pratsyuyut-sonyachnee-batareyi-vzimku
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
E_production = [400, 600, 950, 1050, 1350, 1200, 1200, 1200, 950, 800, 400, 300]

# average monthly temperatures for Kyiv city https://uk.wikipedia.org/wiki/%D0%9A%D0%BB%D1%96%D0%BC%D0%B0%D1%82_%D0%9A%D0%B8%D1%94%D0%B2%D0%B0
T_values = [-3.5, -3, 1.8, 9.3, 15.5, 18.5, 20.5, 19.7, 14.2, 8.4, 1.9, -2.3]
max_delta_T = komfort_T_outside - min(T_values)

for index, item in enumerate(E_production):
	E_production[index] = item * koef

for T in T_values:
	if T < 10.0:
		demand = house_E_demand * (komfort_T_outside - T) / max_delta_T * days_in_month
	else:
		demand = 0
	E_demand.append(demand)

total_E_demand = sum(E_demand)
total_E_production = sum(E_production)
str_to_show1 = 'total energy demand = ' + str(int(total_E_demand)) + ' kWh'
str_to_show2 = 'total energy production = ' + str(int(total_E_production)) + ' kWh'

plt.title('house heat energy demand')
plt.plot(months, E_production)
plt.plot(months, E_demand)
plt.text('Mar', int(max(E_demand) - max(E_demand) * 0.1), str_to_show1)
plt.text('Mar', int(max(E_demand) - max(E_demand) * 0.15), str_to_show2)
plt.xlabel('months')
plt.ylabel('kWh/month')
plt.show()
