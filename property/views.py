from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Property


def index(request):
    property = Property.objects.all()

    context = {'property': property}

    if 'edit_id' in request.GET:
        context = {**context, 'message': 'edit',
                   'message_id': request.GET['edit_id']}

    if 'delete_id' in request.GET:
        context = {**context, 'message': 'delete',
                   'message_id': request.GET['delete_id']}

    template = loader.get_template('property/index.html')
    return HttpResponse(template.render(context, request))


def create_new(request):

    if request.method == 'POST':
        property = Property(
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            zipcode=request.POST['zipcode'],
            county=request.POST['county'],
            area=request.POST['area'],
            zoning=request.POST['zoning'],
            attributes=request.POST['attributes'],
            owner=request.POST['owner']
        )
        property.save()
        return HttpResponseRedirect(reverse('property_index') + '?edit_id=' + str(property.id))

    context = {}
    template = loader.get_template('property/create.html')
    return HttpResponse(template.render(context, request))


def view(request, property_id=None):
    property = Property.objects.filter(id=property_id).first()
    context = {'property': property}
    template = loader.get_template('property/view.html')
    return HttpResponse(template.render(context, request))


def edit(request, property_id=None):
    property = Property.objects.filter(id=property_id).first()

    if request.method == 'POST':
        property.address = request.POST['address']
        property.city = request.POST['city']
        property.state = request.POST['state']
        property.zipcode = request.POST['zipcode']
        property.county = request.POST['county']
        property.area = request.POST['area']
        property.zoning = request.POST['zoning']
        property.attributes = request.POST['attributes']
        property.owner = request.POST['owner']
        property.save()
        return HttpResponseRedirect(reverse('property_index') + '?edit_id=' + str(property.id))

    context = {'property': property}
    template = loader.get_template('property/edit.html')
    return HttpResponse(template.render(context, request))


def delete(request, property_id=None):
    property = Property.objects.filter(id=property_id).first()

    if request.method == 'POST':
        property = Property.objects.filter(id=property_id).delete()
        return HttpResponseRedirect(reverse('property_index') + '?delete_id=' + str(property_id))

    context = {'property': property}
    template = loader.get_template('property/delete.html')
    return HttpResponse(template.render(context, request))
