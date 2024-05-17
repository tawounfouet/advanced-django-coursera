// This next line is required for testing
if (typeof jest !== 'undefined') React = require('react')

    // Question 1: Set this variable and complete this function
    const userName = 'Rosco Bosco'
    
    function sayHello (name) {
      if (name === undefined)
        name = userName
      console.log('Hello, ' + name)
    }
    
    // Question 1 end
    
    
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
    
    
    // Question 4: Complete this function
    function getMockPost () {
      fetch('/api/v1/mock-post-detail/').then(resp => resp.json()).then((data) => {
        console.log(data)
      })
    }
    //Question 4 End
    
    // Question 5: Complete this component
    class PostDisplay extends React.Component {
      state = {
        post: null
      }
    
      componentDidMount () {
        fetch('/api/v1/mock-post-detail/').then(resp => resp.json()).then((data) => {
          this.setState({post: data})
        })
      }
    
      render () {
        if (this.state.post == null) {
          return <div>Loading...</div>
        }
        return <div>
          <h2>{this.state.post.title}</h2>
          <p>{this.state.post.content}</p>
        </div>
      }
    }
    
    //Question 5 end
    
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