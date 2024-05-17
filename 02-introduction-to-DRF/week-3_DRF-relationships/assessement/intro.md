# Intro

In this exercise you’ll be testing what you’ve learned about authentication, permissions, related fields and nested relationships. A new Django project called module3 has been scaffolded for you, and some Django Rest Framework endpoints have already been set up. In this Project we have an app called bakery which represents a Bakery that does deliveries. The models are:

- `Food`: Represents a food item the bakery sells, which has a name and a cost.
- `Address`: A basic address class for a customer.
- `Customer`: Information about a customer, including a related Address.
- `Order`: An order for food that a customer has made. Has a related Customer and a list of food which are in the order.

API endpoints for list and detail for each of these models have been set up, at /api/v1/food, /api/v1/addresses, /api/v1/customers and /api/v1/orders, respectively. For simplicity no authentication is required for any of these endpoints.

Since there’s quite a lot of boilerplate code, the classes have been organized into separate files depending on what you need to edit. For example, not all serializers are in the same file. The ones that you will need to edit are inside bakery/api/serializers.py whereas the ones that you do not need to edit are in bakery/api/assessment_serializers.py. You do not need to edit any of the bakery/api/assessment_*.py files.

You’ll need to run the migrate management command to get set up, and there’s also a create_fixtures command that you can run to set up some testing data.
Like all our previous exercises you can run each test suite separately, e.g: python manage.py test bakery.tests_1.
