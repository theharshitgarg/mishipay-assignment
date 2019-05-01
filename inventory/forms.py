from django import forms
from utils import shopify


class ProductCreationForm(forms.Form):
    title = forms.CharField(
            label="Name",
            max_length=100,
            widget=forms.TextInput)
    body_html = forms.CharField(
        label="Description",
        max_length=1000,
        widget=forms.Textarea)
    vendor = forms.CharField(
        label="Vendor",
        max_length=20,
        widget=forms.TextInput)
    ProductType = forms.CharField(
        label="Product Type",
        max_length=100,
        widget=forms.TextInput)
    Published = forms.BooleanField(
        label="Is Published",
        required=False)


    @property
    def request_json(self):
        return {
            "product": self.cleaned_data,
        }

    def create_product(self):
        response = shopify.create_product(self.request_json)
        errors = {}
        data = {}
        success = True

        if response.status_code != 201:
            success = False
            errors = json.loads(response.content.decode('utf-8'))

        json_resp = {
            "success": success,
            "errors": errors,
            "data": data,
        }

        return json_resp
