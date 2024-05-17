# Integrating JavaScript and the React Framework: Question 4

## Question 4
A testing Django Rest Framework view has been set up at /api/v1/mock-post-detail/. This just returns a single static dictionary, that contains title and content items. This is so you can test retrieving an item that looks like a Post without requiring any in your database.
On the JavaScript side of things, the getMockPost() function has been created. Write the function body to use fetch() to retrieve the /api/v1/mock-post-detail/ endpoint. Then, decode the JSON from the response and output it to the console.


```javascript
// Question 4: Complete this function
function getMockPost () {
  fetch('/api/v1/mock-post-detail/').then(resp => resp.json()).then((data) => {
    console.log(data)
  })
}

//Question 4 end
```

- Create the getMockPost method.
- Fetch data from the given URL.
- Use a promise to convert the fetched data to JSON.
- Use another promise to log the data in JSON form.