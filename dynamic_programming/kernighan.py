# conversion and counting method:
def count_set_bits_1(n):
    # Convert to binary and count the number of '1's
    return bin(n).count('1')


# Brian Kernighan’s Algorithm for counting set bits
# How It Works
#
# The key idea is that the operation n &= (n - 1) removes the lowest
# set bit (bit with value 1) from  n  in each iteration:
# 	1.	Subtracting 1 from  n  flips all the bits after the lowest set bit,
# 	including the lowest set bit itself.
# 	2.	The bitwise AND operation between  n  and  n - 1  clears the lowest
# 	set bit while keeping the rest of the bits unchanged.
#
# Example Walkthrough
#
# For  n = 13  (binary 1101):
# 	1.	Initial  n = 13 , count = 0:
# 	•	 n - 1 = 12  (binary 1100)
# 	•	 n &= n - 1  => \( 1101 \& 1100 = 1100 \) ( n = 12 )
# 	•	Increment count to 1.
# 	2.	 n = 12 , count = 1:
# 	•	 n - 1 = 11  (binary 1011)
# 	•	 n &= n - 1  => \( 1100 \& 1011 = 1000 \) ( n = 8 )
# 	•	Increment count to 2.
# 	3.	 n = 8 , count = 2:
# 	•	 n - 1 = 7  (binary 0111)
# 	•	 n &= n - 1  => \( 1000 \& 0111 = 0000 \) ( n = 0 )
# 	•	Increment count to 3.
# 	4.	Loop exits as  n = 0 . Final count = 3.
def count_set_bits_2(n):
    count = 0
    while n > 0:
        count += 1
        n &= (n-1)
    return count


# Example usage
n = 23
print(f"The number of set bits in {n} (binary: {bin(n)[2:]}) is {count_set_bits_1(n)}")
print(f"The number of set bits in {n} (binary: {bin(n)[2:]}) is {count_set_bits_2(n)}")