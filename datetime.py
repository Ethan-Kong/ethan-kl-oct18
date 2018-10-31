# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:10:39 2018

@author: ethan.kong
"""

import datetime;
currDate = datetime.date.today();

"""Example of Datet"""
print(datetime.date.today());
print(currDate);
print(currDate.year);
print(currDate.month);
print(currDate.day);

"""Format Date"""
print(currDate.strftime('%d %b, %y')); 

"""lowe case of %y show 2 digits"""
"""upper case of %Y show 4 digits"""
"""lowe case of %b show short month"""
"""upper case of %B show full month"""

print(currDate.strftime('%d %b, %Y')); 
print(currDate.strftime('%A %d %B, %Y'));