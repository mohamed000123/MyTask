from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from products.models import Products
from users.models import User


class productsSer (serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class product_create (APIView):
    def post(self, request):
        try:
            product_name = request.data['product_name']
            product_price = request.data['product_price']
            product_seller = request.data['product_seller']
            user_id = request.user
            Products.objects.create(
                product_name=product_name, product_price=product_price,
                product_seller=product_seller, user_id=user_id)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({'details': 'error'},
                            status=status.HTTP_400_BAD_REQUEST)


class get_user_products (APIView):
    def get(self, request):
        try:
            logged_user = request.session.get('loggeduser', default=None)
            user_products = Products.objects.filter(user_id=logged_user['id'])
            user_products_ser = productsSer(user_products, many=True)
            return Response(user_products_ser.data)
        except:
            return Response({'details': 'error'},
                            status=status.HTTP_400_BAD_REQUEST)


class get_all_products (APIView):
    def get(self, request):
        try:
            products = Products.objects.all()
            products_ser = productsSer(products, many=True)
            return Response(products_ser.data)
        except:
            return Response({'details': 'error'},
                            status=status.HTTP_400_BAD_REQUEST)


class get_specific_products (APIView):
    def post(self, request):
        try:
            sort_by = request.data['order']
            seller = request.data['seller']
            get_seller = User.objects.get(username=seller)

            if sort_by == "decending":
                user_products = Products.objects.filter(
                    user_id=get_seller.id).order_by('-product_price')
            elif sort_by == 'Asending':
                user_products = Products.objects.filter(
                    user_id=get_seller.id).order_by('product_price')
            user_products_ser = productsSer(user_products, many=True)
            return Response(user_products_ser.data)
        except:
            return Response({'details': 'error'},
                            status=status.HTTP_400_BAD_REQUEST)
