from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from useraccount.models import User

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name','mobile','email','college','department','sem')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    mobile = forms.RegexField(regex=r'^\d{10}$')


    class Meta:
        model = User
        fields = ('full_name','mobile','email','college','department','sem')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=255,required=True)
    mobile = forms.IntegerField(max_value=10**10,min_value=10**9,required=True)
    email = forms.EmailField(widget=forms.widgets.EmailInput,required=True)
    department = forms.CharField(max_length=255,required=True)
    college = forms.CharField(max_length=255,required=True)
    sem = forms.IntegerField(min_value=1,max_value=8,required=True)

    class Meta:
        model = User
        fields = ['full_name','mobile','email','department','college','sem']

    '''
    @transaction.atomic to make sure those three operations are done in a single
    database transaction and avoid data inconsistencies
    in case of error.
    '''
    @transaction.atomic
    def save(self, commit=True):

        # student = Student.objects.create(
        #     user = user,
        #     usn = self.cleaned_data['usn'],
        #     year = self.cleaned_data['year'],
        #     cr = self.cleaned_data['cr']
        #     )
        if commit:
            user = self.instance
            user.set_password(self.cleaned_data['password1'])
            user.save()
        else:
            user = self.instance
            user.set_password(self.cleaned_data['password1'])
        return user

