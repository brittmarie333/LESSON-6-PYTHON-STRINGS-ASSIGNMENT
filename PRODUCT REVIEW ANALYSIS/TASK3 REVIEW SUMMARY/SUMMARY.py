#Task 3: Review Summary
#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.
#Example: "This product is really good. I'm...",

statement = ("The device is really good; the performance of this product is excellent. Highly recommended! I had a bad experience with this product. It didn't meet my expectations.")
grammar = ("...")

script = statement[:30]

print(script)

summary = script + grammar

print(summary)