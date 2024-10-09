from email.policy import default
from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
import secrets
from .paystack import PayStack
# Create your models here.
User    = settings.AUTH_USER_MODEL

def limit_value(value):
    val=str(value)
    if len(val) <= 10 and len(val) <= 12 and val.isdigit() == True:
        return value
    else:
        raise ValidationError("Account Number must be 10 digit")
    

PARTIES =(
    ("ANKARA","ANKARA"),("FRESHER PARTY","FRESHER PARTY"),
    ("NADESTU PARTY","NADESTU PARTY"),("OSTEGA PARTY","OSTEGA PARTY"),
)
class party(models.Model):
    price = models.PositiveBigIntegerField(blank=False)
    event = models.CharField(max_length=50,choices=PARTIES,blank=False)
    
    def __str__(self):
        return self.event


class Agent(models.Model):
    name = models.CharField(max_length=50,blank=False)
    bank = models.CharField(max_length=50,blank=False)
    whatsaap = models.URLField(blank=False)
    account = models.CharField(max_length=15,validators=[limit_value],blank=False)
    #phone = PhoneNumberField(blank=False)
    def __str__(self):
        return self.name
    
    

class Payment(models.Model):
    name = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    tictype = models.CharField(max_length=40,default="all" , blank=False, null=False)
    contact       = PhoneNumberField(blank=False)
    amount = models.PositiveIntegerField()
    ref =models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(blank=True,default=1)
    class Meta:
        ordering=("-date_created",)

    def __str__(self) -> str:
        return f"Payment: {self.amount}"
    def save(self , *args,**kwargs) -> None:
        while not self.ref :
            ref = secrets.token_urlsafe(20)
            object_with_similar_ref  = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args,**kwargs)

    def amount_value(self) -> int:
        return self.amount*100*self.quantity
    def amount_norm(self) -> int:
        return self.amount*self.quantity
     
       
class TicketPrice(models.Model):
    regular = models.PositiveIntegerField()
    vip = models.PositiveIntegerField()
    vip_premium = models.PositiveIntegerField()
    
            
            
      
    
    
