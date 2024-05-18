# Requests Module and External APIs: Question 3

## Question 3:
Carrying on from Question 2, implement the MBSBook class. Its constructor should take a book dictionary as an argument (refer to MyBookStoreClient for the format). It should implement three properties:
title: return the book title.
isbn: return the book ISBN.
author: return an MBSAuthor instance constructed with the author name.


## Solution

```python
class MBSBook:
    # Question 3: Implement this class
    def __init__(self, data):
        self.data = data

    @property
    def title(self):
        return self.data["title"]

    @property
    def isbn(self):
        return self.data["isbn"]

    @property
    def author(self):
        return MBSAuthor(self.data["author"])
```

- Create the constructor that takes self and data as arguments.
- Set self.data to data.
- Use the @property decorator for title property. Return the value of the title key.
- Use the @property decorator for isbn property. Return the value of the isbn key.
- Use the @property decorator for author property. Return the value of the author key.