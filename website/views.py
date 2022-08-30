from django.shortcuts import render
from django.core.mail import send_mail
from .models import Event

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('txtName')
        email = request.POST.get('txtEmail')
        subject = request.POST.get('txtSubject')
        message = request.POST.get('txtMsg')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }


        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['xrmissnatural@gmail.com'])

    events = Event.objects.all()
    return render(request, 'website/index.html', {'events': events})
