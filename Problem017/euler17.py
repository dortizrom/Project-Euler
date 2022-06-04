
from num2words import num2words

full_text=""
for i in range(1,1001):
    full_text += num2words(i)

full_text = full_text.replace(" ", "").replace("-","")
print(len(full_text))
