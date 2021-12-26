
import time

def f1():
    # count the number of 1, 4, 7 and 8 in the outputs
    count = 0
    # read input
    f = open('input.txt')
    for line in f.readlines():
            for out in line.split('|')[1].split():
                n = len(out)
                if n <= 4 or n == 7:
                    count += 1
    f.close() 
        
    print('[f1]: Count = %d' % (count))
    return


def f2():
    count = 0

    # dict(digit : associated segment)
    SEG_PER_DIGIT = {0:'abcefg',1:'cf',2:'acdeg',3:'acdfg',4:'bcdf',5:'abdfg',6:'abdefg',7:'acf',8:'abcdefg',9:'abcdfg'}
    
    # give an id to each wire based on the length of the signals in wich the wire appears
    def build_wire_id(signals):
        wire_id = {l:0 for l in 'abcdefg'}
        for l in wire_id.keys():
            for signal in signals:
                if l in signal:
                    wire_id[l] += len(signal)**2
        return wire_id

    # from dict(wire : id) to dict(id : wire)
    def reverse_wire_id(wire_id):
        return {wire_id.get(k) : k for k in wire_id.keys()}
    
    WIRE_ID = build_wire_id(SEG_PER_DIGIT.values())
    print(list(zip(WIRE_ID.keys(), WIRE_ID.values())))

    ID_WIRE = reverse_wire_id(WIRE_ID)
    print(list(zip(ID_WIRE.keys(), ID_WIRE.values())))
    
    # associate each wire to a segment
    # return dict(wire : segment)
    def join_wire_segment(id_wire):
        return {id_wire.get(id) : ID_WIRE.get(id) for id in id_wire.keys()}
    
    # translate the signals in <signals> with <wire_segment>
    def translate_signals(wire_segment, signals):
        translated_signals = []
        for signal in signals:
            translated_signal = ''
            for wire in signal:
                translated_signal += wire_segment.get(wire)
            translated_signals.append(translated_signal)
        return translated_signals
    
    # return the digit associate to the combination of segments in <segments>
    def signal_to_digit(segments_list):
        valid = False
        digits = []
        for segments in segments_list:
            segments = ''.join(sorted(segments))
            for key in SEG_PER_DIGIT.keys():
                if segments == SEG_PER_DIGIT.get(key):
                    digits.append(key)
                    break
        return digits
                


    # read input
    f = open('input.txt')
    for line in f.readlines():
        left, right = line.split('|')
        left = left.split()
        right = right.split()

        wire_id = build_wire_id(left)
        id_wire = reverse_wire_id(wire_id)
        wire_segment = join_wire_segment(id_wire)
        # print('WIRE_ID  :',list(zip(wire_id.keys(), wire_id.values())), '\nWIRE_SEG :',list(zip(wire_segment.keys(), wire_segment.values())))
        translated_signals = translate_signals(wire_segment, right)
        digits = signal_to_digit(translated_signals)

        tmp = 0
        for digit in digits:
            tmp *= 10
            tmp += digit
        count += tmp

    f.close() 
        
    print('[f2]: Count = %d' % (count))
    return


print("########################################")
start_time = time.time()
f1()
print("--------- %.7s seconds ---------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f2()
print("--------- %.7s seconds ---------" % (time.time() - start_time))
