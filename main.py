if __name__ == "__main__":

    # task one
    # name = input("введіть своє ім'я")
    # print(введіть свій вік")
    # while True:
    #     try:
    #         age = int(input())
    #         if age > 130:
    #             print("вік занадто великий, спробуйте ще раз")
    #         elif age < 0:
    #             print("вік не може бути меншим за нуль, спробуйте ще раз")
    #
    #         else:
    #             break
    #     except ValueError:
    #         print("вам слід ввести вік у цілих цифрах, спробуйте ще раз")
    # print(f"Привіт, {name}! Твій вік — {age}")


    # task two ver one
    # def greet_user(name, age):
    #     return f"Привіт, {name}! Твій вік — {age}"
    #
    #
    # if __name__ == "__main__":
    #     name = input("Введіть ваше ім'я: ")
    #     print("Введіть ваш вік: ")
    #
    #     while True:
    #         try:
    #             age = int(input())
    #             if age > 130:
    #                 print("Це занадто великий вік, спробуйте ще раз")
    #             elif age < 0:
    #                 print("Вік не може бути менше нуля, спробуйте ще раз")
    #             else:
    #                 break
    #         except ValueError:
    #             print("Ви повинні ввести вік у форматі числа, спробуйте ще раз")
    #
    #     result = greet_user(name, age)
    #     print(result)

    # task two ver two
    # def greet_user(name, age):
    #     try:
    #         age = int(age)
    #         if age > 130:
    #             return "Це занадто великий вік, спробуйте ще раз"
    #         elif age < 0:
    #             return "Вік не може бути менше нуля, спробуйте ще раз"
    #         else:
    #             return f"Привіт, {name}! Твій вік — {age}"
    #     except ValueError:
    #         return "Ви повинні ввести вік у форматі числа, спробуйте ще раз"
    #
    #
    # if __name__ == "__main__":
    #     name = input("Введіть ваше ім'я: ")
    #     age = input("Введіть ваш вік: ")
    #
    #     result = greet_user(name, age)
    #     print(result)


    # task three
    # numbers = []
    #
    # while True:
    #     try:
    #         num = float(input("Введіть додатне число (або введіть '0' для завершення): "))
    #         if num == 0:
    #             break
    #         elif num < 0:
    #             raise ValueError("Введено від'ємне число")
    #         numbers.append(num)
    #     except ValueError as e:
    #         print(f"Помилка: {e}")
    #
    # if not numbers:
    #     print("Список чисел порожній.")
    # else:
    #     total = sum(numbers)
    #     print(f"Сума всіх додатних чисел: {total}")


    # task four ver one
    def calculate_sum(numbers):
        return sum(numbers)


    if __name__ == "__main__":
        numbers = []
        while True:
            try:
                num = float(input("Введіть число (або '0' для завершення вводу): "))
                if num == 0:
                    break
                numbers.append(num)
            except ValueError as e:
                print(f"Помилка: {e}")

        total = calculate_sum(numbers)
        print(f"Сума елементів списку: {total}")


    # task four ver two
    # def calculate_sum(numbers):
    #     try:
    #         total = sum(numbers)
    #         return total
    #     except ValueError as e:
    #         raise ValueError("Помилка при обчисленні суми: " + str(e))
    #
    #
    # if __name__ == "__main__":
    #     numbers = []
    #     while True:
    #         try:
    #             num = float(input("Введіть число (або '0' для завершення вводу): "))
    #             if num == 0:
    #                 break
    #             numbers.append(num)
    #         except ValueError as e:
    #             print(f"Помилка: {e}")
    #
    #     try:
    #         total = calculate_sum(numbers)
    #         print(f"Сума елементів списку: {total}")
    #     except ValueError as e:
    #         print(f"Помилка: {e}")

    # to commit