from django.db import models

class Request(models.Model):
    PlayerID = models.TextField()
    PaymentMethod = models.TextField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Request {self.id} By User {self.PlayerID}"
