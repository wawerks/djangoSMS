from django.db import models
import os
from twilio.rest import Client
# Create your models here.

class Score (models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = ["TWILIO ACCOUNT SID"]
            # Your Auth Token from twilio.com/console
            auth_token  = ["TWILIO ACCOUNT TOKEN"]
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"Test - {self.result} ",
                from_=["TWILIO TRIAL NUMBER"],
                to=["YOUR MOBILE NUMBER"],
            )

            print(message.body)
        return super().save(*args, **kwargs)
