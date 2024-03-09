from django import template
import json

register = template.Library()

@register.filter(name='json_tag')
def convert_to_json(string_data):
    try:
        json_data = json.loads(string_data)
    except json.JSONDecodeError:
        json_data = {}
    return json_data
