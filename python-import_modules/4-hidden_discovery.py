#!/usr/bin/python3
if __name__ == "__main__":
    __import__("hidden_4.pyc")
    for i in range(0, len(dir("hidden_4"))):
        if dir("hidden_4.pyc")[i][:2] != "__":
            print(dir("hidden_4")[i])
