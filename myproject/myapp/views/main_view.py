from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Student
from ..serializers import StudentSerializer



@api_view(['POST','GET'])
def student_view(request):

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data added successfully"})
        else:
            return Response({'error':serializer.errors})
        
    if request.method == "GET":
        student = Student.objects.all()
        
    