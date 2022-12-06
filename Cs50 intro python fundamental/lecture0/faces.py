# duan multipe replace()
def main():
    # input pesan
    msg = input()

    # convert faces
    result = convert(msg)
    print(result)

def convert(msg):

    # face icon
    msg1 = msg.replace(":)", "🙂")
    msg2 = msg1.replace(":(", "🙁")

    # kembali kan nilai msg2 ke msg
    return msg2

main()