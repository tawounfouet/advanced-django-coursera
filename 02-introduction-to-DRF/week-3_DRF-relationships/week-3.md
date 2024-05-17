# Week 3 : Django Rest Framework Relationship

Welcome to Week 3 of the Advanced Django: Introduction to Django Rest Framework course. These assignments cover authentication, permissions, related fields, and nested relationships. The module ends with graded coding exercises.

## Learning Objectives
- Explain the importance of authentication
- Define session authentication
- Add session authentication to Blango
- Contrast basic authentication from session authentication
- Authenticate with Postman, your username, and your password
- Identify the benefits of token authentication
- Add token authentication to Blango
- Define the purpose of permissions
- Identify some common permissions
- Update Blango so only authenticated users can make changes
- Use custom permissions to restrict access to objects
- Combine permissions so that only the author or admin users can make changes
- Identify the benefits from having related fields
- Define PrimaryKeyRelatedField, StringRelatedField, SlugRelatedField, and HyperlinkRelatedField
- Add a SlugRelatedField for tags to the PostSerializer class
- Add a HyperlinkRelatedField for the author to the PostSerializer class
- Define a read-only nested relationship
- Define a read-write nested relationship
- Implement an update method to avoid a race condition
- Use the get_or_create method to automatically create related objects
- Modify Blango to create and see comments through the API
- Modify Blango to create tags through the API