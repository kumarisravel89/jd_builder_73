from django.db.models import CharField,IntegerField,DateField,Model,AutoField

# Create your models here.

class UserPasswordTable(Model):
    UserId=AutoField(primary_key=True)
    UserName=CharField(max_length=100)
    UserEmail=CharField(max_length=50,primary_key=True)
    Password1=CharField(max_length=20)

    def __str__(self):
        return self.UserId


