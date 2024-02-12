# This program prints the pattern of stars which increases by count 1 till middle row and 
# then decreases by count 1 until 1 * is displayed
# This code uses only one for loop
# Referred to manipulate string printing https://realpython.com/python-strings/ 
# Referred https://www.geeksforgeeks.org/print-without-newline-python/ for string printing
# 

end = 9 # Assign end variable to hold the number of rows of *s to be printed

mid = int (end / 2) + 1 # mid holds the middle row out of all rows. In our example 9 rows so we do not 
# need float we divide end by 2 and cast it to int so 9 / 2  is 4.5 cast to int is 4. Middle row is 5 so 
# we add 1 to mid

j=2 # Set variable j to 2 which we will use while looping back from end after printing half the rows

for i in range (1, end+1): # Use for loop to loop from rows 1 to 10 so 9 loops
    if (i <= mid): # Check if i is less than or equal to middle row and print * i times
        print("*"*i) # referred link mentioned for string printing in same line and multiple *
    else: # If middle row has been printed then print the remaining rows but with decreasing *
        print("*"*(i-j))
        j += 2 #Use variable j to subtract the number of * to be printed as i the row count increases.
        #So when i is 6 we print 4 *, i is 7 we print 3, i is 8 we print 2 and so on