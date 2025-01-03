from django.test import TestCase
from .models import *
from .views import add ,addvalues
import unittest
# Create your tests here.

# if we get ok then it working successfully

class bookclasstest(TestCase):
    def setUp(self):
        a=booktestcase.objects.create(title='fiction',cost=200) #booktestcase is model name
        # a=booktestcase.objects.create(title='nonfiction',cost=400)
        booktestcase.objects.create(title='novel',cost=300)
        print(a) #o/p booktestcase object(1) bzc above 1 variable 'a' is created 
        print("class",booktestcase) #class <class 'Cart.models.booktestcase'> 
        print(a.title) #o/p fiction    

    def testingbook(self):
        ## var=booktestcase.objects.get(title='fiction',cost=200)#it checked with above values match=ok
        # self.assertEqual(var.title,'fiction')
        # var=booktestcase.objects.get(title='novel',cost=300)
        # self.assertEqual(var.title,'novel')
        # print("working",var) #o/p working booktestcase object (2)
        # var=booktestcase.objects.get(title='novelone',cost=300)
        # self.assertEqual(var.title,'novel')  #Cart.models.booktestcase.DoesNotExist: booktestcase matching query does not exist.
        # var=booktestcase.objects.get(title='novel',cost=300)
        # self.asertEqual(var.title,'novelone') #AsertionError: 'novel' != 'novelone'
        var=booktestcase.objects.get(title='novel',cost=300)
        self.assertEqual(var.title,'novel' ,"book not matched")
        # self.assertEqual(var.get_details(),"this book is related to novels")
        print(var.cost) #300


    def test_entry(self):
        obj=booktestcase()
        obj.title="hello"
        obj.cost=6666
        # print("test_entry",obj.title) # o/p test_entry hello
        obj.save()

        record=booktestcase.objects.get(pk=obj.id)
        self.assertEqual(record,obj)

    # def create_book(self ,title="new book",cost=444):
    #     print("hhhhh",title)  #hhhhh new book   hhhhh bookstore
    #     return booktestcase.objects.create(title=title,cost=cost)
        

    # def test_book_qs(self):
    #     title1="bookstore"
    #     cost1=333
    #     var4=self.create_book(cost=cost1)
    #     var5=self.create_book(title=title1)
    #     print(var5.title) # o/p bookstore
    #     print(var4.cost) #333
    #     qs=booktestcase.objects.filter(title=title1)
    #     self.assertEqual(qs.count(),1)

class testcaseadd(unittest.TestCase):
    def test_add(self):
        # self.assertEqual(add(50,30),100) #AssertionError: 80 != 100
        self.assertEqual(add(50,50),100)
        print("ADDITION OF a and b is",add(50,12))  # o/p .ADDITION OF a and b is 62
        # print(add("hello","world"))   #o/p ValueError: a and b must be int or float
        # print(addvalues("hello","world")) # o/p helloworld new fun is created

    def test_value(self):
        self.assertRaises(ValueError,add,'a',10)  # no error 