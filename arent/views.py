from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.models import User 
from mitra.models import AkunMitra, Iklan
from mitra.forms import IklanForm, PilihProvinsiForm
from django.db.models import Q

class Home(ListView):
    template_name = 'home.html'
    model = Iklan
    context_object_name = 'iklan_list'
    paginate_by = 5
    #ordering = ['-id']

    def get_queryset(self):
        cari = self.request.GET.get('cari')
        cari_provinsi = self.request.GET.get('provinsi')
        cari_jenis_kendaraan = self.request.GET.get('jenis_kendaraan')
        if cari != None:
            #object_list = Iklan.objects.filter(judul__icontains=cari)
            object_list = self.model.objects.filter(Q(judul__icontains=cari)|Q(deskripsi_lain__icontains=cari)|Q(merk__icontains=cari)|Q(tipe_kendaraan__icontains=cari))
        elif cari_jenis_kendaraan != None:
            object_list = self.model.objects.filter(jenis_kendaraan=cari_jenis_kendaraan)
        elif cari_provinsi != None and cari_jenis_kendaraan == None:
            object_list = self.model.objects.filter(mitra__akunmitra__provinsi=cari_provinsi)
        elif cari_provinsi != None and cari_jenis_kendaraan != None:
            object_list = self.model.objects.filter(mitra__akunmitra__provinsi=cari_provinsi, jenis_kendaraan=cari_jenis_kendaraan)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self,*args, **kwargs):
        provinsi_list = PilihProvinsiForm(use_required_attribute=False)
        self.kwargs.update({
            'page_title':'Home',
            'provinsi_list':provinsi_list,
        })
        kwargs = self.kwargs
        context = super().get_context_data(**kwargs)
        return context

    def get_allow_empty(self):
        return True


def redirectKeHome(request):
    return redirect('home', 1)