from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from .models import *
from rest_auth.views import LoginView
from django.shortcuts import get_object_or_404

def get_user(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    decoded = jwt.decode(token, '@v^+tcurenaeo=u0cuorgi0(8*9xalx7g2sz0np^u7j6@o&q_c')
    return CustomUser.objects.get(id=decoded['user_id'])

#로그인할때 추가 정보(type) 주기 위해
class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        print(orginal_response.data['user']['pk'])
        user = get_object_or_404(CustomUser,pk=orginal_response.data['user']['pk'])
        mydata = {"user_type": user.type} #user type넣기
        orginal_response.data.update(mydata)
        return orginal_response

# User의 세부정보받기
class RegisterDetail(APIView):
    def post(self, request):
        user = get_user(request) #jwt에서 user읽기
        #print(user)
        body=request.data
        if body["type"]=="gym":
            user.type="gym"
            user.save()
            Gym.objects.create(
                user=user,
                address=body["address"],
                address_detail=body["address_detail"],
                logo=body["logo"],
                website=body["website"],
                profile1=body["profile1"],
                profile2=body["profile2"],
                profile3=body["profile3"],
                gym_name=body["gym_name"],
                price_desc=body["price_desc"],
            )
        else:
            user.type="dieter"
            user.save()
            Dieter.objects.create(
                user=user,
                address=body["address"],
                profile=body["profile"],
            )

        return Response({'detail':'success'},status=200)