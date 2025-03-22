# WEEK 11 - TESTING, DEBUGGING, AND SDKS

# Challenge: Writing unit tests
# import unittest
#
# def add(x, y):
#     return x + y
#
# class TestAdd(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(2, 5), 7)
#
#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-2, -10), -12)
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# # Test fixtures
# import unittest
#
# class ExampleTestCase(unittest.TestCase):
#     def setUp(self):
#         self.x = 100
#         self.y = 50
#
#     def tearDown(self):
#         self.x = None
#         self.y = None
#
#     def test_addition(self):
#         result = self.x + self.y
#         self.assertEqual(result, 150)
#
#     def test_subtraction(self):
#         result = self.x - self.y
#         self.assertEqual(result, 50)
#
# if __name__ == '__main__':
#     unittest.main()

# Software Development Kits (SDKs)
# -----------------------------------------------
# Using boto3 with Amazon EC2
import boto3

# Create EC2 client object
ec2 = boto3.client('ec2')

# Retrieve information about instances
response = ec2.describe_instances()

# Get the list of instances
instances = response['Reservations'][0]['Instances']

# Loop over each instance
for instance in instances:

# Print instance ID
    print(instance['InstanceId'])

# ----------------------------------------------------
# Challenge: Using boto3 with Amazon S3
# Use Boto3 to print out the names of all of your Amazon S3 buckets.
import boto3

# Create S3 client object
s3 = boto3.client('s3')

# Retrieve information about buckets
response = s3.list_buckets()
print(response)

# Loop over each bucket and print its name
for bucket in response:
    print(f' {bucket["Name"]}')
