# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:34:00 2018

@author: ethan.kong
"""

guests = ['first','second','third']
#print(guests[1])
#print(guests[-1])
#print('First value is Initial : ' + guests[0])

guests[0] = 'Steve'

#print('First value is Initial : ' + guests[0])

guests.append('New Guy')

#print('New value is now : ' + guests[-1])

#guests.remove('second')
#print('Second Element is : ' + guests[1])

#del guests[1]
#print('Second Element after remove is : ' + guests[1])

#print(guests.index('second'))

#for step in range(4):

"""
for step in range(len(guests)):
    print(guests[step])

scores = [78,68,88,98,25]
#print(scores[3])
#print(scores[-1])
"""

guests.sort()

"""
for guest in guests:
    print(guest)

print ("Done")
"""

scores = [78,68,88,98,25]
scores.sort()
for score in scores:
    print(score)

print ("Done")