    # Employee class
class Employee:
    # class attribute to track current number of employees
    employee_count = 0
    
    
    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email, hire date.
        Increments the employee_count class attribute when a new employee 
            is created. 
        Initializes posts list and comments list.
        Initializes a total_score variable to track usage/points
        """
        
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        
        self.total_score = 0
        self.posts = [] # Initializes an empty list to hold all posts
        self.comments = [] # Initializes an empty list to hold all comments
        
    def post_message(self, message):
        """
        Method to create a new post by the Employee
        Creates a new Post object with a message and the Employee
            as the author
        Appends the Post object to the Employees list of posts.
        """
        post = Post(self, message)
        self.total_score += 5
        self.posts.append(post)
        return post
    
    def comment_on_post(self, message, post, points=1):
        """
        Method to create a new comment on a post 
        Creates a new Comment object with a message, Employee as author, and
            the given post
        Appends the comment object to the author Employee's comment list and 
            the list of comments on the post. 
        
        """
        comment = Comment(self, message, post)
        self.total_score += points
        post.comments.append(comment) # appends comment to the post object
        self.comments.append(comment) # appends comment to the Employee object
        return comment
        
    def like_post(self, post, points=1):
        """
        Method to create a new comment on a post
        Creates a new Like object with an Employee as author and the orig post
        
        """
        like = Like(self, post)
        self.total_score += points
        post.likes.append(self)
        
    def __str__(self):
        """
        Method that returns a string describing the object
        """
        return f"Employee: {self.name}\nHire date:{self.hire_date}"
        
    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"Employee object repr {self.name}"
    
class Engineer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "engineering"

    def comment_on_post(self, message, post):
        if post.author.department == "engineering":
            points = 1
        else:
            points = 5
        return super().comment_on_post(message, post, points)

    def __str__(self):
        """
        Method that returns a string describing the object
        """
        return f"Engineer: {self.name}\nHire date:{self.hire_date}"
        
    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"Engineer object repr {self.name}"
        
class Marketer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "marketing"

    def comment_on_post(self, message, post):
        if post.author.department == "marketing":
            points = 1
        else:
            points = 5
        return super().comment_on_post(message, post, points)

    def __str__(self):
        """
        Method that returns a string describing the object
        """
        return f"Marketer: {self.name}\nHire date:{self.hire_date}"
        
    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"Marketer object repr {self.name}"
        
class DataScientist(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "data_science"
    
    def comment_on_post(self, message, post):
        if post.author.department == "data_science":
            points = 1
        else:
            points = 5
        return super().comment_on_post(message, post, points)
    def __str__(self):
        """
        Method that returns a string describing the object
        """
        return f"DataScientist: {self.name}\nHire date:{self.hire_date}"
        
    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"DataScientist object repr {self.name}"
        


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
        self.likes = []
        
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
        
# Like class
class Like:
    def __init__(self, author, post):
        self.author = author
        self.post = post
    def unlike(self, post):
        self.post.likes.remove(self)
        
"""
Try out methods and attributes
"""
# create a new Employees: Engineers, Marketers, and DataScientists
eng1 = Engineer("Mary Major", "mary.major@example.com", "07/12/2021")
eng2 = Engineer("Pat Candella", "pat.candella@example.com", "12/1/2022")
mar1 = Marketer("Jorge Souza", "jorge.souza@example.com", "08/10/2020")
ds1 = DataScientist("Arnav Desai", "arnav.desai@example.com", "03/14/15")

# test post, comment, like functionality
p1 = eng1.post_message("message")
eng2.comment_on_post("eng2 comment", p1)
mar1.comment_on_post("mar 1 comment", p1)
ds1.like_post(p1)

print ("Total employee count =", Employee.employee_count) # Expected 4
print ("Mary's posts are",[post.message for post in eng1.posts])
print ("Mary's comments are",[comment.message for comment in eng1.comments])
print ("Pat's comments are",[comment.message for comment in eng2.comments])
print ("The likes on post p1 come from", [like.name for like in p1.likes])

print (eng1.total_score) # Expected 5
print (eng2.total_score)  # Expected 1
print (mar1.total_score) # Expected 5
print (ds1.total_score) # Expected 1







