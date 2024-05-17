from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from assessment.models import Post
from assessment.serializers import PostSerializer

# Question 2: Add any imports you need here

from assessment.filters import PostFilterSet


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Question 2: Update this class to use your filterset
    filterset_class = PostFilterSet

    def get_queryset(self):
        queryset = super(PostViewSet, self).get_queryset()
        if self.request.user.is_anonymous or self.request.GET.get("all") == "true":
            return queryset

        return queryset.filter(author=self.request.user)


# No changes are required to this class
class WhoAmIView(APIView):
    def get(self, request):
        return Response(
            {"username": None if request.user.is_anonymous else request.user.username}
        )