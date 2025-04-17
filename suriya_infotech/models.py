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
    main_image = models.ImageField(upload_to='images/laptop/')
    image1 = models.ImageField(upload_to='images/laptop/')
    image2 = models.ImageField(upload_to='images/laptop/')
    image3 = models.ImageField(upload_to='images/laptop/')
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
    main_image = models.ImageField(upload_to='images/desktop/')
    image1 = models.ImageField(upload_to='images/desktop/')
    image2 = models.ImageField(upload_to='images/desktop/')
    image3 = models.ImageField(upload_to='images/desktop/')
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

class Refurbished_Laptop(models.Model):
    name = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    hard_disk = models.CharField(max_length=50)
    cpu_model = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to='images/refurbished_laptop/')
    image1 = models.ImageField(upload_to='images/refurbished_laptop/')
    image2 = models.ImageField(upload_to='images/refurbished_laptop/')
    image3 = models.ImageField(upload_to='images/refurbished_laptop/')
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

class Refurbished_Desktop(models.Model):
    name = models.CharField(max_length=100)
    hard_disk = models.CharField(max_length=50)
    cpu_model = models.CharField(max_length=50)
    cpu_speed = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=50)
    memory_storage = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to='images/refurbished_desktop/')
    image1 = models.ImageField(upload_to='images/refurbished_desktop/')
    image2 = models.ImageField(upload_to='images/refurbished_desktop/')
    image3 = models.ImageField(upload_to='images/refurbished_desktop/')
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

class Ink_printer(models.Model):
    Brands_Category = [
        ('epson', 'Epson'),
        ('canon', 'Canon'),
        ('brother', 'Brother'),
        ('hp', 'HP'),
        ]
    name = models.CharField(max_length=100)
    brands = models.CharField(max_length=50, choices=Brands_Category)
    connectivity = models.CharField(max_length=50)
    printing_technology = models.CharField(max_length=50)
    special_features = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    print_speed = models.CharField(max_length=50)
    item_weight = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to='images/ink_printer/')
    image1 = models.ImageField(upload_to='images/ink_printer/')
    image2 = models.ImageField(upload_to='images/ink_printer/')
    image3 = models.ImageField(upload_to='images/ink_printer/')
    description = models.TextField()

    def __str__(self):
        return self.brands

class Laser_Jet_printer(models.Model):
    Brands_category = [
        ('canon', 'Canon'),
        ('brother', 'Brother'),
        ('hp', 'HP'),
        ]
    brands = models.CharField(max_length=50, choices=Brands_category)
    connectivity = models.CharField(max_length=50)
    Special_features = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    printer_output = models.CharField(max_length=50)
    item_weight = models.CharField(max_length=50)
    max_speed = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to='images/laser_printer/')
    image1 = models.ImageField(upload_to='images/laser_printer/')
    image2 = models.ImageField(upload_to='images/laser_printer/')
    image3 = models.ImageField(upload_to='images/laser_printer/')
    description = models.TextField()

    def __str__(self):
        return self.brands

class Thermal_printer(models.Model):
    Brands_category = [
        ('rugtek', 'Rugtek'),
        ('tvs', 'TVS'),
    ]
    name=models.CharField(max_length=100)
    brands = models.CharField(max_length=50, choices=Brands_category)
    connectivity = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    special_features = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    printer_output = models.CharField(max_length=50)
    print_speed = models.CharField(max_length=50)
    item_weight = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to='images/thermal_printer/')
    image1 = models.ImageField(upload_to='images/thermal_printer/') 
    image2 = models.ImageField(upload_to='images/thermal_printer/')
    image3 = models.ImageField(upload_to='images/thermal_printer/')
    description = models.TextField()

    def __str__(self):
        return self.brands

    
    