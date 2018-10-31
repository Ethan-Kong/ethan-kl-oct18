# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:18:12 2018

@author: ethan.kong
"""
"""Example 1""""""
answer=input("Would you like express shipping? (Yes or No) ").lower();
if answer == "yes" :
    print("That will be an extra $10.");
else:
    print("Thank you!");    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Example 2""""""
deposit = input("How much would you like to deposit? ");
if float(deposit) > 100 :
    print("You get a free toaster!");
print("Have a nice day!");
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Example 3""""""
deposit = input("How much would you like to deposit? ");
if float(deposit) > 100 :
    print("You get a free toaster!");
else:
    print("Enjoy your mug!");    
print("Thank you!"); 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Example 4""""""
answer=input("Would you like express shipping? (Yes or No) ").lower();
shippingSelected = False;
if answer == "yes" :
    print("That will be an extra $10.");
    shippingSelected = True;
else:
    print("Standard shipping selected!"); 
    

if(shippingSelected) :
    print("Thank you for selecting Express shipping option!")
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Example 5""""""
country = input("Where are you from? ").upper();

if country == 'CANADA' :
    print("Hello Canada!");
elif  country == 'USA' :
    print("Hello USA!");
else :
    print("Thank you & Bye!")    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    