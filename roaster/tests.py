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

    def test_get_number_of_beans(self):
        """Test the get_number_of_beans method."""
        # Initially, there should be no beans associated with the roaster
        self.assertEqual(self.roaster.get_number_of_beans(), 0)

        # Create a bean and associate it with the roaster
        from beans.models import Bean
        Bean.objects.create(
            name="Test Bean",
            roaster=self.roaster,
            roast_level=Bean.MEDIUM,
            origin_type=Bean.SINGLE_ORIGIN,
            origin="Test Origin",
            process=Bean.WASHED,
            producer="Test Producer",
            notes="Test Notes"
        )

        # Now, there should be one bean associated with the roaster
        self.assertEqual(self.roaster.get_number_of_beans(), 1)