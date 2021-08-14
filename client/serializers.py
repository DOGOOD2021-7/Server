from rest_framework import serializers



class ShopSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like')  # user가 특정 shop에 찜을 했는지

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'minprice', 'profile', 'like')