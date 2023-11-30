from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Subscription
from app_gen.froms import SubscriptionFrom , SubscritionModelForm
# Create your views here.
def home(request):
    return render(request,"app_gen/home.html")
def about(req):
    return render(req,"app_gen/about.html")
def subscription(request):
    if request.method == "POST":
        form = SubscritionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("subscription_thankyou"))
    else:
        form = SubscritionModelForm()
    context = {'form': form}
    return render(request,"app_gen/subscription_from.html",context)
def subscription_thankyou(request):
    return render(request, "app_gen\subscription_thankyou.html")
