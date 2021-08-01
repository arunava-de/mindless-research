def collatz_ize(n, dig_freq_first, dig_freq_last):
    
    while n!=1:
        first = n//(10**(count_digs(n)-1))
        last = n%10
        dig_freq_first[first] += 1
        dig_freq_last[last] += 1
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
    
    return True

def count_digs(n):
    c = 0
    while n>0:
        n = n//10
        c += 1
    return c

if __name__=="__main__":
    dig_freq_first = {}
    dig_freq_last = {}

    for i in range(1,10):
        dig_freq_first[i] = 0
        dig_freq_last[i] = 0
        
    dig_freq_last[0] = 0

    print("Please enter upper bound of computation")
    n = int(input())

    for i in range(1,n):
    
        collatz_ize(i, dig_freq_first, dig_freq_last)

    print("Distribution of first digit")
    print(dig_freq_first)

    print()

    print("Distribution of last digit")
    print(dig_freq_last)

