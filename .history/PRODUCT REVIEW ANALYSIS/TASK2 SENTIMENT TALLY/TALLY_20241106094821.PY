#Task 2: Sentiment Tally
#Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
def count_positive_words(reviews, positive_words):
  total_count = ('positive_words)
  for review in reviews:
    total_count += positive_words.count(reviews, positive_words)
  return total_count


positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

for word in positive_words:
    for review in reviews:
       count_positive_words('positive_words')
    print(total_count)


