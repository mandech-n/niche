from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from core.models import Student, Teacher, Donor, Public, Interest

class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField()
    school = forms.CharField()
    form = forms.CharField()
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.form.add(*self.cleaned_data.get('form'))
        student.email.add(*self.cleaned_data.get('email'))
        student.school.add(*self.cleaned_data.get('school'))
        student.interests.add(*self.cleaned_data.get('interests'))

        return user

class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField()
    school = forms.CharField()
    role = forms.CharField()
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.email.add(*self.cleaned_data.get('email'))
        teacher.form.add(*self.cleaned_data.get('form'))
        teacher.school.add(*self.cleaned_data.get('school'))
        teacher.role.add(*self.cleaned_data.get('role'))
        teacher.interests.add(*self.cleaned_data.get('interests'))
        return user

class DonorSignUpForm(UserCreationForm):
    email = forms.EmailField()
    organization = forms.CharField()
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_donor = True
        user.save()
        donor = Donor.objects.create(user=user)
        donor.organization.add(*self.cleaned_data.get('organization'))
        donor.email.add(*self.cleaned_data.get('email'))
        donor.interests.add(*self.cleaned_data.get('interests'))
        return user

class PartnerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    organization = forms.CharField()
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_partner = True
        user.save()
        partner = Partner.objects.create(user=user)
        partner.organization.add(*self.cleaned_data.get('organization'))
        partner.email.add(*self.cleaned_data.get('email'))
        partner.interests.add(*self.cleaned_data.get('interests'))
        return user

class PublicSignUpForm(UserCreationForm):
    email = forms.EmailField()
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.public = True
        user.save()
        partner = Partner.objects.create(user=user)
        partner.organization.add(*self.cleaned_data.get('organization'))
        partner.email.add(*self.cleaned_data.get('email'))
        partner.interests.add(*self.cleaned_data.get('interests'))
        return user
stakeholders =(
    ("1", "Student"),
    ("2", "Teacher"),
    ("3", "Donor"),
    ("4", "Partner"),

)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_types = forms.ChoiceField(choices = stakeholders)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','user_types']