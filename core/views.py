from rest_framework.authentication import BasicAuthentication

class LoginView(KnoxLoginView):
  authentication_classes = (BasicAuthentication,)
