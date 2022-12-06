# # Nilai Interger
# # x = int(input("What's x: "))
# # y = int(input("What's y: "))

# # Nilai Float ber koma ,
# x = float(input("What's x: "))
# y = float(input("What's y: "))

# # Nilai Round nila terdekat
# # z = round( x + y)
# # z = round(x / y, 2)

# z = x / y
# # Mendigitkan angka z:.2f
# print(f"{z:.2f}")

def main():
    x = int(input("What's square: "))
    print("x square: ", square(x))
    

def square(n):
    return n * n


main()