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
"""lowe case of %y show 2 digits of year"""
"""upper case of %Y show 4 digits of year"""
"""lowe case of %b show short name of month"""
"""upper case of %B show full name of month"""

print(currDate.strftime('%d %b, %y')); 
print(currDate.strftime('%d %b, %Y')); 
print(currDate.strftime('%A %d %B, %Y'));
print(currDate.strftime('Please attend our event %A, %B %d in the year %Y'));
