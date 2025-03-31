import fastf1 as f1
import matplotlib.pyplot as plt
import fastf1.plotting as f1plot

f1plot._plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

session1 = f1.get_session(2025, 'Australia', 'Q')
session1.load(telemetry=True, laps=True, weather=True)
session2 = f1.get_session(2025, 'China', 'Q')
session2.load(telemetry=True, laps=True, weather=True)

fastest_tsunoda1 = session1.laps.pick_drivers('TSU').pick_fastest()
fastest_lawson1 = session1.laps.pick_drivers('LAW').pick_fastest()
tsu_car_data1 = fastest_tsunoda1.get_car_data()
law_car_data1 = fastest_lawson1.get_car_data()
print('[Australia]:')
print('Tsunoda fastest: ', str(fastest_tsunoda1['LapTime'])[10::])
print('Lawson fastest: ', str(fastest_lawson1['LapTime'])[10::])
tt1 = tsu_car_data1['Time']
vt1 = tsu_car_data1['Speed']
tl1 = law_car_data1['Time']
vl1 = law_car_data1['Speed']

fastest_tsunoda2 = session2.laps.pick_drivers('TSU').pick_fastest()
fastest_lawson2 = session2.laps.pick_drivers('LAW').pick_fastest()
tsu_car_data2 = fastest_tsunoda2.get_car_data()
law_car_data2 = fastest_lawson2.get_car_data()
print('[China]:')
print('Tsunoda fastest: ', str(fastest_tsunoda2['LapTime'])[10::])
print('Lawson fastest: ', str(fastest_lawson2['LapTime'])[10::])
tt2 = tsu_car_data2['Time']
vt2 = tsu_car_data2['Speed']
tl2 = law_car_data2['Time']
vl2 = law_car_data2['Speed']

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(tt1, vt1, label='Tsunoda', color='orange')
plt.plot(tl1, vl1, label='Lawson', color='green')
plt.xlabel('Time')
plt.ylabel('Speed [Km/h]')
plt.title('[Australia] TSU vs LAW')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(tt2, vt2, label='Tsunoda', color='orange')
plt.plot(tl2, vl2, label='Lawson', color='green')
plt.xlabel('Time')
plt.ylabel('Speed [Km/h]')
plt.title('[China] TSU vs LAW')
plt.legend()
plt.show()






