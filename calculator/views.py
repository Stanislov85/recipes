from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_viems(request):
    template_name = 'calculator/home.html'
    recept_list = list(DATA.keys())
    pages = {k: ( k + '/') for k in recept_list }

    context = {
        'pages' : pages
    }
    return render(request, template_name, context = context)

def recept_viems(request,recept):
    template_name = 'calculator/index.html'
    if recept in DATA:
        ingridients = DATA[recept]
        servings = request.GET.get('servings')
        if servings:
            summa = {}
            for key,value in ingridients.items():
                quantity = value * int(servings)
                summa[key] = quantity
                context = {
                    'recept' : recept,
                    'recipe' : summa
                }
        else:
            context = {
                'recept': recept,
                'recipe': ingridients
                      }
    else:
            context = None
    return render(request,template_name, context=context)