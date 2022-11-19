import model
import view
import model_mult

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.sum()
    view.view_data(result)

def button_click2():
    value_a = view.get_value()
    value_b = view.get_value()
    model_mult.init(value_a, value_b)
    result = model_mult.mult()
    view.view_data(result)
    