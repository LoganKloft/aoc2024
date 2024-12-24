class AndNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = None
    
    def evaluate(self, node_lut):
        if self.value is not None:
            return self.value

        self.value = node_lut[self.left].evaluate(node_lut) & node_lut[self.right].evaluate(node_lut)
        return self.value

    def get_value(self):
        return self.value

class OrNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = None
    
    def evaluate(self, node_lut):
        if self.value is not None:
            return self.value

        self.value = node_lut[self.left].evaluate(node_lut) | node_lut[self.right].evaluate(node_lut)
        return self.value

    def get_value(self):
        return self.value

class XorNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = None
    
    def evaluate(self, node_lut):
        if self.value is not None:
            return self.value

        self.value = node_lut[self.left].evaluate(node_lut) ^ node_lut[self.right].evaluate(node_lut)
        return self.value

    def get_value(self):
        return self.value

class ValueNode():
    def __init__(self, value):
        self.value = value
    
    def evaluate(self, node_lut):
        return self.value

node_lut = dict()
num_z_wires = 0

with open("day_24/input.txt") as file:
    line = file.readline().strip()

    while line:
        wire, value = line.split(": ")
        node_lut[wire] = ValueNode(int(value))
        line = file.readline().strip()

    for line in file:
        in_wire_1, operator, in_wire_2, _, out_wire_1 = line.strip().split(' ')

        if operator == "XOR":
            node_lut[out_wire_1] = XorNode(in_wire_1, in_wire_2)
        elif operator == "AND":
            node_lut[out_wire_1] = AndNode(in_wire_1, in_wire_2)
        elif operator == "OR":
            node_lut[out_wire_1] = OrNode(in_wire_1, in_wire_2)

        if out_wire_1.startswith('z'):
            num_z_wires += 1

result = ['0'] * num_z_wires
for wire, node in node_lut.items():
    node.evaluate(node_lut)
    if wire.startswith('z'):
        result[int(wire[1:])] = str(node.get_value())

print(result)
print(int(''.join(reversed(result)), 2))