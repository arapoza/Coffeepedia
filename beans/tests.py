from django.test import TestCase

from .models import Bean
from roaster.models import Roaster
from cities_light.models import Country 

# Create your tests here.
class BeanModelTest(TestCase):
    """Test case for the Bean model."""

    def setUp(self):
        """Set up a Bean instance for testing."""
        self.bean = Bean.objects.create(
            name="Test Bean",
            roaster= Roaster.objects.create(name="Test Roaster", 
                                            country=Country.objects.create(name="Test Country"),
                                            website="http://testroaster.com"),
            roast_level=Bean.MEDIUM,
            origin_type=Bean.SINGLE_ORIGIN,
            origin="Ethiopia",
            process=Bean.WASHED,
            producer="Test Producer",
            notes="Test Notes"
        )

    def test_bean_str(self):
        """Test the string representation of the Bean model."""
        self.assertEqual(str(self.bean), "Name: Test Bean\nRoaster: Test Roaster")
