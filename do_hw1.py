import requests
import datetime

num_paragraphs = int(input('Enter the number of paragraphs: '))
resp = requests.get(f'https://baconipsum.com/api?type=meat-and-filler&p={num_paragraphs}')
text = resp.text
paragraphs = text.split("\n")
paragraphs.reverse()

num_pancetta = 0
for paragraph in paragraphs:
    if 'pancetta' in paragraph:
        num_pancetta += 1

with open('output.txt', 'w') as file:
    file.write(f'Program executed by {input("Enter your name: ")} on {datetime.datetime.now()}\n')
    file.write(f'Number of paragraphs with "Pancetta": {num_pancetta}\n')
    file.write("\n".join(paragraphs))

print(f"Number of paragraphs with 'Pancetta': {num_pancetta}")
print("Paragraphs:")

for paragraph in paragraphs:
    print(paragraph)
