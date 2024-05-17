# Integrating JavaScript and the React Framework: Question 2

## Question 2
The class PostReadCounter has been defined but needs to be completed. It just holds a count of the number of times a post has been read. Note that this is a mock class and doesn’t interact with the real Post model at all. The class’s constructor should accept a single argument, the post’s title, as a string. The read count of the post should start at 0, and be incremented every time the PostReadCounter's read() method is called. The class should also implement a getDescription() method that returns a string like <title> was read 2 times. Pluralization of time is important! Finally, the class should also have an outputDescription() method that outputs the return value of getDescription() to the console.

### To summarize:
- add a constructor that accepts a string.
- read() increments a read count that starts at 0.
- getDescription() returns a string in the format <title> was read <n> times.
- outputDescription() prints the return value from getDescription() to the console.

Here’s an example of how it will be used:
```javascript
const prc = PostReadCounter('My Post')
prc.getDescription()  // Returns 'My Post was read 0 times'
prc.read()
prc.getDescription()  // Returns 'My Post was read 1 time'
prc.read()
prc.outputDescription() // 'My Post was read 2 times' is output to the console
```
```

```sh
Add code to the 
<script type="text/babel"> element inside index.html if you want to test the code in a browser.
```




```javascript
// Question 2: Complete this class
class PostReadCounter {
  readCount = 0

  constructor (title) {
    this.title = title
  }

  read () {
    this.readCount += 1
  }

  getDescription () {
    return this.title + ' was read ' + this.readCount + ' time' + (this.readCount !== 1 ? 's' : '')
  }

  outputDescription () {
    console.log(this.getDescription())
  }
}

// Question 2 End
```

- Provide a value for the userName variable
- Declare the sayHello function with the parameter name
- If name does not have a value, set name to userName
- Log Hello, concatenated with name