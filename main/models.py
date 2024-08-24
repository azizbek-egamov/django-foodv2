from django.db import models
import time
import random

def uniqid(prefix='', more_entropy=False):
    m_time = time.time()
    base = '%8x%05x' % (int(m_time), int((m_time - int(m_time)) * 10000000))

    if more_entropy:
        base += '%.8f' % random.random()

    return prefix + base

class Food(models.Model):
    nomi = models.CharField(max_length=255)
    narxi = models.IntegerField()
    rasm = models.ImageField(upload_to='photo')
    holati = models.BooleanField(default=False)
    sana = models.DateTimeField(auto_now_add=True)
    rand = models.CharField(max_length=32, default=uniqid, unique=True)
    
class UserFoodList(models.Model):
    user_id = models.CharField(max_length=20)
    nomi = models.CharField(max_length=255)
    narxi = models.IntegerField()
    rasm = models.TextField()
    soni = models.IntegerField()
    rand = models.CharField(max_length=255)
    sana = models.DateTimeField(auto_now_add=True)
    
class AdminId(models.Model):
    admin = models.IntegerField(verbose_name="Admin ID")
    
    
    def __int__(self):
        return self.admin

    class Meta:
        verbose_name = 'Admin ID'
        verbose_name_plural = verbose_name + ''
        
class CardInfo(models.Model):
    card_number = models.CharField(max_length=16, verbose_name="Karta raqami")
    qr_kod = models.ImageField(upload_to='qr_code', verbose_name="QR kod rasmi")
    
    def __int__(self):
        return self.card_number

    class Meta:
        verbose_name = 'Karta ma\'lumotlari'
        verbose_name_plural = verbose_name + ''
        
class Users(models.Model):
    user_id = models.IntegerField(verbose_name='Foydalanuvchi ID')
    username = models.CharField(max_length=200, verbose_name="Username")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    
    def __int__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = verbose_name + 'lar'
    
class lang(models.Model):
    uid = models.IntegerField(verbose_name="ID raqami")
    lang = models.CharField(max_length=2)