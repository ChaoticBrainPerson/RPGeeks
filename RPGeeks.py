from numpy import binary_repr

def decode_message(Serial_number, message):
    decode= []
    i = 0
    sn_code = ""
    while len(sn_code)<8:
        try:
            sn_code += str(int(Serial_number[i]))
            i += 1
        except Exception as e:
            i += 1
    sn_code = binary_repr(int(sn_code))
    for i in range(len(sn_code)):
        if sn_code[i] == "0":
            decode.append(1)
        else:
            decode.append(-1)
    len_ID = len(decode)
    text = []
    for i in range(len(message)):
        if message[i] == "0":
            text.append(1)
        else:
            text.append(-1)
        
        
    decode_ints = []
    [decode_ints.append(text[i]*decode[i%len_ID]) for i in range(len(message))]

    decode_string = ""
    for i in range(0,len(decode_ints), len_ID):
        dc_code= (sum(decode_ints[i:(i+len_ID)])/len_ID)
        if dc_code <0:
            decode_string += "1"
        else:
            decode_string += "0"

    decode_word = ""
    for i in range(0, len(decode_string), 8):
        decode_word = decode_word + str(chr(int(decode_string[i:i+8], 2)))
    return(decode_word)
def encode_message(Serial_number, message):
    Binary_word = ""
    i = 0
    sn_code = ""
    while len(sn_code)<8:
        try:
            sn_code += str(int(Serial_number[i]))
            i += 1
        except Exception as e:
            i += 1
    encode = binary_repr(int(sn_code))
    for i in range(len(message)):
        Binary_word = Binary_word + binary_repr(ord(message[i]), width = 8)

    msg = ""
    for i in range(len(Binary_word)):
        for j in range(len(encode)):
            if Binary_word[i] == encode[j]:
                sc_str = 0
            else:
                sc_str = 1
            msg += str(sc_str)
    return(msg)