
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('home1/', index_view),
    path('booking/',booking_view),
    path('display/',display_view),
    path('update/<int:booking_id>/',update_view),
    path('delete/<int:booking_id>/',delete_view),
    path('photos/',photos),
    path('about/',about),
    path('hello/',hello),
    path('student/',getStudent),
    path('employee/',getEmployee),
    path('product/',getProduct),
    path('savestudent/',saveStudent),
    path('getinformation/<rollnumber>',getInformation),
    path('saveinformation',saveInformation),
    path('updateinformation',updateInformation),
    path('deleteinformation/<rollnumber>',deleteInformation),
    path('getallinformation',getALLInformation),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('addition', addition),
    path('', homepage),
    path('substraction', substraction),
    path('multiplication', multiplication),
    path('division', division),
    path('setsession', setsession),
    path('getsession', getsession),
    path('removesession', removesession),





]
