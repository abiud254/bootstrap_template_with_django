from django.contrib import admin

from .models import (
    AboutSection,
    Contact_Us,
    FeatureCard,
    HeroSection,
    ServiceCard,
    ServiceHeader,
)

# Register your models here.
admin.site.register(Contact_Us)
admin.site.register(HeroSection)
admin.site.register(FeatureCard)
admin.site.register(AboutSection)
admin.site.register(ServiceHeader)
admin.site.register(ServiceCard)
