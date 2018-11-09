from django.contrib import admin
from girls.models import Girl, ModelImage
from django.utils.safestring import mark_safe

class ModelImageAdmin(admin.ModelAdmin):
    #fields = ['image_tag',]
    #readonly_fields = ['image_tag',]

    readonly_fields = ["headshot_image", 'model']

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=obj.image.width,
                height=obj.image.height,
            )
        )

class ModelImageInline(admin.StackedInline):
    model = ModelImage
    #fields = ['headshot_image',]
    readonly_fields = ['headshot_image']

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=obj.image.width,
                height=obj.image.height,
            )
        )

class GirlAdmin(admin.ModelAdmin):
    model = Girl
    inlines = [ModelImageInline]

admin.site.register(ModelImage, ModelImageAdmin)
admin.site.register(Girl, GirlAdmin)

