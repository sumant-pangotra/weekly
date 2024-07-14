from django.db import models

"""
u = AppUser(first_name="John",last_name="Doe",email_id="johndoe@test.com",date_of_birth="2001-01-28")
u.save()
AppUser.objects.all()
u.id
u.life_expetency_years = 75
u.save()
AppUser.objects.filter(id=1)
"""

class AppUser(models.Model):
    userId = models.BigAutoField(auto_created=True,primary_key=True,verbose_name="userId")
    first_name = models.CharField(max_length=255,verbose_name="First Name")
    last_name = models.CharField(max_length=255,verbose_name="Last Name")
    email_id = models.EmailField(unique=True,null=False,verbose_name="Email")
    date_of_birth = models.DateField(verbose_name="Date of Birth",null=False)
    life_expetency_years = models.PositiveSmallIntegerField(default=70,verbose_name="Life Expetency")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
