""" Implement a student library system using OOPs where students can borrow a book from the list of books.

Create a separate Library and Student class.

Your program must be menu-driven.

You are free to choose the methods and attributes of your choice to implement this functionality. """

'''
Need to have functions:

*************Library**************

student info verification
list of books------->string list
availability of each book----->list
add book to book list

**********************************



***********Student****************

Name
card number
start date of card
end date of card
borrowed date--------> date
due date-------------> date

**********************************
'''
import datetime
class library:
    def __init__(self,card_list,book_availability):
        self.card_list=list(range(1,101))  # assuming there are 100 cards issued
        self.book_availability=book_availability
        self.books_list=[] # doubt... will the list defined here be visible across all instances or will the books list defined for an object be limited to that itself
    
    def verify(self,card_no,start_date,end_date):
        current_date = datetime.date.today()
        if card_no not in self.card_list:
            print("Card Nmber Invalid, please bring a valid library card")
        elif not(start_date <= current_date <= end_date):
            if start_date > current_date:
                print("card status not yet activated")
            elif current_date > end_date:
                print("card_expired")
        else:
            print("card valid")
            validity_status=True
            
    
            
            
        
        
            
            
            