from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from rest_framework import status
from products.models import Products
from users.models import User


class productsSer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class product_create(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            product_name = request.data['product_name']
            product_price = request.data['product_price']
            product_seller = request.user
          

            Products.objects.create(
                product_name = product_name, product_price=product_price,
                product_seller = product_seller)
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise AuthenticationFailed('Unauthenticated!')


class get_user_products(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user_products = Products.objects.filter(
                product_seller = request.user)
            user_products_ser = productsSer(user_products, many=True)
            return Response(user_products_ser.data)
        else:
            raise AuthenticationFailed('Unauthenticated!')


class get_all_products(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            products = Products.objects.all
            products_ser = productsSer(products, many=True)
            return Response(products_ser.data)
        else:
            raise AuthenticationFailed('Unauthenticated!')


class get_specific_products(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.filter(
                username=request.data['user_name']).first
            sort_by = request.data['order']
            if sort_by == "decending":
                user_products = Products.objects.filter(
                    product_seller=user).order_by('-product_price')
            elif sort_by == 'Asending':
                user_products = Products.objects.filter(
                    product_seller=user).order_by('product_price')
            user_products_ser = productsSer(user_products, many=True)
            return Response(user_products_ser.data)
        else:
            raise AuthenticationFailed('Unauthenticated!')
