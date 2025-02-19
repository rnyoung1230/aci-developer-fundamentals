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
        self.total_score = 0

    def __str__(self):
        return f"EMPLOYEE INFO\n" \
               f"Employee Id: {self.employee_id}\n" \
               f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Hire Date: {self.hire_date}\n" \
               f"Social Networking Score: {self.total_score}\n"

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
        post = Post(self, message)
        self.total_score += 5
        self.posts.append(post)
        return post

    def post_comment(self, comment, post, points=1):
        comment = Comment(self, comment, post)
        self.total_score += points
        post.comments.append(comment)
        return comment

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

    def post_comment(self, comment, post, points=0):
        if post.author.department == "Engineering":
            points = 1
        else:
            points = 5

        super().post_comment(comment, post, points)

class Marketer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = "Marketing"

    def __str__(self):
        return super().__str__() + f"Department: {self.department}\n"

    def post_comment(self, comment, post, points=0):
        if post.author.department == "Marketing":
            points = 1
        else:
            points = 5

        super().post_comment(comment, post, points)

class Post:
    post_id = 0

    def __init__(self, author, message):
        """
        Constructor method for Post class
        """
        self.post_id = Post.get_post_id()
        self.message = message
        self.author = author
        self.comments = []

    def __str__(self):
        return f"Post Id: {self.post_id}\n" \
               f"{self.author.name}: " \
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

    def __init__(self, author, comment, post):
        self.comment_id = Comment.get_comment_id()
        self.author = author
        self.comment = comment
        self.post = post

    def __str__(self):
        return f"{self.author.name}: {self.comment}\n"

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
marketer_emp = Marketer("Jennifer Smith", "jennifer_smith@gmail.com", "09-07-2023")

post_3 = marketer_emp.post_message("Hello, my name is Jen. I'm new to the Marketing team.")
engineer_emp.post_comment("Nice to meet you Jen. I'm Ken.", post_3)
marketer_emp.post_comment("Hi Ken. Let's do lunch sometime!", post_3)

engineer_emp.print_info()
marketer_emp.print_info(include_posts=True)