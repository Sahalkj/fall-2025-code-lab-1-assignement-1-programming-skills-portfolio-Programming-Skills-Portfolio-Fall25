def check_num(number):
    if number % 2 == 0:
        return "The Number is Even"
    else:
        return "The Number is Odd"

def main():
    number = int(input("Enter a number: "))
    print(check_num(number))

if __name__ == "__main__":
    main()