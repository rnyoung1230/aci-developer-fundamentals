#
class Employee:
    # class attribute to uniquely identify employees
    employee_id = 0

    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        """
        self.employee_id = Employee.get_employee_id()
        self.name = name
        self.email = email
        self.hire_date = hire_date
        self.posts = []

    def __str__(self):
        return f"EMPLOYEE INFO\n" \
               f"Employee Id: {self.employee_id}\n" \
               f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Hire Date: {self.hire_date}\n"

    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"Employee object repr {self.name}"

    @classmethod
    def get_employee_id(cls):
        cls.employee_id += 1
        return cls.employee_id

    def post_message(self, message):
        post = Post(message, self.name)
        self.posts.append(post)
        return post

    def post_comment(self, comment, post):
        comment = Comment(comment, self.name)
        post.comments.append(comment)

    def print_info(self, include_posts=False):
        if include_posts:
            posts_display = ""

            for post in self.posts:
                posts_display +=(f"{str(post)}\n"
                                 f"\nComments\n{''.join(str(comment) for comment in post.comments)}"
                                 f"------------------------------------------\n")

            print(f"{self}\nPOSTS\n{posts_display}")
        else:
            print(self)

class Engineer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "Engineering"

    def __str__(self):
        return super().__str__() + f"Department: {self.department}\n"

class Marketer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "Marketing"

    def __str__(self):
        return super().__str__() + f"Department: {self.department}\n"

class Post:
    post_id = 0

    def __init__(self, message, author):
        """
        Constructor method for Post class
        """
        self.post_id = Post.get_post_id()
        self.message = message
        self.author = author
        self.comments = []

    def __str__(self):
        return f"Post Id: {self.post_id}\n" \
               f"{self.author}: " \
               f"{self.message}"

    def __repr__(self):
        """
        Method that returns identifying information on the object
        """
        return f"Post object repr {self.author} {self.message}"

    @classmethod
    def get_post_id(cls):
        cls.post_id += 1
        return cls.post_id

    def edit_post(self, message):
        self.message = message

class Comment:
    comment_id = 0

    def __init__(self, comment, author):
        self.comment_id = Comment.get_comment_id()
        self.author = author
        self.comment = comment

    def __str__(self):
        return f"{self.author}: {self.comment}\n"

    @classmethod
    def get_comment_id(cls):
        cls.comment_id += 1
        return cls.comment_id

    def edit_comment(self, comment):
        self.comment = comment

######################################## TEST CODE ########################################

e1 = Employee("Robert Young", "ryoun3@gmail.com", "02-01-2025")
e2 = Employee("Ben Reid", "b_reid@yahoo.com", "03-15-2024")


post_1 = e1.post_message("Hello, I'm posting a message.")
e2.post_comment("I don't agree with that post.", post_1)
e1.post_comment("Well, that's just your opinion, man!", post_1)

post_2 = e1.post_message("It's so great to be working at this company!")
e2.post_comment("I couldn't agree with you more, Robert.", post_2)

e1.print_info(include_posts=True)
e2.print_info()

engineer_emp = Engineer("Ken O'Rourke", "korourke@gmail.com", "12-10-2024")
print(engineer_emp)

marketer_emp = Marketer("Jennifer Smith", "jennifer_smith@gmail.com", "09-07-2023")
post_3 = marketer_emp.post_message("Hello, my name is Jen. I'm new to the Marketing team.")
engineer_emp.post_comment("Nice to meet you Jen. I'm Ken.", post_3)
marketer_emp.post_comment("Hi Ken. Let's do lunch sometime!", post_3)
print(marketer_emp)
marketer_emp.print_info(include_posts=True)