from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from products.models import Products
from users.models import User



class productsSer (serializers.ModelSerializer) :
    class  Meta:
        model = Products
        fields = "__all__"


class product_create (APIView):
    def post(self, request):
        
            product_name = request.data['product_name']
            product_price = request.data['product_price']
            product_seller = request.data['product_seller']
            user_id = request.user
            Products.objects.create(
                product_name=product_name, product_price=product_price,
                product_seller=product_seller, user_id=user_id)

  


class get_user_products (APIView):
      def get (self,request):
            lo_user = request.session.get('loggeduser',default=None)
            user_products = Products.objects.filter(user_id=lo_user['id'])
            user_products_ser=productsSer(user_products,many=True)
            return Response(user_products_ser.data)
        
      
 


class get_all_products (APIView):
      def get (self,request):
            
            products = Products.objects.all
            products_ser=productsSer(products,many=True)
            return Response(products_ser.data)
        
   


class get_specific_products (APIView):
      def post (self,request):
          
        
            lo_user = request.session.get('loggeduser',default=None)
            user= User.objects.get(id = lo_user['id'])
            
            sort_by = request.data['order']

            if sort_by == "decending" :
                user_products = Products.objects.filter(user_id=user).order_by('-product_price')
            elif sort_by == 'Asending' :
                user_products = Products.objects.filter(user_id=user).order_by('product_price')
            user_products_ser=productsSer(user_products,many=True)
            return Response(user_products_ser.data)