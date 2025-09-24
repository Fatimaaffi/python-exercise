class Book:
    title=""
    author=""
    year=""
    is_checked_out=False
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
      
        
    def checkout(self):
     self.is_checked_out=True
    def return_book(self):
       self.is_checked_out=False
    def __str__(self):
       return f"{self.year} by {self.author} checked out:{self.is_checked_out}"

class Library:
  
   def __init__(self):
      self.collection=[]
   def add_book(self,Book):
      self.collection.append(Book)
   def list_books(self):
      for book in self.collection :
         print( f"{book.title} +checked_out: {book.is_checked_out}")
   def find_book(self,title):
      for book in self.collection:
         if book.title.lower()==title.lower():
            return book
      return None

b1 =Book("1984","george",1949)
b2 =Book("1964","lucas",1978)
lib=Library()
lib.add_book(b1)
lib.add_book(b2)
lib.list_books()
b1.checkout()
print(b1)

      
      


