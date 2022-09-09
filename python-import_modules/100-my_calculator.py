#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    from calculator_1 import add, sub, mul, div
    list_func = add, sub, mul, div
    list_op = "+", "-", "*", "/"
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    for i in range(0, 4):
        if op == list_op[i]:
            print(a, op, b, "=", list_func[i](a, b))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
