# Requests Module and External APIs: Question 4

## Question 4:
Finish the MyBookStoreClient.get_books() method so that it returns a list of MBSBook instances, one for each of the raw book dictionaries in the data attribute.


## Solution
```python
    def get_books(self):
        if self.api_key != "ABC123":
            raise ValueError("Incorrect API key.")

        # Question 4: Implement the rest of this method
        return list(map(MBSBook, self.data))
```

- Solution uses the map function so that each dictionary is passed to the constructor for the MBSBook class.
- The list function returns a list of MBSBook objects.