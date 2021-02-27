import json

from django.views import View
from django.http  import JsonResponse

from .models import *

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        result     = []
        
        for category in categories:
            my_dict = {
                'name' : category.name,
                'menu' : category.menu.name
            }
            result.append(my_dict)
            
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data     = json.loads(request.body)
        menu     = Menu.objects.get(name=data['menu'])
        category = Category.objects.create(
            name = data["name"],
            menu = menu
        )
        
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

class DrinkView(View):
    def get(self, request):
        drinks = Drink.objects.all()
        result = []
        
        for drink in drinks:
            my_dict = {
                'korean_name'  : drink.korean_name,
                'englshi_name' : drink.english_name,
                'description'  : drink.description,
                'category'     : drink.category.name
                
            }
            result.append(my_dict)
        
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.get(name=data['category'])
        drink = Drink.objects.create(
            korean_name  = data["korean_name"],
            english_name = data["english_name"],
            description  = data["description"],   
            category     = category         
        )
        
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status=201)


class ImageView(View):
    def get(self, request):
        images = Image.objects.all()
        result = []
        
        for image in images:
            my_dict = {
                'image_url' : image.image_url,
                'drink'     : image.drink.korean_name
            }
            result.append(my_dict)
            
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data  = json.loads(request.body)
        drink = Drink.objects.get(korean_name=data['drink'])
        image = Image.objects.create(
            image_url = data["image_url"],
            drink     = drink 
        )
        # 위에 name 주의
        # URL 추가 시 꼭 = 다음에 띄어쓰기 쓰지 않기
        
        return JsonResponse({"MESSEGE" : "SUCCESS"}, status=201)

class NutritionView(View):
    def get(self, request):
        nutritions = Nutrition.objects.all()
        result = []
        
        for nutrition in nutritions:
            my_dict = {
                'one_serving_kcal' : nutrition.one_serving_kcal,
                'sodium_mg'        : nutrition.sodium_mg,
                'saturated_fat_g'  : nutrition.saturated_fat_g,
                'sugars_g'         : nutrition.sugars_g,
                'protein_g'        : nutrition.protein_g,
                'caffeine_mg'      : nutrition.caffeine_mg,
                'size_ml'          : nutrition.size_ml,
                'size_fluid_ounce' : nutrition.size_fluid_ounce,
                'drink'            : nutrition.drink.korean_name
            }
            result.append(my_dict)
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data      = json.loads(request.body)
        drink     = Drink.objects.get(korean_name=data['drink'])
        nutrition = Nutrition.objects.create(
                one_serving_kcal = data["one_serving_kcal"],
                sodium_mg        = data['sodium_mg'],
                saturated_fat_g  = data['saturated_fat_g'],
                sugars_g         = data['sugars_g'],
                protein_g        = data['protein_g'],
                caffeine_mg      = data['caffeine_mg'],
                size_ml          = data['size_ml'],
                size_fluid_ounce = data['size_fluid_ounce'],
                drink            = drink
        )
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)
        # 양 쪽 다 오탈자 주의
        
class AllergyDrinkView(View):
    def get(self, request):
        allergies = Allergy_drink.objects.all()
        result    = []
        
        for allergy in allergies:
            my_dict={
                'allergy_drink' : allergy.allergy_drink.id,
                'drink'         : allergy.drink.id
            }
            # name으로 바꾸면 알러지와 음료 이름이 매칭 된다.
            result.append(my_dict)
        return JsonResponse({'result' : result}, status = 200)
    
    def post(self, request):
        data  = json.loads(request.body)
        name  = Allergy.objects.get(name=data['allergy_drink'])
        #가져오려는 클래스가 Allergy였으므로 name이 맞고 데이터 상에는 'allery_drink'니까
        drink         = Drink.objects.get(korean_name=data['drink'])
        allergy_drink = Allergy_drink.objects.create(
            allergy_drink = name,
            drink         = drink
            # 실제 httpie에서 받는 값(실제 쿼리가 변화되는 과정이므로)
            # (추측) id값으로 하면 어떨까? ; 쿼리에러남
            #products.models.Allergy.DoesNotExist: Allergy matching query does not exist.
        )   # 생각해보니 클라이언트는 아이디값을 알 리가 없다.
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status=201)