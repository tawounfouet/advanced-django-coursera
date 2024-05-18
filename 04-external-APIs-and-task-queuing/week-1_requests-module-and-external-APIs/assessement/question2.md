# Requests Module and External APIs: Question 2

## Question 2:
We want MyBookStoreClient to return Python objects rather than raw decode JSON lists and dictionaries. This will make the responses easier for the client consumers to work with. For now, just implement the MBSAuthor class in my_book_store/client.py. It should take the name of the author as an argument to its constructor, which it will store on its name attribute, i.e:

```python
>>> author = MBSAuthor("Some Name")
>>> author.name
'Some Name'
```

## Task
```python
class MBSAuthor:
    # Question 2: Implement this class
    pass


class MBSBook:
    # Question 3: Implement this class
    pass


class MyBookStoreClient:
    data = [
        {
            "title": "Django: An Introduction",
            "isbn": "1234567891234",
            "author": "Aaron Aaronson",
        },
        {
            "title": "Django: Next Steps",
            "isbn": "9876432104321",
            "author": "Bob Bobson",
        },
        {
            "title": "Python: An Introduction",
            "isbn": "1112223334445",
            "author": "Charles Charleston",
        },
        {
            "title": "React: Learn It All",
            "isbn": "1223334444555",
            "author": "Aaron Aaronson",
        },
    ]

    def __init__(self, api_key):
        self.api_key = api_key

    def get_books(self):
        if self.api_key != "ABC123":
            raise ValueError("Incorrect API key.")

        # Question 4: Implement the rest of this method
```

## Solution
```python
class MBSAuthor:
    # Question 2: Implement this class
    def __init__(self, name):
        self.name = name
```
- Create the constructor that takes self and name as arguments
- Set the self.name attribute to name