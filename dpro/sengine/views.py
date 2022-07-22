from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def index(request):
    return HttpResponse("Hello world!")


class MyCreateView(View):
    """
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello Sunil!")


class LoginView(View):
    """
    """
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {})
   
    def post(self, request, *args, **kwargs):
        #form = self.form_class(request.POST)
        fname = request.POST['fname']
        lname = request.POST['lname']
        if fname and lname:
            from sengine.models import Person
            # <process form cleaned data>
            #import pdb;pdb.set_trace()
            Person.objects.create(first_name=fname, last_name=lname)
            return render(request, 'success.html', {'fname': fname ,'lname': lname})

        return render(request, self.template_name, {})

    