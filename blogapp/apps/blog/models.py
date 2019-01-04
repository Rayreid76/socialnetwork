# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class userManage(models.Manager):
    def userValidation(self, fname, lname, email, password, cpassword, datebirth):
        errors = []
        if len(fname) <= 3:            
            errors.append("Error first name is to short")
        if len(lname) <= 3:            
            errors.append("Error last name is to short")
        if len(password) < 8:            
            errors.append("Error password needs to be 8 characters")
        if cpassword != password:            
            errors.append("Error passward does not match")
        if datebirth == "":
            errors.append("Error needs Birht date")
        if not EMAIL_REGEX.match(email):
            errors.append("Error not valid email")
        if len(errors) > 0:
            return errors
        try:
            self.get(email=email)
            errors.append("Name and Email already exist.")
            return errors
        except:
            hashed = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
            account = "user"
            Users.objects.create(fname=fname, lname=lname, email=email, password=hashed, date_of_birth=datebirth, account_leval=account)
            return errors

    def loginVal(self, email, password):
        errors = []
        if email == "":
            errors.append("Email cannot be blank!")
        if password == "":
            errors.append("Password cannot be blank!")
        else:
            users = self.filter(email=email)
            if len(users) > 0:
                user = users[0]
                coded = b'password'
                if bcrypt.checkpw(coded.encode(), user.password.encode()):
                    return (True, user.id) 
                else:
                    errors.append("Incorrect password")
            else:
                errors.append("No email found")
        return (False, errors)
    
    def quoteVal(self, author, quote, user):
        errors = []
        if len(author) < 4:
            errors.append("No Author entered")
        if len(quote) < 11:
            errors.append("Quote is to short")
        if len(errors) > 0:
            return errors
        else:
            Quotes.objects.create(author=author,quote=quote,user=Users.objects.get(id=user))
            return errors

class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    account_leval = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = userManage()

class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="favorite")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = userManage()

class Likes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="liked")
    quote = models.ForeignKey(Quotes, on_delete=models.CASCADE, related_name="liked")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = userManage()
