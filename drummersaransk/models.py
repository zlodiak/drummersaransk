from django.db import models
from django.contrib.auth.models import User, UserManager
from django.conf import settings
import os

from captcha.fields import CaptchaField


class Status(models.Model):		
	status = models.CharField(
		max_length=40, 
		blank=False,
	)		
		
	@classmethod
	def get_status_list(self):
		status_list = list()
		status_list.append(('', 'Не указан'))
		
		for values_ins in Status.objects.all().values_list('id', 'status'):
			status_list.append(values_ins)
			
		return status_list				
		
		
class Gender(models.Model):		
	gender = models.CharField(
		max_length=10, 
		blank=False,
	)	
		
	@classmethod
	def get_gender_list(self):
		gender_list = list()
		gender_list.append(('', 'Не указан'))
		
		for values_ins in Gender.objects.all().values_list('id', 'gender'):
			gender_list.append(values_ins)
			
		return gender_list		
		
		
class Teacher(models.Model):		
	teacher = models.CharField(
		max_length=40, 
		blank=False,
	)	

	def __str__(self):
		return self.teacher
				

class UserProfile(User):			
	family = models.CharField(
		'Фамилия',
		max_length=30, 
		blank=True,
		null=True,
	)
	name1 = models.CharField(
		'Имя',
		max_length=30, 
		blank=True,
		null=True,
	)
	name2 = models.CharField(
		'Отчество',
		max_length=30, 
		blank=True,
		null=True,
	)
	nickname = models.CharField(
		'Отображаемое имя',
		max_length=30, 
		blank=False,
	)
	gender = models.ForeignKey(
		Gender,
		verbose_name='Пол',
		blank=True,
		null=True,
	)
	birth_date = models.DateField(
		'Дата рождения',
		blank=True,
		null=True,
	)
	status = models.ForeignKey(
		Status,
		verbose_name='Статус',
		blank=True,
		null=True,
	)
	city = models.CharField(
		'Город',
		max_length=50, 
		default='Саранск', 
		blank=False,
	)
	phone = models.CharField(
		'Номер телефона',
		max_length=50, 
		blank=True,
		null=True,
	)
	skype = models.CharField(
		'Skype',
		max_length=50, 
		blank=True,
		null=True,
	)
	email_address = models.EmailField(
		'Адрес электронной почты',
		max_length=50, 
		blank=False,
	)	
	other = models.TextField(
		'Интересы и увлечения',
		max_length=500,
		blank=True,
		null=True,
	)
	avatar = models.ImageField(
		'Фото',
		upload_to='userprofile/avatar/', 
		blank=True,
		null=True,
	)

	drum_period_1 = models.DateField(
		'Начал играть',
		blank=True,
		null=True,
	)	
	drum_period_2 = models.DateField(
		'Закончил играть',
		blank=True,
		null=True,
	)	
	drum_photo = models.ImageField(
		'Фото инструмента',
		upload_to='userprofile/drum_photo/', 
		blank=True,
		null=True,
	)
	drums = models.CharField(
		'Использую барабаны',
		max_length=300, 
		blank=True,
		null=True,
	)	
	cymbals = models.CharField(
		'Использую тарелки',
		max_length=300, 
		blank=True,
		null=True,
	)	
	hardware = models.CharField(
		'Использую хардвер',
		max_length=300, 
		blank=True,
		null=True,
	)	
	sticks = models.CharField(
		'Использую палочки',
		max_length=300, 
		blank=True,
		null=True,
	)	
	plastics = models.CharField(
		'Использую пластики',
		max_length=300, 
		blank=True,
		null=True,
	)	
	groups_past = models.CharField(
		'Играл в группах',
		max_length=300, 
		blank=True,
		null=True,
		help_text='перечислить через запятую',
	)
	groups_present = models.CharField(
		'Играю в группах',
		max_length=300, 
		blank=True,
		null=True,
		help_text='перечислить через запятую',
	)		
	teacher = models.ForeignKey(
		Teacher,
		verbose_name='Преподаватель',
		blank=True,
		null=True,
	)	
	teacher_fio = models.CharField(
		'Ф. И. О. преподователя',
		max_length=300, 
		blank=True,
		null=True,
	)
	drummers = models.CharField(
		'Уважаемые барабанщики',
		max_length=300, 
		blank=True,
		null=True,
		help_text='перечислить через запятую',
	)		
		
	objects = UserManager()
		
	@classmethod
	def get_city_list(self):
		result = self.objects.values_list('city', flat=True).distinct()	
		return result
		
	@classmethod
	def get_distinct_cities(self):		
		cities_list = list()
		cities_list.append(('', 'Не указан'))
		
		for values_ins in UserProfile.objects.all().values_list('city', 'city').distinct():
			cities_list.append(values_ins)
			
		return cities_list						


class PathGlory(models.Model):
	user_id = models.IntegerField(
		'',
	)		
	title = models.CharField(
		'Название события',
		max_length=100, 
		blank=False,
	)			
	date = models.DateField(
		'Дата проведения',
		blank=True,
		null=True,
	)		
	place = models.CharField(
		'Место проведения',
		max_length=200, 
		blank=True,
		null=True,
	)		
	teaser = models.TextField(
		'Вступительный текст (тизер)',
		max_length=10000, 
		blank=False,
		help_text='Будет отображаться в ленте',
	)			
	text = models.TextField(
		'Основной текст',
		max_length=100, 
		blank=False,
		help_text='Будет отображаться на отдельной странице',
	)			
	path_glory_photo = models.ImageField(
		'Фото',
		blank=True,
		upload_to='userprofile/path_glory_photo/', 
		null=True,
	)							
	
	@classmethod
	def get_all_entries(self):
		return self.objects.all()
		
	@classmethod
	def get_all_user_entries(self, id):
		return self.objects.filter(user_id=id)		
		
	@classmethod
	def get_entry(self, user_id, id_p):
		return self.objects.get(id=id_p, user_id=user_id)	
		
	@classmethod
	def get_entry_short(self, id):
		return self.objects.get(id=id)				


class Friends(models.Model):		
	user_id = models.IntegerField(
		blank=False,
		null=False,
	)	
	friend_id = models.IntegerField(
		blank=False,
		null=False,	
	)	
	
	@classmethod
	def get_entry(self, user_id, friend_id):
		try:
			self.objects.get(user_id=user_id, friend_id=friend_id)
		except:
			return False
		else:
			return True
		
	@classmethod
	def set_entry(self, user_id, friend_id):
		try:
			obj = self.objects.create(
				user_id = user_id,
				friend_id = friend_id,
			)			
			obj.save
		except:
			return False
		else:
			return True
		
	@classmethod
	def del_entry(self, user_id, friend_id):	
		try:
			self.objects.get(user_id=user_id, friend_id=friend_id).delete()
		except:
			return False
		else:
			return True		
			
	@classmethod
	def get_all_entries(self, user_id):
		return self.objects.filter(user_id=user_id)
		
	@classmethod
	def count_entry(self, user_id):		
		return self.objects.filter(user_id=user_id).count()
		
	@classmethod
	def exists_entry(self, user_id):		
		res = self.objects.filter(user_id=user_id)
		return res


