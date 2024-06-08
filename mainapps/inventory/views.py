from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView,UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Inventory, InventoryCategory
from .forms import InVentoryForm, InventoryCategoryForm



# def create_iventory(self):
#     pass

class InventoryHome(TemplateView):
    # model= Inventory()
    template_name='inventory/inventory.html'

    # form_class= InVentoryForm
    # success_url='/admin'

def add_category(request):
    if request.method=='POST':
        form=InventoryCategoryForm(request.POST)
        if form.is_valid():
            category=form.save()
            return JsonResponse({'id':category.id,'name':category.name})

    return render(request,'common/inpage_form.html',{'form':InventoryCategoryForm})
def get_inventory_category(request):
    user= request.user
    if user:
        if user.is_main and user.company:
            categories= InventoryCategory.objects.filter(profile=user.company)
            return render(request,'inventory/categories.html',{'categories':categories})

        elif user.is_worker and user.profile:
            categories= InventoryCategory.objects.filter(profile=user.profile)
            return render(request,'inventory/categories.html',{'categories':categories})
        