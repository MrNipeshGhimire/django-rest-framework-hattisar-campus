from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Student
from ..serializers import StudentSerializer
from rest_framework import status


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
        serializer = StudentSerializer(student, many=True)
        return Response({'data':serializer.data})


@api_view(['PUT','DELETE','GET'])
def student_view_detail(request,id):
    try:
        # object form
        student = Student.objects.get(id=id)
    except Exception as e:
        return Response({'error':"Data not found or server error"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method  == 'GET':
        serializer = StudentSerializer(student)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    

    # FOR DELETE OPERATION
    if request.method == 'DELETE':
        student.delete()
        return Response({'msg':"Data deleted successfully"},status=status.HTTP_200_OK)
    
    # for edit 
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data updated successfully",'updated_data':serializer.data})
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    






    
