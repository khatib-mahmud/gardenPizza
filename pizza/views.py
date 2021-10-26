from django.http import response
from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaFrom
from django.forms import formset_factory
from .models import Pizza


def home(request): 
    return render(request, 'index.html', {})
    
def order(request):
    multiple_form = MultiplePizzaFrom()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Your %s, %s and %s pizza is on the way' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data.get('topping2'))
            new_form = PizzaForm()
            
            return render(request, 'order.html', {'created_pizza_pk':created_pizza_pk,'form':new_form ,'note':note,'multiple_form':multiple_form })
        else:
            note = 'something is worng try again'
            new_form = PizzaForm()
            return render(request, 'order.html', {'form':new_form , 'note':note })
            
    else:
        form = PizzaForm()
        return render(request, 'order.html', {'form':form,'multiple_form':multiple_form })


def pizza(request):

    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaFrom(request.GET)

    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)

    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'PIzza have been ordered'
        else:
            note = 'order not created'
        return render(request, 'pizza.html', {'note':note,'formset':formset})
    
    else:
        return render(request, 'pizza.html', {'formset':formset})
    


def edit_order(request,pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method =='POST':
        filled_form = PizzaForm(request.POST,instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
    return render(request, 'edit_order.html', {'pizza':pizza,'pizzaform':form})

