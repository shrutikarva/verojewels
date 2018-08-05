from  .models import ArtType
def add_variable_to_context(request):
    mylist=[]
    type_list = ArtType.objects.all()
    for i in type_list:
        mylist.append(i)

    return {'type_list' : mylist}


