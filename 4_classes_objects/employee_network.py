#

class Employee:
    # class attribute to track current number of employees
    employee_count = 0

    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email, and hire date.
        Adjusts the employee_count class attribute when a new employee
            is created.
        """
        self.name = name
        self.email = email
        self.hire_date = hire_date
        self.post_history = []

        Employee.employee_count += 1

    def __str__(self):
        post_history_display = ""

        for post in self.post_history:
            #print(post)
            post_history_display +=(f"Posts:\n{post.message}\n"
                                    f"Author: {post.author}\n"
                                    f"\nComments:\n{''.join(str(comment) for comment in post.comments)}\n"
                                    f"------------------------------------------\n")

        return f"EMPLOYEE INFO\n" \
               f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Hire Date: {self.hire_date}\n\n" \
               f"{post_history_display}\n"

    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"Employee object repr {self.name}"

    def post_message(self, message):
        post = Post(message, self.name)
        self.post_history.append(post)
        return post

    def post_comment(self, comment, orig_post):
        comment = Comment(comment, self.name)
        orig_post.comments.append(comment)

class Post:
    post_id = 0

    def __init__(self, message, author):
        """
        Constructor method for Post class
        Initializes a Post object with message and author.
        """
        Post.post_id += 1
        self.post_id = Post.post_id

        self.message = message
        self.author = author
        self.comments = []

    def __str__(self):
        return f"Post Id: {self.post_id}\n" \
               f"Post: {self.message}\n" \
               f"Author: {self.author}\n" \
               f"Comments: {self.comments}\n" \
               f"---------------------------------"

    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"Post object repr {self.author} {self.message}"

    def edit_post(self, new_message):
        self.message = new_message

class Comment:
    comment_id = 0

    def __init__(self, comment, author):
        Comment.comment_id += 1
        self.comment_id = Comment.comment_id
        self.author = author
        self.comment = comment

    def __str__(self):
        return f"{self.comment}\n" \
               f"Author: {self.author}\n"

    def edit_comment(self, new_comment):
        self.comment = new_comment

######################################## TEST CODE ########################################

e1 = Employee("Robert Young", "ryoun3@gmail.com", "02-01-2025")
e2 = Employee("Ben Reid", "b_reid@yahoo.com", "03-15-2024")


post_1 = e1.post_message("Hello, I'm posting a message.")
e2.post_comment("I don't agree with that post.", post_1)
e1.post_comment("Well, that's just your opinion, man!", post_1)

print(e1)

