from django.db import models
from blog.models import Post
from account.models import CustomUser


# Create your models here.


class UserProfile(models.Model):
    """
    user profile model that have three rows,
    owner,
    wallet,
    friends,
    in admin panel user email will be shown

    """
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    wallet = models.BigIntegerField(default=0)
    friends = models.ManyToManyField(CustomUser, blank=True)

    # transactions history must be added
    # ---------------------------------#
    def __str__(self):
        """
        :return: user email
        """
        return self.owner.email


class Transcation(models.Model):
    """ user transaction history model. it will be kept even when user deleted account"""
    time = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
