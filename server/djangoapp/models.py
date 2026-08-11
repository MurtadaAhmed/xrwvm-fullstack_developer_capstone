# Uncomment the following imports before adding the Model code

# from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# 1. CarMake Model
class CarMake(models.Model):
    # CharField creates a standard VARCHAR text column in SQL
    name = models.CharField(max_length=100, unique=True, verbose_name="Make Name")
    # TextField creates a larger text box for longer paragraphs
    description = models.TextField(verbose_name="Description")
    
    # The __str__ method defines how this object represents itself as a string
    def __str__(self):
        return self.name


# 2. CarModel Model
class CarModel(models.Model):
    # ForeignKey sets up a Many-to-One relationship.
    # One CarMake (e.g., Toyota) can be linked to many CarModels (e.g., Camry, RAV4).
    # on_delete=models.CASCADE means if a Make is deleted, all its models are also deleted.
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, verbose_name="Car Make")
    
    # Dealer ID connects this car model to dealerships stored in your MongoDB database
    dealer_id = models.IntegerField(verbose_name="Dealer ID")
    
    name = models.CharField(max_length=100, verbose_name="Model Name")
    
    # Defining choices to limit model types in administrative forms
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
        ('Hatchback', 'Hatchback'),
        ('Convertible', 'Convertible'),
    ]
    type = models.CharField(
        max_length=20, 
        choices=CAR_TYPES, 
        default='Sedan',
        verbose_name="Vehicle Type"
    )
    
    # IntegerField with validators restricts years to realistic boundaries
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2026)
        ],
        verbose_name="Year"
    )

    def __str__(self):
        # Displays the brand alongside the specific model (e.g., "Toyota - Camry")
        return f"{self.car_make.name} - {self.name}"

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
