from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        readers = Group.objects.get(name="authors")
        user.groups.add(readers)
        return user