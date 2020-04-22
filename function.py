def square(x):
    return x * x


def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
