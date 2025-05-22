#Generate a random 12-character password containing:
#At least 1 uppercase
#At least 1 lowercase
#At least 1 digit
#At least 1 special character

import random
import string

length = 12
random_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
print(random_string)    
