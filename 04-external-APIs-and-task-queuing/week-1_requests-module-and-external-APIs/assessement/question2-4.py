class MBSAuthor:
    # Question 2: Implement this class
    def __init__(self, name):
        self.name = name


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
        return list(map(MBSBook, self.data))