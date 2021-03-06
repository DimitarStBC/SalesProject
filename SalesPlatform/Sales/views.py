from django.shortcuts import render
from Sales.models import Users,Contacts
from Sales.serializers import UserSerializer,ContactSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import io,json
def base_template(request):
    render(request,'sales/base.html')    

def EnterContent(request):
    return render(request,'sales/enterContent.html')
def user_template(request):
    usersData = Users.users.all()
    serializer = UserSerializer(usersData, many=True)
    users = serializer.data
    context = {'users':users}
    return render(request,'sales/users.html',context)    

def contacts_template(request):
    contactsdata = Contacts.contacts.all()
    serializer = ContactSerializer(contactsdata, many=True)
    contacts = serializer.data
    return render(request,'sales/contacts.html',context=contacts)

# Create your views here.
def user_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        users = Users.users.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def contact_list(request):
    """
    List all contacts, or create a new contact.
    """
    if request.method == 'GET':
        contacts = Contacts.contacts.all()
        serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = dict(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)        