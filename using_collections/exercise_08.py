# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# The former code extracts a slice from text, which it then treats like a new
# string. The latter code simply searches text between the specified indices.