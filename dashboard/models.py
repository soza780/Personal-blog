from django.db import models
from blog.models import Post
from account.models import CustomUser


# Create your models here.
class Transaction(models.Model):
    """ user transaction history model. it will be kept even when user deleted account"""
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField(blank=True, null=True)


class UserSocialLinks(models.Model):
    INSTAGRAM = "INSTAGRAM"
    GITHUB = "GITHUB"
    LINKDIN = "LINKDIN"

    SOCIAL_NETWORKS = (
        (INSTAGRAM, "Instagram"),
        (GITHUB, "Github"),
        (LINKDIN, "Linkdin")
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    social_type1 = models.CharField(choices=SOCIAL_NETWORKS, blank=True, null=True, max_length=100)
    social_type1_link = models.CharField(max_length=255,blank=True, null=True)
    social_type2 = models.CharField(choices=SOCIAL_NETWORKS, blank=True, null=True, max_length=100)
    social_type2_link = models.CharField(max_length=255,blank=True, null=True)
    social_type3 = models.CharField(choices=SOCIAL_NETWORKS, blank=True, null=True, max_length=100)
    social_type3_link = models.CharField(max_length=255,blank=True, null=True)



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
