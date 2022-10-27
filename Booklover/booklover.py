import pandas as pd

class BookLover:

    def __init__(self, name, email, fav_genre, num_books = 0,
  book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, book_rating):
        
        if book_name in self.book_list['book_name'].unique():
            print('This book is already in the book list')
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
                })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def has_read(self, book_name):
        if self.book_list['book_name'].eq(book_name).any():
            return True
        else:
            return False

    def num_books_read(self):
        return self.book_list.shape[0]
    
    def fav_books(self):
        df = self.book_list[self.book_list.book_rating > 3]
        return df

if __name__ == '__main__':
    #Testing out if the class works 
    mir = BookLover('Mir Muhammad Abdur Rahman', 'Abdurrahman@dukanor.com', 'Islamic Conquests')
    print(mir.name + ' ' + mir.email + ' ' + mir.fav_genre)
    mir.add_book('Quran', 10)
    print(mir.book_list)
    mir.add_book('Quran', 12)
    print(mir.book_list)
      