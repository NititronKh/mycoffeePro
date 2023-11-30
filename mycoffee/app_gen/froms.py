from django import forms
from app_cof.models import Coffee
from .models import Subscription

class CoffeeMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title
    
    

class SubscriptionFrom(forms.Form):
    name = forms.CharField(max_length=60,required=True,label='ชื่อ-นามสกุล')
    email = forms.EmailField(max_length=60,required=True,label='อีเมล')
    coffee_set = CoffeeMultipleChoiceField(
        queryset=Coffee.objects.order_by('-is_premium'),
        required = True,
        label = 'เมนูที่สนใจ',
        widget = forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True,label="ข้อความยาวๆผมรู้ว่าคุณจะไม่อ่าน กดยอมรับและเข้าใจได้เลย")

class SubscritionModelForm(forms.ModelForm):
    coffee_set = CoffeeMultipleChoiceField(
        queryset=Coffee.objects.order_by('-is_premium'),
        required = True,
        label = 'เมนูที่สนใจ',
        widget = forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True,label="ข้อความยาวๆผมรู้ว่าคุณจะไม่อ่าน กดยอมรับและเข้าใจได้เลย")
    class Meta:
        model = Subscription
        fields = ['name', 'email', 'coffee_set','accepted']
        labels = {
            'name': 'ชื่อ-นามสกุล',
            'email': 'อีเมล',
            'food_set':'เมนูที่สนใจ'
        }