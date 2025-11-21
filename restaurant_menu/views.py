from django.shortcuts import render
from django.views import generic
from .models import Item

class MenuListView(generic.ListView):
    model = Menu
    context_object_name = 'menu_list'



class MenuItemDetail(generic.DetailView):
    queryset = Item.objects.order_by('date_created')