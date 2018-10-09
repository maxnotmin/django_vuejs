from django.test import TestCase
from .models import Bucketlist
# Create your tests here.

class ModelTestCase(TestCase):
    """
    This class will define the test case for the Test Model
    """
    def setUp(self):
        """
        define the test client and other test variable
        :return:
        """
        self.bucketlist_name = "The Bucketname"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """

        :return:
        """
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

