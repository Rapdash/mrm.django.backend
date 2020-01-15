from .models import Branch, Account
from .serializers import 
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView

class ListBranchesView(ListAPIView):
  queryset = Branch.objects.all()
  serializer_class = BranchSerializer
  permission_classes = (IsAuthenticated,)

class CreateBranchesView(CreateAPIView):
  queryset = Branch.objects.all()
  s