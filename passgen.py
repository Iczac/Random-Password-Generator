import generator as gen
from generator import InvalidLengthError
from generator import GenFail
import time

gen = gen.Generator()

def main():


    on_board = True

    while (on_board):
        print('')
        print('Generator')
        print('_________')
        print('?~ Current Generator Config ~?')
        print('Password Length - ' + str(gen.get_length()))
        print('Include Lowercase - ' + str('Yes' if gen.get_lower() else 'No'))
        print('Include Uppercase - ' + str('Yes' if gen.get_upper() else 'No'))
        print('Include Numbers - ' + str('Yes' if gen.get_numbers() else 'No'))
        print('Include Special Characters - ' + str('Yes' if gen.get_special_char() else 'No'))
        print('-------')
        print(
            '<Commands>\n1 - Set Password Length\n2 - Toggle Lower Case\n3 - Toggle Upper Case\n4 - Toggle Numbers\n5 - Toggle Special Characters\n6 - Generate a Password')
        choice = input('Please enter your command\n')
        if choice == '1':
            sub_error = True
            while (sub_error):
                value = input('Please enter your desired password length. (*Must be at least 6 Characters long*)\n')
                if int(value) >= 6:
                    gen.set_length(int(value))
                    sub_error = False
                else:
                    print('Invalid Length. Must be at least 6 Characters long')
                    print('')
        elif choice == '2':
            if gen.get_lower():
                gen.set_lower(False)
            else:
                gen.set_lower(True)
        elif choice == '3':
            if gen.get_upper():
                gen.set_upper(False)
            else:
                gen.set_upper(True)
        elif choice == '4':
            if gen.get_numbers():
                gen.set_numbers(False)
            else:
                gen.set_numbers(True)
        elif choice == '5':
            if gen.get_special_char():
                gen.set_special_char(False)
            else:
                gen.set_special_char(True)
        elif choice == '6':
            if gen.check():
                on_board = False
            else:
                print('Password must contain at least one of these properties - Upper,Lower,Numbers,Special Characters')
                time.sleep(4)

    error = True
    while (error):
        try:
            print('Generating Password.....')
            time.sleep(3)
            print('Generated Password - ' + str(gen.generate()))
            print('')
            sub_error = True
            while (sub_error):
                choice = input('Do you want to generate again? Y/N\n')
                if choice.upper() == 'Y':
                    error = True
                    sub_error = False
                elif choice.upper() == 'N':
                    print('Thanks for using PassGenPy')
                    error = False
                    sub_error = False
                else:
                    print('Please enter valid command')

        except InvalidLengthError as e:
            print(e)
        except GenFail as e:
            print(e)


if __name__ == "__main__":
    main()

