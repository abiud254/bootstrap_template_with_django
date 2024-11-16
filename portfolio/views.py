from django.shortcuts import redirect, render

from .models import (
    AboutSection,
    Contact_Us,
    FeatureCard,
    HeroSection,
    ServiceCard,
    ServiceHeader,
)


# Create your views here.
def index(request):
    hero_section = HeroSection.objects.all()
    feature_cards = FeatureCard.objects.all()
    about_section = AboutSection.objects.all()
    service_header = ServiceHeader.objects.all()
    service_card = ServiceCard.objects.all()

    return render(
        request,
        "index.html",
        {
            "hero_section": hero_section,
            "feature_cards": feature_cards,
            "about_section": about_section,
            "service_header": service_header,
            "service_card": service_card,
        },
    )


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact_us = Contact_Us(
            name=name, email=email, subject=subject, message=message
        )
        contact_us.save()
        return redirect("/#contact")

    return render(request, "index.html")
