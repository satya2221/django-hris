from django.contrib.auth.mixins import LoginRequiredMixin

class LoginRequiredView(LoginRequiredMixin):
    login_url = '/login/'

    # setelah login akan mengarahkan ke halaman yang diinginkan
    # selain next ada redirect_to
    redirect_field_name = 'next' 

    class Meta:
        abstract = True
