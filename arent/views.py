from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.models import User 
from mitra.models import AkunMitra, Iklan

class Home(ListView):
    template_name = 'home.html'
    model = Iklan
    context_object_name = 'iklan_list'
    ordering_by = ['-id']
    paginate_by = 25
    def get_context_data(self,*args, **kwargs):
        nama_user = AkunMitra.objects.get(nama='Fachri')
        
        self.kwargs.update({
            'page_title':'Home'
        })
        kwargs = self.kwargs
        context = super().get_context_data(**kwargs)
        return context
    
def redirectKeHome(request):
    return redirect('home', 1)