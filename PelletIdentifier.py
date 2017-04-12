import time
from Color import Color
class PelletIdentifier:

    def __init__(self, sensor_number):
        self.sensor_path = '/sys/class/lego-sensor/sensor'
        self.path = self.sensor_path + str(sensor_number)

    def poll_color(self):
        RGB = []
        file = open(self.path + '/mode', 'w')
        file.write('RGB-RAW')
        file.close()
        for i in {'0', '1', '2'}:
            with open(self.path + '/value' + i, 'r') as file:
                RGB.append(int(file.readline().replace('\n', '')))
            file.close()
        return RGB

#p = PelletIdentifier(0)
#while(True):
    #print(p.poll_color())

#    c = Color(p.poll_color())
#    print(c.identify_color())
#    time.sleep(1)
