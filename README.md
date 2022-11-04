# Book Library FastAPI backend application

This is a standalone project that will 
follow-up crash course that we are taking in parallel. 
the crash course that we are taking in parallel. 
The Project should be develop according to real-world Book Library example,
with only core and esential functionalities. 
Please consider using pydantic modeling, Classes, Inheritance, and Polymorphism for 
sential functionalities. 
Please consider using pydantic modeling, Classes, Inheritance, and Polymorphism for 
everything, even when you don't need, just use it for practicing.

The Entire project is separated into project is separated in three milestones:
##### 1. Creating environment, Modeling and Frameworking
##### 2. Creating database and fill it with data
##### 3. Working with FastAPI, to create Endpoints for administration and JSON consuming



## 1. Creating an environment, Modeling, and Frameworking

#### 1.1. Creating environment

##### Start by creating a virtual environment for this project by using in terminal:
` python -m .venv venv `

##### Activate the following environment by entering the following in a terminal:
` source .venv/bin/activate`

##### Install pydantic
` pip install pydantic `

#### 1.2. Create models (will be updated):

##### Define the following pydantic models



Book:
```
attributes: ID, Title, Artist, Issue Year, Number of Pages, Genre, Price

Validators:

Book without a Title and Artist should not be created, 
also, the number of pages should be greater than 0

Defaults:
The price should default to 0.
```

Artist:
```
attributes: ID, Full Name, Allias, Country, Prefered Genre

Validators:
Artists without Full Names should not exist.

```

Customer:
```
attributes: ID, Full Name, Address, Balance

Validators:
Users without Full Names should not exist.
```

#### 1.3. Frameworking (Linking) models

Book<->Artist

```
Create the field "artist" in the Books model that will contain Artist
```

Artist<->Books

```
Create a field "books" that will contain a list of Books written by the Artist
```

Customer<->Books:

```
Create a field "books" containing a list of Books acquired by the Customer.
```
