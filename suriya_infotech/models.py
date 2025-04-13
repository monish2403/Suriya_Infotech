from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    hard_disk = models.CharField(max_length=50)
    cpu_model = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    description = models.TextField()
    CATEGORY_CHOICES = [
            ('asus', 'Asus'),
            ('acer', 'Acer'),
            ('dell', 'Dell'),
            ('hp', 'HP'),
            ('lenovo', 'Lenovo'),
            ('samsung', 'Samsung'),
            ('apple', 'Apple')
        ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    

    def __str__(self):
        return self.name

class Desktop(models.Model):
    name = models.CharField(max_length=100)
    hard_disk = models.CharField(max_length=50)
    cpu_model = models.CharField(max_length=50)
    cpu_speed = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=50)
    memory_storage = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    description = models.TextField()
    CATEGORY_CHOICES = [
            ('asus', 'Asus'),
            ('acer', 'Acer'),
            ('dell', 'Dell'),
            ('hp', 'HP'),
            ('lenovo', 'Lenovo'),
            
        ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


    def __str__(self):
        return self.name