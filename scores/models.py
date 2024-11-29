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
            account_sid = "ACcf46515f1e8daf2dbf0db735f32c1b57"
            # Your Auth Token from twilio.com/console
            auth_token  = "00707947eb8dcb17d49ed6bfc3f90e99"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"Your Score is - {self.result} JEREMIAH 29:11",
                from_="+16814122387",
                to="+639489635571",
            )

            print(message.body)
        return super().save(*args, **kwargs)
