from math import floor
import random
class Switch:
    def __init__(self, id):
        self.id = id
        self.is_on = False

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

class Wire:
    def __init__(self, id, connected_switch):
        self.id = id
        self.connected_switch = connected_switch

    def state(self):
        return self.connected_switch.is_on

num_switches = 90
swish_list = [Switch(i) for i in range(num_switches)]

num_wires = 90
wire_list = [Wire(i, random.choice(swish_list)) for i in range(num_wires)]

def search_swish(wire, swish_list):
    list_len = len(swish_list)
    if list_len == 1: return swish_list[0]
    mid_index = floor(list_len/2)
    if not wire.state():
        for swish in swish_list[:mid_index]:
            swish.on()
        if wire.state():
            return search_swish(wire, swish_list[:mid_index])
        return search_swish(wire, swish_list[mid_index:])
    else:
        for swish in swish_list[:mid_index]:
            swish.off()
        if not wire.state():
            return search_swish(wire, swish_list[:mid_index])
        return search_swish(wire, swish_list[mid_index:])
    
    


print(search_swish(wire_list[25], swish_list).id)