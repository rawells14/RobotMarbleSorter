class Color(object):
    color_strings = ['Large Red', 'Small Red', 'Large White', 'Small White',
                     'HDPE', 'Large Blue', 'Small Blue', 'Large Green', 'Small Green',
                     'Large Yellow', 'Small Yellow', 'Steel']
    color_ranges = [[[111, 160],[60, 75],[39, 47]],
                    [[87, 110], [62, 68], [39, 47]],
                    [[170, 255], [185, 255], [90, 120]],
                    [[115, 140], [115, 140], [53, 60]],
                    [[98, 108], [90, 110], [50, 60]],
                    [[85, 94], [80, 95], [60, 75]],
                    [[75, 84], [60, 75], [42, 55]],
                    [[75, 110], [76, 130], [40, 55]],
                    [[75, 89], [80, 90], [40, 55]],
                    [[150, 195], [115, 130], [40, 50]],
                    [[105, 135], [90, 120], [40, 50]],
                    [[90, 95], [70, 85], [43, 47]]]

print(len(Color.color_ranges))
