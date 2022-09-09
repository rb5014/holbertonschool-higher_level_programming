#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    from calculator_1 import add, sub, mul, div
    func = add, sub, mul, div
    op = "+", "-", "*", "/"

    for i in range(1, 4):
        if argv[2] == op[i]:
            print(argv[1], op[i], argv[3], "=", func(argv[1], argv[3]))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
