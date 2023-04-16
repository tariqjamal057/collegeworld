from django.db import models
from django.contrib.auth.models import User



class BaseModal(models.Model):
    """
    Abstract Model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True