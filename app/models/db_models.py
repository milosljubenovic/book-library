from pydantic import BaseModel
import pydantic 



class Book(BaseModel):  
    id:int
title:str
artist:str
issue_year:int
number_of_pages: int
genre:str
price:int


class Artist(BaseModel):
    id:int
full_name:str
alias:str
country:str
prefered_genre:str


class Customer(BaseModel):
    id:int
full_name:str
address:str 
prefered_genre:str





artist = Artist(id= 1, full_name= "Henry Cavil", alias="Superman", country="United Kingdom", prefered_genre="Fantasy")
if artist.full_name == None:
        print("Please enter the artists' full name")

book = Book(id=1, title="The Hobbit", artist="J.R.R. Tolkien", issue_year=1937, number_of_pages=295, genre="Fantasy", price=1000)
if book.title and book.artist and book.page > 0 == None:
        print("Please enter the book title and artist")
if book.title == None:
        print("Please enter the book's title")

customer = Customer(id=1, full_name="John Doe", address="1234 Main Street", prefered_genre="Fantasy")
if customer.full_name == None:
        print("Please enter your full name")