from django.db import models
from users.models import user

# Create your models here.

class team(models.Model):
    Team_Name = models.CharField(max_length=64)
    Team_description = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(user, related_name='admin', on_delete=models.CASCADE, to_field="id")
    members = models.ManyToManyField(user,max_length=50,help_text='Select members for team')

    def __str__(self) -> str:
        return self.Team_Name
    
    def display_members(self):
        return ', '.join(members.Name for members in self.members.all()[:])

    display_members.short_description = 'Users'