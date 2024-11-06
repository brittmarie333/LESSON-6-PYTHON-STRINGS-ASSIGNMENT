#Task 2: Sentiment Tally
#Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
def pos_word_count(reviews, positive_words):
    pos_count = (0)
    for review in reviews:
        pos_count += positive_words.count(reviews, positive_words)
    return pos_count


def neg_word_count (reviews, negative_words):
  neg_count = 0
  for review in reviews:
    neg_count += negative_words.count(reviews, negative_words)
  return neg_count


positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]


for review in reviews:
   for word in positive_words:
      pos_word_count = reviews.count(positive_words)
print(pos_word_count)

for review in reviews:
   for word in negative_words:
      neg_word_count = reviews.count(negative_words)
print(pos_word_count)