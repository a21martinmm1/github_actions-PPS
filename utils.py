# Crea un programa Python que resolva o reto FizzBuzz, onde existirá unha función que reciba como parámetro un número e devolverá “fizz” para valores divisibles por 3, “buzz” para valores divisibles por 5 e “ fizz buzz” para valores divisibles ao mesmo tempo por 3 e 5.
# Crea as probas necesarias para probar o código anterior.


# Creamos a función que comproba se o número é divisible entre 3 e 5, entre 3 só, entre 5 só ou ningún
def fizzbuzz(num):
    # if num % 3 == 0:
    #     if num % 5 == 0:
    #         return "fizz buzz"
    #     else:
    #         return "fizz"
    # else:
    #     if num % 5 == 0:
    #         return "buzz"
    #     else:
    #         return False
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return False
