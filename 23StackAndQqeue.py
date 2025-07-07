# stack --> 
# stack work with LIFO-> Last in First Out
passenger = []
passenger.append('Naved')
passenger.append('Saved')
passenger.append('Javed')

print(passenger) #['Naved', 'Saved', 'Javed']
passenger.pop()
print(passenger)#['Naved', 'Saved']



#Queue
#Queue work with FIFO--> Fisrt in first Out.
#
from collections import deque

customer = deque(["Sajid", "bajid", "Zajid","Kajid"])
print(customer) # deque(['Sajid', 'bajid', 'Zajid', 'Kajid'])
customer.popleft() # It's cut a value from 1st in queue.

print(customer) # deque(['bajid', 'Zajid', 'Kajid'])
