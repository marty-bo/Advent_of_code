

class Packet():

    def __init__(self, version, type, value, id, sub_packets):
        self.version = version
        self.type = type
        self.value = value
        self.id = id
        self.sub_packets = sub_packets
    
    def to_string(self, deep=0) -> str:
        heading = '\t'*deep
        res = heading + '>>>>>>>>' + '\n'
        res += heading + 'VERSION = ' + str(self.version) + '\n'
        res += heading + 'TYPE = ' + str(self.type) + '\n'
        if self.type == 4:
            res += heading + 'VALUE = ' + str(self.value) + '\n'
        else:
            res += heading + 'LENGTH = ' + str(len(self.sub_packets)) + '\n'
            for sub_packet in self.sub_packets:
                res += sub_packet.to_string(deep=deep+1)
        res += heading + '<<<<<<<<' + '\n'
        return res
    
    def version_numbers_sum(self):
        res = self.version
        if self.type != 4:
            for sub_packet in self.sub_packets:
                res += sub_packet.version_numbers_sum()
        return res
    
    def evaluate_expression(self):
        # sum
        if self.type == 0:
            return sum([sub_packet.evaluate_expression() for sub_packet in self.sub_packets])
        # product
        elif self.type == 1:
            sub_packets_res = 1
            for sub_packet in self.sub_packets:
                sub_packets_res *= sub_packet.evaluate_expression()
            return sub_packets_res
        # minimum
        elif self.type == 2:
            return min([sub_packet.evaluate_expression() for sub_packet in self.sub_packets])
        # maximum
        elif self.type == 3:
            return max([sub_packet.evaluate_expression() for sub_packet in self.sub_packets])
        # value
        elif self.type == 4:
            return self.value
        # greather than
        elif self.type == 5:
            return int(self.sub_packets[0].evaluate_expression() > self.sub_packets[1].evaluate_expression())
        # less than
        elif self.type == 6:
            return int(self.sub_packets[0].evaluate_expression() < self.sub_packets[1].evaluate_expression())
        # equal
        elif self.type == 7:
            return int(self.sub_packets[0].evaluate_expression() == self.sub_packets[1].evaluate_expression())
            pass
        return 0
