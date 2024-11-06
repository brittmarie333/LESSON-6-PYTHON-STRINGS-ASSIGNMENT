#Task 2: Sentiment Tally
#Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

for postive_word in keywords:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    print(review)