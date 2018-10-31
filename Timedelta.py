# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:01:05 2018

@author: ethan.kong
"""

import datetime;
currDate = datetime.date.today();

"""Example of Date"""
#print(datetime.date.today());
#print(currDate);
#print(currDate.year);
#print(currDate.month);
#print(currDate.day);

print("Timedelta 15 days : ");
print(currDate + datetime.timedelta(days=15));
print("Timedelta 25 hours : ");
print(currDate + datetime.timedelta(hours=25));
