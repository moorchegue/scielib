##############
Specifications
##############


Original specs
==============

Imagine you’re helping to build an app for the local book-library in your town.
The app will help users see what books are available for rent, under what
prices. Users will be able to communicate with other users, follow them, read
their reviews on books etc.

1. Design the app’s database.  

The library db should contain data regarding books, users, transactions
history, top sellers, clients’ relations with one another, reviews, etc.
describe the tables will you use. 
 
2. Design the library’s RESTful API document. 

Add all the necessary calls you think of, such as adding new users, renting
books, searching for a specific book, etc. 
 
3. Write a query that will pull all the books with same price as the 2nd book
ever taken by user ‘x’ (x is an input).  

For example, David's book renting history is: 

	* aug 2012 – took book “java for beginners” 
	* aug 2013 – took book “java for pros” 
	* jan 2014 – took book “java vs chuck Norris” 
	* feb 2015 – took book “is john snow object oriented?” 
	* mar 2015 – took book “java after death” 
 
For the query with input “David” I would expect to see all the books with the
price of the book named “java for pros” (his 2nd time renting a book).
 
Special note: if the assignment is not 100% clear – feel free to add / assume
anything that will make you.


Notes
=====

Implementation tech choices
---------------------------

For a real project it would make a lot of sense to go with
`Oscar <https://github.com/tangentlabs/django-oscar>`__, as it already has all
prerequisites necessary for successful launch (particularly payment methods,
transactions, customer communications, etc), only adding several necessary
customisations to support rental business logic.

However since this is merely an exercise / prototype with generic specs, pure
Django with a couple of extra packages would allow to build the project faster
and with a reserve of flexibility, should further improvements / changes be
required.


DB schema
---------

Categorization
~~~~~~~~~~~~~~

Briefly looking at a couple of existing online book stores, it seems to be
neccessary for a book catalogue of a significant size to have navigation with
categories (one-to-many), genres (many-to-many) and collections (many-to-many).
Browsing books by author seems to also improve user experience.


Stock-taking
~~~~~~~~~~~~

As we're talking about a town library, it is assumed that tracking book copies
(specimen) is not feasible due to limited recourses, thus we only need to track
patrons borrowing certain books, not the copies, and a book stock is a counter
in the database, reflecting how many copies ara available at a moment.


Reviews
~~~~~~~

Reviews are assumed to be created by patrons and not pre-created / uploaded by
staff. I.e. reviews are considered a user-generated content. A review would
consist of a text and a 0 to 5 score.
