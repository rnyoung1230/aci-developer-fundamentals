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
        self.comments = [] # Initializes an empty list to hold all comments
        
    def post_message(self, message):
        """
        Method to create a new post by the Employee
        Creates a new Post object with a message and the Employee as the author
        Appends the Post object to the Employees list of posts.
        """
        post = Post(self, message)
        self.posts.append(post)
        return post
    
    def comment_on_post(self, message, post):
        """
        Method to create a new comment on a post 
        Creates a new Comment object with a message, Employee as author, and
            the given post
        Appends the comment object to the author Employee's comment list and 
            the list of comments on the post. 
        """
        comment = Comment(self, message, post)
        post.comments.append(comment) #appends comment to the post object
        self.comments.append(comment) # appends comment to the Employee object
        return comment
    
# Post class 
class Post:
    def __init__(self, author, message):
        """
        Constructor method for the Post class
        Initializes a Post object with message and author Employee
        Initializes and empty list to hold comments on the post
        """
        self.author = author
        self.message = message
        self.comments = []
        
    def edit_message(self, new_message):
        """
        Method to edit the message in the post
        Updates the message attribute of the Post object
        """
        self.message = new_message

# Comment class
class Comment:
    def __init__(self, author, message, post):
        """
        Constructor method for Comment class
        Initializes a Comment object with an author Employee, a message, and a
            Post object
        """
        self.author = author
        self.message = message
        self.post = post

    def edit_message(self, new_message):
        """
        Method to edit the message of a comment
        Updates the message attribute of the comment object
        """
        self.message = new_message
        


        
"""
Try out methods and attributes
"""
# create a new employee
e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")
e2 = Employee("Pat Candella", "pat.candella@example.com", "12/1/2022")

# Use the post message method to create new Post objects
intro_message = e2.post_message("Hi all! So excited to be joining the company!")

# Use the returned post to comment on the message
e1.comment_on_post("Welcome to the team!", intro_message)
e2.comment_on_post("Thanks!", intro_message)


# Another example of a new post with comment exchange
workshop_post = e1.post_message("I just attended a workshop.")

e2.comment_on_post("Cool! What was the workshop about?", workshop_post)
e1.comment_on_post("Python classes and objects", workshop_post)

print ("Mary's posts are",[post.message for post in e1.posts])
print ("Pat's posts are", [post.message for post in e2.posts])

print ("-" * 50)

print ("Mary's comments are",[comment.message for comment in e1.comments])
print ("Pat's comments are",[comment.message for comment in e2.comments])

print ("-" * 50)

print ("Intro message comments are",[comment.message for comment in intro_message.comments])
print ("Workshop post comments are", [comment.message for comment in workshop_post.comments])



