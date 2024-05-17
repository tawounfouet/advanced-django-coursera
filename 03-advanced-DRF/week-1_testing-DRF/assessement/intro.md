# Testing Django Rest Framework: Intro

## Intro
We’ve set up a Django project called module1 for the questions, with a single app, assessment. The app has been scaffolded with a Post model containing just three fields. All necessary API URLs have been set up with a viewset:
- /api/v1/token-auth/: To fetch a Django Rest Framework token for authentication
- /api/v1/posts/: The Post list view.
- /api/v1/posts/<pk>: The Post detail view.

In this coding exercise you’ll be setting up tests to test the API. The test methods have been written but you will be making sure the test classes are set up correctly.

Technically this was a difficult exercise to set up, since unit tests are being used to assess that your unit tests are written correctly. For this reason things behave a little differently.

Normally when writing Django unit tests, they would be in files starting with test_. If you examine the project, you’ll see, for example, the file assessment/tests_1.py This is the test to test your test is written correctly.

The tests you are editing are in the assessment/questions/ directory, with the files question_1.py through to question_5.py.

Running the tests is a little different. A new Django management command, test_assessment has been written to just run your tests. For example, to run all the tests in all the question_[1-5].py files, run the command:
```sh
$ python3 manage.py test_assessment
```

Or you can run individual test(s) by adding numbered arguments. For example, to run just the tests in question_2.py:
```sh
$ python3 manage.py test_assessment 2
```

Or to run the tests in question_1.py, question_3.py and question_5.py:
```sh
$ python3 manage.py test_assessment 1 3 5
```

To run the tests that assess your tests, use the normal Django management test command. Like in previous coding exercises, you can run all the tests by providing no argument after test:
```sh
$ python3 manage.py test
```

Or just the test(s) for a single question, by passing the module name:
```sh
$ python3 manage.py test assessment.tests_1
```

Each tests_[1-5].py and question_[1-5].py has had comments added so you know that you’re editing the right file.
With that rather long introduction, on to the questions.
