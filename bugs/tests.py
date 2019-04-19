from django.test import TestCase
from .models import Bug

# Create your tests here.
class BugTest(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Bug models
    """
    
    def test_str(self):
        test_name = Bug(name='A bug')
        self. assertEqual(str(test_name), 'A bug')