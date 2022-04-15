from django import forms


class mahajan(forms.Form):

    num1=forms.IntegerField(label="enter number",max_value=2000)
