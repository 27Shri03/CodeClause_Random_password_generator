import random  # To generate or to choose random numbers.
import string  # To generate a password.

# User will enter the length of the password.

n = int(input("Enter the length of the password: "))

# Source string is used to combine the letters and digits.

main = string.ascii_letters + string.digits

# We will choose each character randomly from the source string and add it into our empty string using a for loop till n.

password = ''.join((random.choice(main) for i in range(n)))

# Now we will print our password.

print("\nRandom password with length", n, "is: ", password)
