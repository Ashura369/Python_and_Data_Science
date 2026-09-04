temp = ['a', 'e', 'i', 'o', 'u']

text = 'hello'
text2 = 'aeiou'

# checking for all the items 
ans = all(i in text for i in temp)
print(ans)

# checking if any of the items are available
ans2 = any(i in text for i in temp)
print(ans2)

# printing the items which are available
ans3 = set(temp) & set(text)                    # 'set()' automatically removes the duplicated items
print(list(ans3))


# using 'subset' -- checks if every element of text is inside temp
ans4 = set(text2).issubset(set(temp))
print(ans4)
