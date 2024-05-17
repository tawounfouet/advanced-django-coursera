# Question 3
A
 React component called ClickOnceButton has been partially set up. It should render a <button> with Bootstrap classes (btn and btn-primary) that has the text Click Me!. Once the button has been clicked, the text should change to Clicked! and the button should become disabled, by setting its disabled property to true. You will need to set up some state to store this information, and add a click handler.
This component has been set up to be rendered into the <div> with id="question3-root" on the testing page, under the text Question 3 component is rendered below. You do not need to implement the ReactDOM.render() calls as this has been done.


```javascript
// Question 3: Complete this component
class ClickOnceButton extends React.Component {
  state = {
    wasClicked: false
  }

  handleClick () {
    this.setState({wasClicked: true})
  }

  render () {
    return <button
      className="btn btn-primary"
      onClick={() => {this.handleClick()}}
      disabled={this.state.wasClicked}>
      {this.state.wasClicked ? 'Clicked!' : 'Click Me'}
    </button>
  }
}

// Question 3 End
```

- Create the class ClickOnceButton which creates a React component.
- Set the initial state of wasClicked to false.
- You need a handleClick method that sets wasClicked to true.
- The render method should return a <button>.
- Set the CSS to "btn btn-primary".
- On a click, call the handleClick method.
- Disable the button after it has been clicked.
- The text (handled with a ternary operator) should be 'Click Me' if not clicked and 'Clicked!' once clicked.