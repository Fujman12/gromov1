from django.db import models
import random
import string
from django.utils.safestring import mark_safe
from django.conf import settings
# Create your models here.


def generate_image_id(n=33):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


class Girl(models.Model):
    first_name = models.CharField("First name", max_length=256)
    last_name = models.CharField("Last name", max_length=256, blank=True, null=True)

    date_of_birth = models.DateField("Date of birth", blank=True, null=True)
    hair_color = models.CharField("Hair color", max_length=30, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    parameters = models.CharField("Parameters", max_length=20, blank=True, null=True)

    eye_color = models.CharField("Eye color", max_length=20, null=True)
    image_id = models.CharField("Image id", max_length=256, blank=False, null=False)

    def __str__(self):
        return "{} - Height: {}, parameters: {}".format(self.first_name, self.height, self.parameters)

    def save(self, *args, **kwargs):
        if not self.image_id:
            self.image_id = self.id

        super(Girl, self).save(*args, **kwargs)


def get_model_upload_path(instance, filename):

    return 'images/{0}/{1}'.format(instance.model.image_id, filename)


class ModelImage(models.Model):
    image = models.ImageField(upload_to=get_model_upload_path, null=True)
    model = models.ForeignKey('Girl', on_delete=models.CASCADE, related_name='images')

    # def image_tag(self):
    #     return mark_safe('<img src="%s" >' % (settings.MEDIA_URL + self.image.__str__()))
    #
    # image_tag.short_description = 'Image'
    #image_tag.allow_tags = True