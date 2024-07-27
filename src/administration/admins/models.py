from django.db import models
from tinymce.models import HTMLField


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class PropertyTag(models.Model):
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class PropertyFeature(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Property(models.Model):
    STATUS_CHOICE = (
        ('o', 'Open'),
        ('c', 'Close'),
    )

    image = models.ImageField(upload_to='property/images/', null=True, blank=False)

    name = models.CharField(max_length=255)
    price_start = models.PositiveIntegerField(default=0)
    price_end = models.PositiveIntegerField(default=0)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, blank=False)
    property_id = models.CharField(max_length=255, null=True, blank=True)
    content = HTMLField()

    address = models.CharField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=False)
    lat = models.FloatField(null=True, blank=False)
    long = models.FloatField(null=True, blank=False)
    slug = models.SlugField(unique=True)

    youtube_video_id = models.CharField(
        max_length=100, null=True, blank=True,
        help_text="Don't place video links here use youtube Id like "
    )

    price_list_file = models.FileField(upload_to='property/files/price_lists/', null=True, blank=True, help_text="Make sure to upload pdf file.")
    floor_map_file = models.FileField(upload_to='property/files/floor_maps/', null=True, blank=True, help_text="Make sure to upload pdf file.")

    tags = models.ManyToManyField(PropertyTag)
    features = models.ManyToManyField(PropertyFeature)

    floor_payment_image = models.ImageField(upload_to='property/images/floor_payment_plans/', null=True, blank=True)
    floor_payment_file = models.ImageField(upload_to='property/images/floor_payment_files/', null=True, blank=True)
    floor_payment_description = models.TextField(null=True, blank=True)

    floor_design_image = models.ImageField(upload_to='property/images/floor_payment_plans/', null=True, blank=True)
    floor_design_file = models.ImageField(upload_to='property/images/floor_payment_files/', null=True, blank=True)
    floor_design_description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name

    def get_images(self):
        return PropertyImage.objects.filter(property=self)

    def get_videos(self):
        return PropertyVideo.objects.filter(property=self)

    def get_floor_plans(self):
        return PropertyFloorPlan.objects.filter(property=self)

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        self.price_list_file.delete(save=True)
        self.floor_map_file.delete(save=True)
        super(Property, self).delete(*args, **kwargs)


class PropertyFloorPlan(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    size_start = models.FloatField(default=0, help_text="Size in sq.ft")
    size_end = models.FloatField(default=0, help_text="Size in sq.ft")
    price_start = models.FloatField(default=0, help_text="Price in Pakistani Rupees")
    price_end = models.FloatField(default=0, help_text="Price in Pakistani Rupees")
    bed_rooms = models.PositiveIntegerField(default=1)
    bath_rooms = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="property/images/floor_plans/images/", null=True, blank=True)
    file = models.ImageField(upload_to="property/images/floor_plans/files/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['property', 'bed_rooms']

    def __str__(self):
        return self.property.name


class PropertyImage(models.Model):
    image = models.ImageField(upload_to='property/images/')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.property.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(PropertyImage, self).delete(*args, **kwargs)


class PropertyVideo(models.Model):
    youtube_video_id = models.CharField(
        max_length=100, null=True, blank=True,
        help_text="Don't place video links here use youtube Id like "
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.property.name


