# epath

This package provides easy and dynamic way to import parent files in Python.  

Sample folder structure can be seen below.  

``` 
--main_folder

--app.py

  --folder_1

    --sample.txt

  --folder_2

    --target.py
``` 
Here, it is desired to read the sample.txt file from the target.py file. Then it will be used by calling the say_hello and say_goodBye functions in the app.py file.  

app.py
``` 
def say_hello():
  print("Hello")

def say_goodBye():
  print("GoodBye")
``` 

sample.txt
```
This is a sample.txt 
```

target.py
```
from epath import Path

pt = Path()
txt_path = pt.get("/../folder_1/sample.txt")
with open(txt_path) as f:
    lines = f.readlines()

print(lines)
>>>['This is a sample.txt ']

#----------------------------------
app = pt.importer("/../app")
app.say_hello()
>>>Hello

app.say_goodBye()
>>>GoodBye

```