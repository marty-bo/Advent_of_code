
import time
from Packet import Packet



HEXA_TO_BINARY = dict(zip(list('0123456789ABCDEF'), '0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111'.split(',')))



def hexa_to_binary(hexa : str) -> str:
    res = ''
    for hex in hexa:
        res += HEXA_TO_BINARY.get(hex)
    return res

def binary_to_decimal(bits : str) -> int:
    res = 0
    for bit in bits:
        res *= 2
        res += int(bit)
    return res


def read_packet(packet_input, deep=0, debug=False):
    if debug: print('\t'*deep+'>->->->->->')
    packet_len = 0

    version = packet_input[:3]
    packet_input = packet_input[3:]
    packet_len += 3
    version = binary_to_decimal(version)
    if debug: print('\t'*deep+'VERSION : %d' % (version))

    type = packet_input[:3]
    packet_input = packet_input[3:]
    packet_len += 3
    type = binary_to_decimal(type)
    if debug: print('\t'*deep+'TYPE : %d' % (type))

    if type == 4:
        bits = ''
        while packet_input[0] == '1':
            packet_input = packet_input[1:]
            packet_len += 1

            bits += packet_input[:4]
            packet_input = packet_input[4:]
            packet_len += 4

        packet_input = packet_input[1:]
        packet_len += 1

        bits += packet_input[:4]
        packet_input = packet_input[4:]
        packet_len += 4

        bits = binary_to_decimal(bits)
        if debug: print('\t'*deep+'BITS : %d' % (bits))


        if debug: print('\t'*deep+'<-<-<-<-<-<')
        p = Packet(version, type, bits, None, None)
        return (packet_input, packet_len, p)
    else:
        id = packet_input[:1]
        packet_input = packet_input[1:]
        packet_len += 1
        id = binary_to_decimal(id)
        if debug: print('\t'*deep+'ID : %d' % (id))

        if id == 0:
            length = packet_input[:15]
            packet_input = packet_input[15:]
            packet_len += 15
            length = binary_to_decimal(length)
            if debug: print('\t'*deep+'LENGTH : %d' % (length))

            sub_packets = []
            while length > 0:
                (packet_input, sub_length, sub_packet) = read_packet(packet_input, deep+1, debug)
                length -= sub_length
                packet_len += sub_length
                sub_packets.append(sub_packet)
            if debug: print('\t'*deep+'<-<-<-<-<-<')
            p = Packet(version, type, None, id, sub_packets)
            return (packet_input, packet_len, p)
        else:
            length = packet_input[:11]
            packet_input = packet_input[11:]
            packet_len += 11
            length = binary_to_decimal(length)
            if debug: print('\t'*deep+'LENGTH : %d' % (length))

            sub_packets = []
            while length > 0:
                (packet_input, sub_length, sub_packet) = read_packet(packet_input, deep+1, debug)
                length -= 1
                packet_len += sub_length
                sub_packets.append(sub_packet)
            if debug: print('\t'*deep+'<-<-<-<-<-<')
            p = Packet(version, type, None, id, sub_packets)
            return (packet_input, packet_len, p)



def f(debug=False):

    f = open('input.txt')
    packet_input = f.readline()
    f.close()

    packet_input, packet_len, packet = read_packet(hexa_to_binary(packet_input), debug=debug)
    
    # print(packet.to_string())

    print('[f]: Sum of all versions = %d Evaluation of the expression = %d' % (packet.version_numbers_sum(), packet.evaluate_expression()))

    return
    



print("########################################")
start_time = time.time()
f(debug=False)
print("----------- %.8s seconds -----------" % (time.time() - start_time))
