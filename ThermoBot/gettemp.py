from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

temp_k = sensor.get_temperature(W1ThermSensor.KELVIN)
temp_f = sensor.get_temperature(W1ThermSensor.DEGREES_F)
temp_c = sensor.get_temperature(W1ThermSensor.DEGREES_C)
temp_all = sensor.get_temperatures([W1ThermSensor.DEGREES_F, W1ThermSensor.DEGREES_C, W1ThermSensor.KELVIN])

print temp_all
