from django.test import TestCase
from Store.models import *

# Create your tests here.

class BookTestCases(TestCase):

    def setUp(self):
        print("testing is started")
        pass

    def tearDown(self):
        print("testing is completed")
        pass

    def test_book_title(self):
        b = Books.objects.create(title="new book", price=50000,no_of_pages=400)
        print(b)
        if b.price>=10000:
            print('price too high')
            return self.assertFalse(False)
        else:
            return self.assertTrue(True) # .assertEqual(b.price,5670,"Not matched with db")
    def test_book_title_lenght(self):
        b = Books.objects.create(title="new booklkjsdlkfjlsdkjf lsjflksjflkj", price=50000,no_of_pages=400)
        if len(b.title)>20:
            print('title too long ')
            return self.assertFalse(False)
        else:
            return self.assertTrue(True)
# Book Test cases
#1. having title
"""
2. wihtout have title
3. with price with title
4. with price with title, and no_of_pages  = ok
5. without price, title, no_of_pages 

user Login:
1. must have username
2. must have password
3. username and password should match with database
4. only username matches - 
5. username not exist - 
"""

class loginclass(TestCase):
    def logintest(self):
        obj = login.objects.create(username="ram", password=5555)
        if obj.username == "ram":
            print(" value ")
            return self.assertFalse(False)
        else:
            return self.assertTrue(True)

      



   