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
                    'box']

    #NEW RANGES
    color_ranges = [[[37,69],[35, 62], [8, 16]],
                    [[81, 111], [63, 88], [31, 49]],
                    [[147, 195], [115, 157], [50, 78]], #small white
                    [[205, 270], [174, 250], [118, 137]],
                    [[20, 43],[15,28],[13,37]],
                    [[43, 60], [25, 38], [49, 63]],
                    [[15, 21], [60, 98], [0, 8]],
                    [[15, 27], [60, 125], [0, 12]],
                    [[13,18], [13, 18], [0, 8]]
                    ]


    def __init__(self, RGB):
        self.R = RGB[0]
        self.G = RGB[1]
        self.B = RGB[2]
        self.colorString = self.identify_color()
        print('Red: ' + str(self.R))
        print('Green: ' + str(self.G))
        print('Blue: ' + str(self.B))


#returns a number. will be valid index of totalMarbles if color reading was in the RANGES
#will be number greater than valid indexes of totalMarbles if color reading matches box color
#will be negative 1 if no valid range was found, so it is trash
    def identify_color_num(self):
        color = -1
        for i in range(0, len(self.color_ranges)):
            if ((self.R in range(self.color_ranges[i][0][0], self.color_ranges[i][0][1])) and (self.G in range(self.color_ranges[i][1][0], self.color_ranges[i][1][1])) and (self.B in range(self.color_ranges[i][2][0], self.color_ranges[i][2][1]))):
                  color = i
                  break
        return color
#OLD FUNCTION
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
