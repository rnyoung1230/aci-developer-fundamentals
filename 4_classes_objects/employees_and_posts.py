# Employee class
class Employee:
    # class attribute to track current number of employees
    employee_count = 0
    
    
    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email, and hire date. 
        Increments the employee_count class attribute when a new employee 
            is created. 
        """
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        
        self.posts = [] # Initializes an empty list to hold all posts
        
    def post_message(self, message):
        """
        Method to create a new post by the Employee
        Creates a new Post object with a message and the Employee as the author
        Appends the Post object to the Employees list of posts.
        """
        post = Post(self, message)
        self.posts.append(post)
        return post

    
# Post class 
class Post:
    def __init__(self, author, message):
        """
        Constructor method for the Post class
        Initializes a Post object with message and author Employee
        Initializes and empty list to hold comments on the post
        """
        self.message = message
        self.author = author
        self.comments = []
        
    def edit_message(self, new_message):
        """
        Method to edit the message in the post
        Updates the message attribute of the Post object
        """
        self.message = new_message


"""
Try out methods and attributes
"""
# create a new employee
e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")

# Use the post message method to create new Post objects
e1.post_message("hello")

# Capture the function return in a variable so you can reference the Post
second_post = e1.post_message("second message")

# Use the edit message method from the Post class to edit the message
second_post.edit_message("edited message")

# Check post to see that it includes the Employee as author
print (second_post.author.name)

# Use a list comprehension to print each message on the Employee's posts list. 
print ([post.message for post in e1.posts])

