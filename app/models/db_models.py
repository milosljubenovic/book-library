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



book = Book 

class Artist(BaseModel):
    id:int
full_name:str
alias:str
country:str
prefered_genre:str



artist = Artist

class Customer(BaseModel):
    id:int
full_name:str
address:str 
prefered_genre:str

customer = Customer 


