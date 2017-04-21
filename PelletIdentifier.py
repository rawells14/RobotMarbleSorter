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

    def isMarble(self):
        color = Color(self.poll_color())
        if (color.identify_color_num() > 7):
            return False
        else:
            return True

#returns a number. will be valid index of totalMarbles if color reading was in the RANGES
#will be number greater than valid indexes of totalMarbles if color reading was in box RANGES
#will be negative 1 if trash

    def identify(self):
        color = Color(self.poll_color())
        return color.identify_color_num()


#p = PelletIdentifier(0)
#while(True):
    #print(p.poll_color())

#    c = Color(p.poll_color())
#    print(c.identify_color())
#    time.sleep(1)
