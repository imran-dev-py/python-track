# import the module
from assignment import area
from assignment import email_generator
import assignment
# display message 'Enjoy using our module'
print(assignment.intro)
# output the area of a square with a side length of 6 units using the area fn
print(assignment.area(6))
# remove the module
del assignment
# import the email_generator fn
print(email_generator('imran', 'ahmed', 'gmail', '.com'))
# import the area fn
print(area(6))
