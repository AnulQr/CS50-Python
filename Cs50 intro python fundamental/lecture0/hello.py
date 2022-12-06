#  Sebutkan nama
# name = input("What's your name: ").strip().title()

# fist, last = name.split(" ")

#  Tampilkan nama
# print(f"My name is: {last}")


def main():
    name = input("What's your name: ")
    hallo(name)

def hallo(to="World"):
    print("Hallo", to)
    
main()