# Python is good, Java is better" → Output: "Java is good, Python is better"

Words = "Python is good, Java is better"

print(Words.replace("Python", "TEMP").replace("Java", "Python").replace("TEMP", "Java"))
