import my_module

my_module.greeting()
my_module.greeting('방구마')

from my_module import greeting
greeting('호구마')

from my_module import pi as p
print(my_module.pi)

print(p)