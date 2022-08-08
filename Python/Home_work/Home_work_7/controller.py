# связующее звено между всеми модулями

import model_rational as r
import model_complex as c
import view
import menu as m
import log
import output as o

def button_click():
    print(m.poisnenie)
    name = m.input_name()
    x = m.calc_menu()
    while x != 4:
        if x == 2: 
            a = view.get_value()
            result = r.my_eval(a)
            o.output_of_result(a, result)
            s = 'Имя пользователя: ' + name + '; ' + 'Выражение: ' + a + '; ' 'Результат: ' + str(result)
            log.log_data(s)
        elif x == 3: 
            a = view.get_value()
            result = c.parentheses(c.list_of_numbers_and_operations(a))
            o.output_of_result(a, result)
            s = 'Имя пользователя: ' + name + '; ' + 'Выражение: ' + a + '; ' 'Результат: ' + str(result)
            log.log_data(s)
        x = m.calc_menu()
    else:
        print('Выход из программы')
