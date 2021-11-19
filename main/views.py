from django.shortcuts import render
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
import tempfile
from django.shortcuts import render, redirect, get_object_or_404
from .forms import  jobCardForm
from .models import  jobCardsClass


def home(request ):
    cards = jobCardsClass.objects.all().order_by('dateRecieved')

    counter = jobCardsClass.objects.all().count()

    content = {'cards':cards , 'counter':counter}
    return  render(request, 'main/home.html', content)


def jobCard(request ):
    form = jobCardForm()

    counter = jobCardsClass.objects.all().count()
    n = '100'
    jobnum = n + str(counter)

    if request.method == 'POST':
        form = jobCardForm(request.POST)
        if form.is_valid():

            form.jobNumber = jobnum

            form.save()
            obj = form.save()


            send_mail(
                'ZTS JOB CARD' + form.cleaned_data['jobNumber'],
                'A new job card has been loaded for ' + form.cleaned_data['customerName'] + ' with a Total Cost of ' + form.cleaned_data['totalCostOfJob'] + 'Job Number: '+ jobnum + '(http://localhost:8000/zipherJobCards/viewJobCard/'+ str(obj.id) +')',
                'it.zipher@gmail.com',
                ['it@zipher.co.za'],
                fail_silently=False,
            )

            return redirect('home')
        else:
            print(form.errors)


    content = {'form':form, 'n': jobnum }
    return render(request, 'main/jobCard.html', content)

def viewJobCard(request, jobCard_pk):
    card = get_object_or_404(jobCardsClass, pk=jobCard_pk)
    if request.method == 'GET':
        form = jobCardForm(instance=card)
        return render(request, 'main/viewSettings.html', {'card': card, 'form':form})

    return render(request, 'main/viewSettings.html', {'card': card})

def printJobCard(request, jobCard_pk):
    card = get_object_or_404(jobCardsClass, pk=jobCard_pk)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Job Card.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    content = {'card':card}
    html_string = render_to_string('main/printJobCard.html', content)
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output.seek(0)
        response.write(output.read())

    return response

def deleteJobCard(request, jobCard_pk):
    jobCard = get_object_or_404(jobCardsClass, pk=jobCard_pk)

    jobCard.delete()
    return redirect('home')
