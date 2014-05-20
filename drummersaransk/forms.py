from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.conf import settings
import os

from drummersaransk.models import UserProfile, PathGlory, Gender, Status

from captcha.fields import CaptchaField


error_dict = {
	'spaces': 'Поле не может состоять только из пробелов',
}


class PathGloryForm(forms.ModelForm):
	date = forms.DateField(
		widget=forms.TextInput(attrs={
			'class':'datepicker',
		}),
		required=False,
		label='Дата проведения',
	)	
	
	user_id = forms.IntegerField(
		widget=forms.HiddenInput,
		required=True,
	)		
				
	class Meta:
		model = PathGlory
		fields = (
			'user_id',
			'title', 
			'date', 
			'place', 
			'teaser', 
			'text',
			'path_glory_photo',
		)		
		
	def clean_title(self):
		title = self.cleaned_data['title'].strip()
		if len(title) == 0:
			raise forms.ValidationError(error_dict['spaces'])		

		return title	
		
	def clean_text(self):
		text = self.cleaned_data['text'].strip()
		if len(text) == 0:
			raise forms.ValidationError(error_dict['spaces'])		

		return text			
		
	def clean_teaser(self):
		teaser = self.cleaned_data['teaser'].strip()
		if len(teaser) == 0:
			raise forms.ValidationError(error_dict['spaces'])		

		return teaser			
							

class MyRegistrationForm(UserCreationForm):	
	username = forms.CharField(
		label='Логин',
		help_text='',
		required=True,
	)
	
	password1 = forms.CharField(
		label='Пароль',
		help_text='',
		required=True,
		widget=forms.PasswordInput,
	)	
	
	password2 = forms.CharField(
		label='Подтверждение пароля',
		help_text='',
		required=True,
		widget=forms.PasswordInput,
	)
	
	email_address = forms.EmailField(
		label='Адрес электронной почты',
		help_text='',
		required=True,
	)	
	
	status = forms.ChoiceField(
		widget=forms.Select, 
		choices=Status.get_status_list(),
		label='Статус',
		required=False,
	)	
		
	captcha = CaptchaField()
	
	class Meta:
		model = UserProfile
		fields = (
			'username', 
			'nickname', 
			'city', 
			'email_address', 
			'password1', 
			'password2',
		)

	def clean_password1(self):
		password1 = self.cleaned_data['password1']
		q_letters = len(password1)
		if q_letters < 3:
			raise forms.ValidationError("Пароль не может быть короче 3 символов.")		

		return password1	
		
	def clean_username(self):
		username = self.cleaned_data['username']
		q_letters = len(username)
		if q_letters < 3:
			raise forms.ValidationError("Логин не может быть короче 3 символов.")		

		return username		
		
	def clean_status(self):
		status = self.cleaned_data['status']	
		if not status:
			raise forms.ValidationError("Это обязательное поле.")		

		return status	
		
	def save(self):
		obj = super(MyRegistrationForm, self).save(commit=False)
		status_num = self.cleaned_data.get('status', None)	
			
		if status_num:
			status = Status.objects.get(id=status_num)
			obj.status = status			
		return obj.save()					
				
		
class PersonalDataForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PersonalDataForm, self).__init__(*args, **kwargs)
		if self.instance.status:
			self.fields["status"].initial = self.instance.status.id
			
		if self.instance.gender:
			self.fields["gender"].initial = self.instance.gender.id
        	
	birth_date = forms.DateField(
		widget=forms.TextInput(attrs={
			'class':'datepicker',
		}),
		required=False,
		label = 'Дата рождения',
	)
	
	gender = forms.ChoiceField(
		widget=forms.Select, 
		choices=Gender.get_gender_list(),
		label='Пол',
		required=False,
	)	

	status = forms.ChoiceField(
		widget=forms.Select, 
		choices=Status.get_status_list(),
		label='Статус',
		required=False,
	)	
			
	class Meta:
		model = UserProfile
		fields = (
			'family', 
			'name1', 
			'name2', 
			'nickname', 
			#'gender', 
			'birth_date', 
			#'status', 
			'city', 
			'phone', 
			'skype', 
			'email_address', 
			'other', 
		)
		
	def clean_nickname(self):
		nickname = self.cleaned_data['nickname'].strip()
		if len(nickname) == 0:
			raise forms.ValidationError(error_dict['spaces'])		

		return nickname	
		
	def clean_city(self):
		city = self.cleaned_data['city'].strip()
		if len(city) == 0:
			raise forms.ValidationError(error_dict['spaces'])		

		return city	
		
	def clean_email_address(self):
		email_address = self.cleaned_data['email_address'].strip()
		if len(email_address) == 0:
			raise forms.ValidationError(error_dict['spaces'])		

		return email_address								
		
	def clean_status(self):
		status = self.cleaned_data['status']	
		if not status:
			raise forms.ValidationError("Это обязательное поле.")		

		return status			

	def save(self):
		obj = super(PersonalDataForm, self).save(commit=False)
		status_num = self.cleaned_data.get('status', None)
		gender_num = self.cleaned_data.get('gender', None)
		
		if gender_num:
			gender = Gender.objects.get(id=gender_num)
			obj.gender = gender
		else:
			obj.gender = None
			
		if status_num:
			status = Status.objects.get(id=status_num)
			obj.status = status			
		return obj.save()

class DrumDataForm(forms.ModelForm):
	drum_period_1 = forms.DateField(
		widget=forms.TextInput(attrs={
			'class':'datepicker',
		}),
		required=False,
		label='Начало барабанной карьеры',
	)
	
	drum_period_2 = forms.DateField(
		widget=forms.TextInput(attrs={
			'class':'datepicker',
		}),
		required=False,
		label='Конец барабанной карьеры',
	)	
			
	class Meta:
		model = UserProfile
		fields = (
			'drum_period_1', 
			'drum_period_2', 
			'drum_photo', 
			'drums', 
			'cymbals', 
			'hardware', 
			'sticks', 
			'plastics', 
			'groups_past', 
			'groups_present', 
			'teacher', 
			'teacher_fio', 
			'drummers',
		)	

	def clean(self):	
		cleaned_data = super(DrumDataForm, self).clean()
		teacher = cleaned_data.get("teacher")
		teacher_fio = cleaned_data.get("teacher_fio")	
        		
		if teacher:
			if teacher.id == 2 and teacher_fio.strip() == '':					
				raise forms.ValidationError("Ф. И. О. преподавателя должно быть указано.")
			else:							
				return cleaned_data	
		else:
			return cleaned_data		

class ChangePasswordForm(forms.Form):
	password_old = forms.CharField(
		max_length=30, 
		widget=forms.PasswordInput(),
		label = 'Действующий пароль',
	)
	password1 = forms.CharField(
		widget=forms.PasswordInput(),
		label = 'Новый пароль',
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput(),
		label = 'Новый пароль ещё раз',
	)
	
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(ChangePasswordForm, self).__init__(*args, **kwargs)	
		
	def clean_password1(self):
		password1 = self.cleaned_data['password1']
		q_letters = len(password1)
		if q_letters < 3:
			raise forms.ValidationError("Пароль не может быть короче 3 символов.")		

		return password1		
	
	def clean_password_old(self):
		cleaned_data = self.cleaned_data
		password_old = cleaned_data.get("password_old")	
		if not self.request.user.check_password(password_old):
			raise forms.ValidationError("Действующий пароль введён не верно.")
		else:
			return password_old
	
	def clean(self):	
		cleaned_data = self.cleaned_data
		password1 = cleaned_data.get("password1")
		password2 = cleaned_data.get("password2")	
        		
		if password1 != password2:		
			raise forms.ValidationError("Новые пароли не совпадают.")
		else:							
			return cleaned_data
			
			
class ChangeAvatarForm(forms.Form):
	avatar = forms.ImageField()			
		
	
class AuthenticationCustomForm(AuthenticationForm):
	username = forms.CharField(
		label='Имя пользователя',
		widget=forms.TextInput(attrs={
			'placeholder': 'Логин',
		}),		
	)

	password = forms.CharField(
		label='Пароль', 
		widget=forms.PasswordInput(attrs={
			'placeholder': 'Пароль',
		}),
	)
	
	
class SearchFriendsForm(forms.Form):
	name = forms.CharField(
		label='Имя',
		required=False,	
	)
		
	birth_date = forms.DateField(
		widget=forms.TextInput(attrs={
			'class': 'datepicker fld_birth_date',
			'id': 'birth_date',
			'name': 'birth_date',
		}),
		required=False,
		label='Дата рождения',
	)	
	
	gender = forms.ChoiceField(
		widget=forms.Select, 
		choices=Gender.get_gender_list(),
		label='Пол',
		required=False,
	)	

	status = forms.ChoiceField(
		widget=forms.Select, 
		choices=Status.get_status_list(),
		label='Статус',
		required=False,
	)
	
	city = forms.ChoiceField(
		widget=forms.Select, 
		choices=UserProfile.get_distinct_cities(),
		label='Город',
		required=False,
	)	
	
