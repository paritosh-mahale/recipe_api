from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Recipe
# Create your views here.


class RecipeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        recipe = Recipe.objects.all()
        recipe_name = self.request.query_params.get('recipe_name', None)

        if recipe_name is not None:
            recipe = recipe.filter(recipe_name__icontains=recipe_name)

        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response({'message': 'Recipe added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response({'message': 'Recipe deleted successfully'}, status=status.HTTP_200_OK)

