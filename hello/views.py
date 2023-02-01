from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage

from django.utils.timezone import datetime
# from django.http import HttpResponse

from django.http import JsonResponse
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def homes(request):
    return render(request, "hello/home.html")
def about(request):
    return render(request,'hello/about.html')
def contact(request):
    return render(request,'hello/contact.html')




# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)
    


    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        
    else:
        return render(request, "hello/log_message.html", {"form": form})    

def json(request):
    data=list(LogMessage.objects.values())
    return JsonResponse(data,safe=False)

    
