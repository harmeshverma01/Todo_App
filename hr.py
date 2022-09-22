


  
from django.db import models

# Create your models here.




#Views



        
from django.contrib import admin


#  try:
#         serializer = ForgetPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             email = request.data.get('email')
#             otp = request.data.get('otp')
#             user = Forget_password.objects.filter(email=email)
#             if user.exists():
#                 return Response(({'message': 'data is validated'}))
#             if user.otp == otp:
#                 return  Response({'message': 'otp is verify'})
#             user = user.first()
#             user.is_validate = True
#             user.save()
#             return Response(({'message': 'is validated now'}))
#         except:
#             return Response(({'user not valid'}), status=status.HTTP_204_NO_CONTENT)
        
# email = request.data.get('email')
#         otp = request.data.get('otp')
#         user = Forget_password.objects.filter(email=email, otp=otp)
#         if user.exists():
#             return Response(({'message': 'data is validated'}))
#         return Response(({'message': 'somethings went wrong'}))        


      
def validate(self, attrs):
    new_password = attrs.get('new_password')
    confirm_password = attrs.get('confirm_password')
    if new_password != confirm_password:
        raise serializers.ValidationError("password and confirm password does not match")
    user.set_password(password)
    user.save()
    return attrs

        
def post(self, request)    
    email = request.data.get('email')
    password = request.data.get('password')
    user = get_object_or_404(User, email=email)
    if user.check_password(password):
        serializer = ResetpasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(({'message': 'password changed successfully'}), status=status.HTTP_200_OK)
        return Response(serializer.errors)
    return Response(({'message': 'this is not valid password'}), status=status.HTTP_400_BAD_REQUEST)


class RecommendedProductView(APIView):
    serializer_class = OrderSerializer
    
    def get(self, request, id=None):
        product = OrderDetails.objects.filter(product__category_id=id).distinct()
        serializer = self.serializer_class(product, many=True)
        return Response(serializer.data)
    