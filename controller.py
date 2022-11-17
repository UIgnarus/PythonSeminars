import controller
import view
def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    controller.init(value_a, value_b)
    result = controller.sum
    