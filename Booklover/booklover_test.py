import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        "Tests add_book function by adding a book and checking if the book is in the list"
        
        testUser = BookLover('Test Name', 'Test Email', 'Test Genre')
        testUser.add_book('Test Book', 1)
        
        value = 'Test Book' in testUser.book_list['book_name'].unique()
        message = 'Newly created book "Test Book" is not in list'
        self.assertTrue(value, message)
    
    def test_2_add_book(self):
        "Tests add_book function to see if it ignores requests for books that have already been read"
        
        mir = BookLover('Mir Muhammad Abdur Rahman', 'Abdurrahman@dukanor.com', 'Islamic Conquests')
        
        mir.add_book('Quran', 10)
        print(mir.book_list)
        
        mir.add_book('Quran', 12)
        print(mir.book_list)

        value = (1 == mir.book_list['book_name'].value_counts()['Quran'])
        message = 'More than one Test Book in the book list'
        
        self.assertTrue(value, message)
    
    def test_3_has_read(self):
        testUser = BookLover('Test Name', 'Test Email', 'Test Genre')
        testUser.add_book('Test Book', 1)
        
        value = testUser.has_read('Test Book')
        message = 'Has read not working properly'
        
        self.assertTrue(value, message)
    
    def test_4_has_read(self):
        
        testUser = BookLover('Test Name', 'Test Email', 'Test Genre')
        testUser.add_book('Test Book', 1)
        
        value = testUser.has_read('Test')
        message = 'Has read not working properly'
        
        self.assertFalse(value, message)
    
    def test_5_num_books_read(self):
        testUser = BookLover('Test Name', 'Test Email', 'Test Genre')
        testUser.add_book('Test Book', 1)
        
        testUser.add_book('Book', 2)
        
        value = testUser.num_books_read()
        message = 'Num of books read not working properly'
        self.assertEqual(value, 2, message)
        
    def test_6_fav_books(self):
        
        testUser = BookLover('Test Name', 'Test Email', 'Test Genre')
        
        testUser.add_book('Test Book', 5)
        
        testUser.add_book('Test Book2', 2)
        
        testUser.add_book('Test Book3', 4)
                
        df = pd.DataFrame({
                'book_name': ['Test Book', 'Test Book2', 'Test Book3'], 
                'book_rating': [5.0, 2.0, 4.0]
            })
        
        df = df[df.book_rating > 3]
        
        value = df.equals(testUser.fav_books())
        message = 'Fav books not working'
        self.assertTrue(value, message)
        
if __name__ == '__main__':
    unittest.main()
    
    