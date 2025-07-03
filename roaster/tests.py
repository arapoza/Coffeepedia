from django.test import TestCase

from cities_light.models import Country
from .models import Roaster

# Create your tests here.
class RoasterModelTest(TestCase):
    """Test case for the Roaster model."""

    def setUp(self):
        """Set up a Roaster instance for testing."""
        self.roaster = Roaster.objects.create(
            name="Test Roaster",
            country=Country.objects.create(name="Test Country"),
            website="http://testroaster.com"
        )

    def test_roaster_str(self):
        """Test the string representation of the Roaster model."""
        self.assertEqual(str(self.roaster), "Test Roaster")