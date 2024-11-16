from django.db import models


# Create your models here.
class HeroSection(models.Model):
    title = models.CharField(max_length=200, default="eStartup")
    description = models.TextField(
        default="Transform your business ideas into reality. We provide all the tools and resources to help startups launch, grow, and thrive in today’s fast-paced digital world. Our platform is designed to streamline your journey from concept to market, making every step easy and efficient"
    )
    get_started_button_text = models.CharField(max_length=50, default="Get Started")
    get_started_button_url = models.CharField(max_length=200, default="#about")
    video_button_text = models.CharField(max_length=50, default="Watch Video")
    video_url = models.URLField(default="https://www.youtube.com/watch?v=Y7f98aduVJ8")
    hero_image = models.ImageField(upload_to="hero/", null=True, blank=True)

    def __str__(self):
        return self.title


class FeatureCard(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Icon class or name")

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    section_label = models.CharField(max_length=50, default="WHO WE ARE")
    title = models.CharField(
        max_length=200, default="Unleashing Potential with Creative Strategy"
    )
    description = models.TextField(
        default="At eStartup, we believe in transforming ideas into impact. Our team of experts brings together innovation and strategic thinking to help your business thrive in a competitive landscape."
    )
    list_item1_icon = models.CharField(max_length=50, default="fa-check-circle")
    list_item1_text = models.CharField(
        max_length=200, default="Tailored solutions for every business stage."
    )
    list_item2_icon = models.CharField(max_length=50, default="fa-check-circle")
    list_item2_text = models.CharField(
        max_length=200, default="Proven strategies to accelerate growth."
    )
    list_item3_icon = models.CharField(max_length=50, default="fa-check-circle")
    list_item3_text = models.CharField(
        max_length=200, default="Dedicated support from industry professional."
    )
    button_text = models.CharField(max_length=50, default="Read More")
    button_url = models.CharField(max_length=200, blank=True)
    button_icon = models.CharField(max_length=50, default="fa-arrow-right")
    main_image = models.ImageField(upload_to="about/", help_text="Main large image")
    top_right_image = models.ImageField(
        upload_to="about/", help_text="Top right small image"
    )
    bottom_right_image = models.ImageField(
        upload_to="about/", help_text="Bottom right small image"
    )

    def __str__(self):
        return self.title


class ServiceHeader(models.Model):
    label = models.CharField(max_length=50, default="Services")
    title1 = models.CharField(max_length=200, default="Our")
    title2 = models.CharField(max_length=200, default="Services")

    def __str__(self):
        return self.label


class ServiceCard(models.Model):
    service_icon = models.CharField(max_length=50, default="fa-check-circle")
    service_title = models.CharField(max_length=200)
    service_description = models.TextField()

    def __str__(self):
        return self.service_title


class Contact_Us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
