from django import template
from ..models import UserFoodList
register = template.Library()

@register.filter
def get_item_by_rand(user_food_list, rand_value):
    try:
        return user_food_list.get(rand=rand_value)
    except UserFoodList.DoesNotExist:
        return None