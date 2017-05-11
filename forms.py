from django import forms

class ContactMeForm (forms.Form):
    name = forms.CharField(label="Name: ", max_length=100)
    email = forms.EmailField(label="Email: ")
    question = forms.CharField(label="Question:", widget=forms.Textarea)

class PizzaPoll (forms.Form):
    PEPPERONI = 'pepperoni'
    MUSHROOMS = 'mushrooms'
    ONIONS = 'onions'
    SUASAGE = 'sausage'
    OLIVES = 'olives'
    PEPPERS = 'bell peppers'
    CHEESE = 'cheese'
    BEST_TOPPING = (
        (PEPPERONI, 'pepperoni'),
        (MUSHROOMS, 'mushrooms'),
        (ONIONS, 'onions'),
        (SUASAGE, 'sausage'),
        (OLIVES, 'olives'),
        (PEPPERS, 'bell peppers'),
        (CHEESE, 'cheese'),
    )

    choice = forms.ChoiceField(choices=BEST_TOPPING, widget=forms.RadioSelect())
