# ######################################################
# Author : Jingbo Yue
# email : yue53@purdue.edu
# ID : ee364b28
# Date : 01-20-2026
# ######################################################
import os # List of module import statements
import sys # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def evenResult(number_list, operation):
    """Even Number Result
    
    If the string is ”sum”, return the sum of all the elements that are even in the list. 
    If the string is ”product”, return the product of all the elements that are even in the list."""

    # DO SOMETHING HERE
    # If operation is Sum
    if operation == "sum":
        total_start = 0
        for num in number_list:
            if num % 2 == 0:
                total_start = total_start + num
        return total_start
    
    # If operation is Product
    elif operation == "product":
        product_start = 1
        for num in number_list:
            if num % 2 == 0:
                product_start = product_start * num 
        return product_start

        
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    print(evenResult([1, 2, 4, 6], "sum"))     
    print(evenResult([1, 2, 4, 6], "product")) 

    

