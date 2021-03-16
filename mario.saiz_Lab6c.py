#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 6a


def main():

    with open("powerball.txt") as f:
        for line in f:
            if "33 36 38 52 60 11" in line:
                 print ("This is the last line: " +line)
                 break

main()

def test():
    """Execution time test function"""
    L = []
    for i in range(1000):
        L.append(i)

if __name__ == '__main__':
    import timeit
    print("\nIt took this many seconds to find the last line: ")
    print(timeit.timeit("test()", setup="from __main__ import test"))

