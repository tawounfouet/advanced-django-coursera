# Integrating JavaScript and the React Framework: Intro

## Intro
In these exercises, the project module4 carries on where module3 left off, on the Django side. You will be writing and testing JavaScript code so there are a few additions that have been set up to make this easier for you.
All the JavaScript code you will need to write is in a single file, assessment/static/assessment/main.js. There are a few lines of code that must be included in this file for it to be tested, and these are annotated, so don’t remove them. The portions of the file you need to edit are also clearly marked for each question.

The template index.html in assessment/templates/ has also been set up. This has 
the React and Babel scripts already included, as well as main.js. Included is a <script> tag that you can populate with code for testing. This file is not evaluated to check if the tests pass, so you can make any changes to it you like. The URL path / is routed to this template.
Since these are JavaScript tests, you won’t use Django to execute them. Instead you’ll use npm.
NPM

Before the tests can be run all the supporting packages need to be installed, which can be done with the npm install command that needs to be run inside the project directory. This reads a list of packages from the package.json file and installs them:
$ npm install

After the packages are installed, to run all the tests for the project, you can use the command npm test, like this:
$ npm test

Or, to run the commands for just one question, specify the path to the test file. For example:
$ npm test js_tests/question_5.test.js

Each test file is in the js_tests directory, and named like question_[1-5].test.js.