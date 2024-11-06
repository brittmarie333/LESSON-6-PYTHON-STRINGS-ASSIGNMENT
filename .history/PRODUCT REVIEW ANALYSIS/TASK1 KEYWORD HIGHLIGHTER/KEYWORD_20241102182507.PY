#Task 1: Keyword Highlighter
#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.


chosen_review = []

keywords = ["good", "excellent", "bad", "poor", "average"]

def review_keywords(reviews, keywords) :

    for review in reviews :
        for keyword in keywords
            if keyword.upper() in review.upper():
                chosen_review.append(review)


#So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."



first_string = ''