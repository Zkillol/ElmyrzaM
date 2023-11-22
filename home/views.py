from django.shortcuts import render, get_object_or_404
from .models import CountryModel, TableCoutnry, Slider


def couuntry_list_view(request):
    if request.method == "GET":
        country_list = CountryModel.objects.all()


        return render(request, template_name='index.html', context={
            'country_list': country_list,

        })


def country_list_detail_view(request, id):
    if request.method == 'GET':
        country_id = get_object_or_404(CountryModel, id=id)
        return render(request, template_name='country_detail.html', context={'country_id': country_id})

def country_detail_view(request):
    table_list = TableCoutnry.objects.all()
    slider_list = Slider.objects.all()
    return render(request, template_name='detail.html' , context={
            'table_list': table_list,
            'slider_list': slider_list})
