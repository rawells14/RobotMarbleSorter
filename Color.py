class Color(object):
    default = 'box'

    #OLD ORDER
    #color_strings = ['Large Red', 'Small Red', 'Large White', 'Small White',
    #                 'HDPE', 'Large Blue', 'Small Blue', 'Large Green', 'Small Green',
    #                 'Large Yellow', 'Small Yellow', 'Steel']

    #OLD RANGES
    #color_ranges = [[[111, 160],[60, 75],[39, 47]],
    #                [[87, 110], [62, 68], [39, 47]],
    #                [[170, 255], [185, 255], [90, 120]],
    #                [[115, 140], [115, 140], [53, 60]],
    #                [[98, 108], [90, 110], [50, 60]],
    #                [[85, 94], [80, 95], [60, 75]],
    #                [[75, 84], [60, 75], [42, 55]],
    #                [[75, 110], [76, 130], [40, 55]],
    #                [[75, 89], [80, 90], [40, 55]],
    #                [[150, 195], [115, 130], [40, 50]],
    #                [[105, 135], [90, 120], [40, 50]],
    #                [[90, 95], [70, 85], [43, 47]]]

    #NEW order
    color_strings = ['Steel', 'HDPE', 'Small White', 'Large White', 'Small Blue', 'Large Blue', 'Small Red', 'Large Red',
                    'Small Green', 'Large Green', 'Large Green 2' 'Small Yellow', 'Large Yellow']

    #NEW RANGES
    color_ranges = [[[75,92],[83, 100], [42, 52]],
                    [[135, 145], [139, 148], [82, 95]],
                    [[235, 265], [240, 265], [145, 160]],
                    [[225, 265], [230, 265], [165, 190]],
                    [[45, 80],[50,70],[40,83]],
                    [[65, 90], [60,80], [84, 106]],
                    [[40, 50], [115, 160], [25, 29]],
                    [[40, 50], [110, 160], [30, 35]],
                    [[75,95], [60, 70], [30, 42]],
                    [[55, 65], [55, 60], [30, 35]],
                    [[120, 125], [80, 85], [45, 52]],
                    [[140, 165], [195, 245], [34, 40]],
                    [[124, 140], [230, 245], [34, 42]]
                    ]


    def __init__(self, RGB):
        self.R = RGB[0]
        self.G = RGB[1]
        self.B = RGB[2]
        self.colorString = self.identify_color
        print('Red: ' + str(self.R))
        print('Green: ' + str(self.G))
        print('Blue: ' + str(self.B))


#returns a number. will be valid index of totalMarbles if color reading was in the RANGES
#will be number greater than valid indexes of totalMarbles if color reading was in trash RANGES
#will be negative 1 if no valid range was found
    def identify_color_num(self):
        color = -1
        for i in range(0, len(self.color_ranges)):
            if ((self.R in range(self.color_ranges[i][0][0], self.color_ranges[i][0][1])) and (self.G in range(self.color_ranges[i][1][0], self.color_ranges[i][1][1])) and (self.B in range(self.color_ranges[i][2][0], self.color_ranges[i][2][1]))):
                  color = i
                  break
        return color

    def identify_color(self):
        color = ''
        i = 0
        for i in range(0, len(self.color_ranges)):
            if ((self.R in range(self.color_ranges[i][0][0], self.color_ranges[i][0][1])) and (self.G in range(self.color_ranges[i][1][0], self.color_ranges[i][1][1])) and (self.B in range(self.color_ranges[i][2][0], self.color_ranges[i][2][1]))):
                  color = self.color_strings[i]
                  break
        if (color == ''):
            color = self.default;
        return color

    def get_color_string(self):
        return self.colorString
