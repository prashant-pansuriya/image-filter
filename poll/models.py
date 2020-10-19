from django.core.files.base import ContentFile
from django.db import models
from PIL import Image
import numpy as np
from .utils import get_filter_image
from io import BytesIO

# Create your models here.

CHOICES = (
    ('NO_FILTER','NO_FILTER'),
    ('COLORIZED', 'COLORIZE'),
    ('GRAYSCALE','GRAYSCALE'),
    ('BLURRED','BLURRED'),
    ('BINARY','BINARY'),
    ('INVERT','INVART'),
)

class Upload(models.Model):

    image = models.ImageField(upload_to="images/")
    action = models.CharField(max_length=10, choices= CHOICES, default='no_filter')
    update = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  str(self.id)

    def save(self, *args, **kwargs):
        # Image Open
        pil_image = Image.open(self.image)

        # image to array convert
        cv_image = np.array(pil_image)
        image = get_filter_image(cv_image, self.action)

        # array to pil convert
        pil_image = Image.fromarray(image)

        buffer = BytesIO()
        pil_image.save(buffer, format= "png")
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save= False)
        super(Upload, self).save()

class Post(models.Model):

    title = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
