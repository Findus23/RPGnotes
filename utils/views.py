from django.http import JsonResponse
from sorl.thumbnail import get_thumbnail

from characters.models import Character
from locations.models import Location
from loot.models import Loot
from utils.markdown import html_to_text


class JSONResponseMixin:
    def render_to_response(self, context, **kwargs):
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context, **kwargs)
        else:
            return super().render_to_response(context, **kwargs)

    def render_to_json_response(self, context, **response_kwargs):
        response = JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

        response['Cache-Control'] = f'max-age={24 * 60 * 60}'
        return response

    def get_data(self, context):
        object: Character = context["object"]
        description_list = []
        image = None
        if isinstance(object, Location):
            if object.parent:
                description_list.append(f"in {object.parent}")
        elif isinstance(object, Loot):
            if object.owner:
                description_list.append(object.owner.name)
            if object.location:
                description_list.append(object.location.name)
            if object.value_gold:
                description_list.append(f"{object.value_gold} gold")
            if object.magic_item:
                description_list.append("magic")
        if object.description_html:
            description_list.append(html_to_text(object.description_html))
        if hasattr(object, "smaller_image") and object.smaller_image:
            image = get_thumbnail(object.smaller_image, "200").url
        if hasattr(object, "image") and object.image:
            image = get_thumbnail(object.image, "200").url
        description = ", ".join([t for t in description_list if t])
        return {
            "name": object.name,
            "description": description,
            "image": image
        }
