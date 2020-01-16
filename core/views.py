from rest_framework.authentication import BasicAuthentication
from knox.views import LoginView as KnoxLoginView

class LoginView(KnoxLoginView):
  authentication_classes = (BasicAuthentication,)
