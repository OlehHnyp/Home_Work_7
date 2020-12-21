import Home_Work_7_Task_1_implisit as im


figures_and_func = {'rectangle': 'im.rectangle_area()',
                    'triangle': 'im.triangle_area()',
                    'circle': 'im.circle_area()'}

figures_areas = {}

choice = set(input(
"""
Hi, I can help you to calculate area of \
triangle, rectangle and circle. Insert figures \
which area you want to calculate. Separate them \
by space:\
"""
).lower().split())

while True:
    if choice.issubset(set(figures_and_func.keys())):
        for fig in choice:
            figures_areas.update({fig: eval(figures_and_func.get(fig))})
        break
    else:
        choice = set(input("Try again:").lower().split())

print("Here is result:")

for el in figures_areas.items():
    print(f"{el[0]} area is {el[1]}")


