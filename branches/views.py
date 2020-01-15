from .models import Branch, Account
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView

class ListBranchesView(ListAPIView):
  queryset = Branch.objects.all()
  permission_classes = (IsAuthenticated,)

class CreateBranchesView(CreateAPIView):
