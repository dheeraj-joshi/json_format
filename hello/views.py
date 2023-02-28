from .serializers import MessageSerializer
from .models import LogMessage
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.utils.timezone import datetime
# from django.http import HttpResponse

from django.http import JsonResponse




# Add this code elsewhere in the file:

@api_view(['GET','POST'])
def log_api(request):
    if request.method=='GET':
        logs=LogMessage.objects.all()
        serializer=MessageSerializer(logs,many=True)
        return Response({'status':True,'data':serializer.data,'message':'success'})
      
    
    if request.method=='POST':
        data=request.data
        # data['log_date']=datetime.now()
        serializer=MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':True,'data':serializer.data,'msg':'log created successfully'})
        return Response(serializer.errors)




def json(request):
    data=LogMessage.objects.values()
    print(data)
    
    return JsonResponse(list(data),safe=False)

    
