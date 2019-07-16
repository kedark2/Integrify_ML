#!/usr/bin/env python
# coding: utf-8

# # Exercises (OOP with Python). MAX POINTS : 67
# 
# ## Task 1 -- Employee (21 + 1.5 p)
# 
# Create a class `Employee` that has:
# 
#  1)`init`-method, setting employee's first name : None, rank : 0, last name : None, pay and email in the format firstname.lastname@something.com . The : notation refers to default arguments. (2p)
#  
# 2) Create a static method to check whether a given day (indexed between 0 and 6) is an even number or odd number. The method is called is_even_day and should return True if it is even day, otherwise False. (2p)
# 
# 3) `promote`- method. Promote method promotes the employee's rank by 1 (1p)
# 
# 4) `raise_salary` method with input argument `amount`. This increases the salary of the employee by `amount`. (1p)
# 
# 5) has functionality to count the number of employees. Note that this cannot be done through `self`, but using a class variable. (1p)
# 
# 6) Add a `classmethod` to raise pay by amount (the method inputs the amount as an argument). (1.5p)
# 
# 7) Create an alternative constructor that uses the class definition instead. (2p)
# 
# 8) Add at least one setter and one getter method of your own choice. (2p)
# 
# 9) Define a sensible representation method `__repr__` for the class (2p)
# 
# 10) Create a subclass `Ballerina` as a subclass of `Employee`. Make sure to use the `super` in the constructor. The child class should have  one more argument (`dances` : list, that quantifies what types of dances the particular ballerina is able to dance). (2p)
# 
# 11) Create 1 new ballerina worker. (1p)
# 
# 12) Does the help of `Ballerina` print out anything else besides the attributes and methods? If yes, then what? (2p)
# 
# 13) Create a class variable of your own choice to both the `Employee` and `Ballerina` classes. Make sure that they have defined different values in these classes.  Then define a method in the `Employee` class that changes that class variable value. (2p)
# 
# 14) Continues from last point. If you run that method on the `Ballerina` object, which method is called, of that of the base class or child class? (1p)
# 
# 
# 

# Note:
# The same way as you call an object method `object.method()`, you may call the class method as `Classname.classmethod`, where instead of `self` the classmethod uses `cls` as default input argument, and returns `cls(input_arguments_here)`.

# ## Task 2:  Online Video Calling App (18p)
# 
# Create a class __VideoApp__ (1p)
# 
# 1. The _VideoApp_ must contain the following class attributes:
#    - __participants_online__ which contains the number of active callers default to 0 (1.5p)
#    - __action__ containing a list of 2 strings: "speaking", "silent" (1.5p)
from collections import namedtuple

class VideoApp:
    __participants_online__ = 0
    __action__ = ["speaking", "silent"]
    def __init__(self,__username__, __company__):
        self.__username__ = __username__
        self.__company__ = __company__

# 2. The _VideoApp_ must contain the class method:
#    - __show_participants_online__ which returns the print message indicating what participants are attending the meeting. (1.5p)
    @classmethod
    def __show_participants_online__(cls):
        return cls.__participants_online__

# 3.  The _VideoApp_ must contain the following attributes:
#    - __user_name__ which assigns name of the caller (1p)
#    - _company_ which indicates the company represented by the caller (1p)

# 4.  The _VideoApp_ must contain the following methods:
    #
    #    - __go_online__ which increases the attribute *participants_online* by 1 (1p)
    @classmethod
    def __go_online__(cls):
        cls.__participants_online__ += 1

    #    - __go_offline__ which subtracts 1 from the attribute *participants_online* and returns the new *_participants_online* (1p)
    @classmethod
    def __go_offline__(cls):
        if cls.__participants_online__ > 0:
            cls.__participants_online__ -= 1
        return cls.__participants_online__

    #    - _status_ which takes argument _action_ and checks if the action argument matches the string in the _action_
    #    class attribute, otherwise throws ValueError: "The user must either be "speaking" or "silent"". It also returns
    #    the message: "{self.user_name} is _action_" (2.5p)
    def __status__(self, __action__):
        if __action__ in self.__action__:
            return (f"{self.__username__} is {__action__}")
        else:
            raise ValueError("The user must either be 'speaking' or 'silent' ")


newApp = VideoApp("raj", "integrigfy")
print(newApp.__status__("silent"))


# 
# Create another class __Message__ (1p)
# 
# 1. It has following attributes: 
#    - __user_name__ 
#    - _message_ 
#    (1p)

class Message:
    def __init__(self, __user_name__, __message__):
        self.__user_name__ = __user_name__
        self.__message__ = __message__
    def _status_(self):
        return f"{self.__user_name__} sent the message: {self.__message__}"

newMsg = Message("Kedar", "How are you doing?")
print(newMsg._status_())

# 2. It has one method:
#    -  *_status* that returns: "{self.user\_name} sent the message: {self.message}". Make this method a  \_\_method (2p)
# 
# Create another class __ChatApp__ which inherits from both parent classes in the following order: __VideoApp__ and __Message__  (1p)
# 
# 1. Each _ChatApp_ takes same attributes as base classes
# Now create an instance of this class and explicity call the method \_\_status\_\_ from Message class (1p)
class ChatApp:
    pass

# ## Task 3 (4.5 p)
# 
# Write a class that **compares strings based on their length.**
# 
# The class has to have such a property  that we can compare different instances between each other based on the string length without spaces.
# ### Conditions:
# * Use the `__new__` dunder method properly. Note that the class string objects have to be initialized without spaces. (1.5p)
# * The class inherits its structure from the `str` class. (0.5p)
# * Define the Dunder methods `__le__`,`__ge__`,`__lt__`,`__gt__`,`__le__` in the class that allow comparison between class objects according to these methods. (2.5p)
# 

# ##  Task 4: PersonalInfo (13 p) 
# 
# * Create a class `PersonalJoiner` without init method. When don't we need an init method? (1.5p)
class PersonalJoiner:

    def join(*args, **kwargs):
        d = {}
        for keys in args:
            pass



# * Created `namedtuple` called `PersonalDetails` with a fieldname `date_of_birth`. (1p)

PersonalDetails = namedtuple('PersonalDetails', 'date_of_birth')

# * Create a new object `person_1_details` that is a subclass of `Personaldetails`, with `date_of_birth` equal to '09-04-1991'. (2p)


person_1_details = PersonalDetails(date_of_birth="09-04-1991")

# * Create a namedtuple called `person_features` with two fieldnames -- `eye_color` and `IQ_score`. (1p)



person_features = namedtuple('person_features',["eye_color", "IQ_score"])

# * Create an object `person_1_features` with green eyes and IQ score of 109. (1p)

person_1_features = person_features(eye_color = 'green', IQ_score = 109)




# * Can you print out the namespaces of both  `person_1_details` and `PersonalDetails` ? Why/why not? (1p)
# * Task : Add a static method `join` that is able to concatenate any amount of named tuples. Essentialy it has to return
# (namedtuple) containing details from all records in entry order (6p)
#
#     Example of behaviour:
#
#     `print(PersonalJoiner.join(person1_1_details, person1_1_features))` has to result in
#
#     `Person(date_of_birth='09-04-1991', eye_color='Green', IQ_score=109)` .
#
# **HINT : First load the input arguments to a list using NamedTuple `_asdict` method and then pass these keys to values to the NamedTuple.**

# ## Task 5 : Decorator1 (4p)
#
# Write a function called `double`.
#
# The function should decorate a function and return two copies of it's return value in a list.
def double(fcn):
    def wrapper(*args):
        return [fcn(*args), fcn(*args)]

@double
def addition(a,b):
    return a+b

print (addition(1,2))


# ## Task 6: Decorator2 (5p)
# Write a function call `verify`.
# The function that is passed to this function should only be called if a keyword argument-value pair
#role:admin exists,
# otherwise the function should return "invalid"

def verify(fcn):
    def fcn_that_wraps(**kwargs):
        if kwargs['role'] == 'admin':
            fcn(**kwargs)
        else:
            return 'invalid'
    return fcn_that_wraps

@verify
def check_verify(**kwargs):
    print("The verify function is verified")

check_verify('admin')

# In[ ]:






