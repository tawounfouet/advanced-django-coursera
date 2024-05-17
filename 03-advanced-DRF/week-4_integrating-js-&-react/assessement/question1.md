# Question 1
In main.js, implement the function body and parameters for the sayHello function. The function should accept a single argument, the name of the person to say hello to. It should log to the console the message Hello, .

For example, if called like this:
```javascript
sayHello('Leo')
```
The text Hello, Leo would be output to the console.

Above the function definition that was created for you, is the constant userName. Set this to any name you like. If sayHello() is called with no arguments, it should use the name you set instead. For example, if userName is set to Barnaby:
```javascript
const userName = `Barnaby`
```
Then calling `sayHello()` without arguments will output Hello, Barnaby.

You can set userName to anything you like, the automated tests will still pass.

Remember you can add code inside the last <script type="text/babel"> element inside index.html to test the function.


## Task
```javascript
// This next line is required for testing
if (typeof jest !== 'undefined') React = require('react')

// Question 1: Set this variable and complete this function
const userName = ''

function sayHello () {
}

// Question 1 End

// Question 2: Complete this class
class PostReadCounter {
}

// Question 2 End

// Question 3: Complete this component
class ClickOnceButton extends React.Component {

  render () {
    // Remove this placeholder return and implement the function
    return null
  }
}

// Question 3 End

// Question 4: Complete this function
function getMockPost () {
}

//Question 4 End

// Question 5: Complete this component
class PostDisplay extends React.Component {

  render () {
    // Remove this placeholder return and implement the function
    return null
  }
}

//Question 5 End

// Do not change anything below, these are required for testing

if (typeof jest === 'undefined') {
  const q3DomContainer = document.getElementById('question3-root')
  ReactDOM.render(
    React.createElement(
      ClickOnceButton,
    ),
    q3DomContainer
  )

  const q5DomContainer = document.getElementById('question5-root')
  ReactDOM.render(
    React.createElement(
      PostDisplay,
    ),
    q5DomContainer
  )
} else {
  module.exports = {
    userName,
    sayHello,
    PostReadCounter,
    ClickOnceButton,
    getMockPost,
    PostDisplay
  }
}
```


## Solution
```javascript
// Question 1: Set this variable and complete this function
const userName = 'Rosco Bosco'

function sayHello (name) {
  if (name === undefined)
    name = userName
  console.log('Hello, ' + name)
}

// Question 1 end
```
- Provide a value for the userName variable
- Declare the sayHello function with the parameter name
- If name does not have a value, set name to userName
- Log Hello, concatenated with name