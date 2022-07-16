def switch(x, y, b):
    return (x * b) + (y * (1 - b))

if __name__ == '__main__':
    print(switch(100, 200, 0))
    print(switch(100, 200, 1))
