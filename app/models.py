from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save 

class OdradjeniSati(models.Model):
	datum = models.DateField(null= True, blank = True, auto_now_add=True)
	pvremena = models. TimeField(null= True, blank = True, verbose_name= 'Početak radnog vremena')
	kvremena = models. TimeField(null= True, blank = True, verbose_name= 'Kraj radnog vremena')
	korisnik = models.ForeignKey(User, on_delete=models.CASCADE ,null = True, blank = True,verbose_name = 'Korisnik' )
	
	class Meta:
		verbose_name_plural = "Odrađeni sati"

	def __int__(self):
		return self.id

	def razlika(self):
		date_format = "%H:%M:%S"
		if self.pvremena != None and self.kvremena != None:
			time1 = datetime.strptime(str(self.pvremena), date_format)
			time2 = datetime.strptime(str(self.kvremena), date_format)
			difference = time2-time1
			diffe = difference.seconds / (60*60)
			diff = str(round(diffe,2))
			return diff

	def vrijeme(self):
		date_format = "%H:%M:%S"
		if self.pvremena != None and self.kvremena != None:
			time1 = datetime.strptime(str(self.pvremena), date_format)
			dtime1 = datetime.strptime('03:00:00', '%H:%M:%S')
			dtime2 = datetime.strptime('16:00:00', '%H:%M:%S')
			dtime3 = datetime.strptime('16:00:00', '%H:%M:%S')
			dtime5 = datetime.strptime('00:00:00', '%H:%M:%S')
			if time1 >= dtime1 and time1 <= dtime2: 
				tip = 'Redovna dnevna smjena'
				return tip
			elif time1 >= dtime3 or time1 >= dtime5 and time1 <= dtime2:
				tip = 'Noćna smjena'
				return tip

	def prekovremeni(self):
		date_format = "%H:%M:%S"
		if self.pvremena != None and self.kvremena != None:
			time1 = datetime.strptime(str(self.pvremena), date_format)
			time2 = datetime.strptime(str(self.kvremena), date_format)
			difference = time2-time1
			diffe = difference.seconds / (60*60)
			
			if diffe > 8:
				diffe1 = diffe - 8
				diff2 = str(round(diffe1,2))
				prk = 'Da'
				return prk, diff2
			else: 
				prk = 'Ne'
				return prk

	def get_absolute_url(self):
		return reverse('osati-pregled')

class ListaZadataka(models.Model):
	naziv = models.CharField(max_length=100)
	opis = models.TextField(max_length = 600)
	korisnik = models.ForeignKey(User, on_delete=models.CASCADE ,null = True, blank = True,verbose_name = 'Korisnik' )
	STATUS = (
		('u', 'U Tijeku'),
		('r', 'Riješeno'),)
	status = models.CharField(max_length=1,choices=STATUS,blank=True,default='u',)
	class Meta:
		verbose_name_plural = "Kreirani zadaci"

	def __str__(self):
		return self.naziv

	def get_absolute_url(self):
		return reverse('zadatak-detail', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nazivfirme = models.CharField(max_length=500, blank=True, verbose_name= 'Naziv firme')
    adresa = models.CharField(max_length=30, blank=True)
    kontakt = models.CharField(max_length= 10 , blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
    	if created:
    		Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
    	instance.profile.save()



