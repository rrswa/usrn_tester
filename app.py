import api

before_query = input("What is URL before the query? ")
after_query = input("What is the part after the query? (Optional) ")
letter_amount = int(input("How many letters does the username need to have? "))

while before_query is None:
    before_query = input("Please input the URL before the query: ")

api.test_usrn(before_query, after_query, letter_amount=5)
