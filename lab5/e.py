import re
text = '/Users/rgalbekovaaltynai/Documents/GitHub/sem2/lab5/a.txt'
with open(text, "r") as file:
    string = file.read().strip()
pattern = "^a.*b$"
result = re.findall(pattern, string)
if result:
    print(result)
else:
    print("Not found") 