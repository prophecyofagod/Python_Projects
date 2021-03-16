# Mario Saiz

f=open('powerball.txt')
lines=f.readlines()
print ( lines[99] )




with open('powerball.txt', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    print (last_line)


def main():
    """Execution time test function"""
    L = []

    with open("powerball.txt") as f:
        for line in f:
            if '16 31 40 53 57 24' in line:
                 print (line)
                 break

        if __name__ == 'powerball.txt':
            import timeit
            print(timeit.timeit("test()", setup="from powerball.txt import test"))

main()
