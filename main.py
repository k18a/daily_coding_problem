from problem1 import two_number_sum

def main():
    assert two_number_sum([1,2,3],10) is False
    assert two_number_sum([1,2,3,4,5,6],10) is True
    assert two_number_sum([9,4,5,2,4,7,8],11) is True

if __name__ == '__main__':
    main()

