
from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
 
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
 
class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")
 
#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
 
#object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)