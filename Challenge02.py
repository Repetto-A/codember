def decode(encrypted_msg):
    global message

    msg = encrypted_msg.split(' ')
    for i in range(len(msg)):
        code = msg[i]
        pointer = 0
        letters = ''
        while pointer<=len(code):      # Pick pairs of three and check if the number is bigger than 122, in this case pick just 2
            try:
                couple = code[pointer] + code[pointer+1] + code[pointer+2]
                changes = 3
                if int(couple)>122:
                    couple = code[pointer] + code[pointer+1]
                    changes = 2
                pointer += changes
                letters += lower_case_ascii[int(couple)]
            except:
                message.append(letters)
                break

def show(message):
    for msg in message:
        print(msg, end=' ')


def main():
    global lower_case_ascii, message

    msg = '11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101'
    lower_case_ascii = {97: "a", 98: "b",99: "c",100: "d",101: "e",102: "f",103: "g",104: "h",105: "i",106: "j",107: "k",108: "l",109: "m",110: "n",111: "o",112: "p",113: "q",114: "r",115: "s",116: "t",117: "u",118: "v",119: "w",120: "x",121: "y",122: "z"}
    message = []
    message.append('submit')
    decode(msg)
    show(message)


if __name__ == '__main__':
    main()