from django.shortcuts import render
from .forms import MailForm
# Create your views here.
def index(request):
    form = MailForm()
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'success.html')
    return render(request, 'index.html', {'form': form})