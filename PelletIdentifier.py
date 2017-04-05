class PelletIdentifier:
    sensor_path = '/sys/class/lego-sensor/sensor'
    def __init__(self, sensor_number):
        self.path = sensor_path + str(sensor_number)

    def poll_color(self):
        RGB = []
        file = open(self.path + '/mode', 'w')
        file.write('RGB-RAW')
        file.close()
        for i in {'0', '1', '2'}:
            with open(self.path + '/value' + i, 'r') as file:
                RGB.append(file.readline())
            file.close()
        return RGB
