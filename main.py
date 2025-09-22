from flet import (
    Page,
    Column,
    Row,
    TextField,
    ElevatedButton,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextAlign,
    Colors,
    ButtonStyle,
    RoundedRectangleBorder,
    Text,
    app,
)
from calculator import Calculator
from history import HistoryManager

BTN_WIDTH = 70
BTN_HEIGHT = 70
BTN_BORDER_RADIUS = 10
BTN_TEXT_SIZE = 24

COLOR_NUMBERS = Colors.GREY_800
COLOR_OPERATORS = Colors.ORANGE_400
COLOR_CLEAR = Colors.RED_400
COLOR_EQUAL = Colors.GREEN_400

class CalculatorApp:
    def __init__(self, page: Page):
        self.page = page
        self.calculator = Calculator()
        self.history_manager = HistoryManager()
        self.display = TextField(
            value="0",
            text_align=TextAlign.RIGHT,
            read_only=True,
            text_size=30,
            width=310,
            border_color="transparent",
            bgcolor=Colors.BLACK,
            color=Colors.WHITE,
            border_radius=10,
        )
        self.full_expression = ""

    def build_ui(self):
        return Column(
            [
                Row([self.display], alignment=MainAxisAlignment.CENTER),
                Row(
                    [
                        ElevatedButton(
                            content=Text("7", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("8", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("9", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("+", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_OPERATORS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        ElevatedButton(
                            content=Text("4", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("5", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("6", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("-", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_OPERATORS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        ElevatedButton(
                            content=Text("1", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("2", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("3", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("x", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_OPERATORS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        ElevatedButton(
                            content=Text("C", size=BTN_TEXT_SIZE),
                            on_click=self.on_clear_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_CLEAR,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("0", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_NUMBERS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("=", size=BTN_TEXT_SIZE),
                            on_click=self.on_equals_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_EQUAL,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                        ElevatedButton(
                            content=Text("÷", size=BTN_TEXT_SIZE),
                            on_click=self.on_button_click,
                            width=BTN_WIDTH,
                            height=BTN_HEIGHT,
                            bgcolor=COLOR_OPERATORS,
                            color=Colors.WHITE,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=BTN_BORDER_RADIUS)),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=10,
        )

    def on_button_click(self, e):
        button_value = e.control.content.value
        if self.full_expression and self.full_expression[-1] in "+-x/" and button_value in "+-x/":
            return
            
        self.full_expression += button_value
        
        if button_value.isdigit():
            self.calculator.add_digit(button_value)
        else:
            self.calculator.add_operator(self._map_operator(button_value))
            
        self.display.value = self.calculator.get_display_value()
        self.page.update()

    def on_clear_click(self, e):
        self.calculator.clear()
        self.full_expression = ""
        self.display.value = "0"
        self.page.update()

    def on_equals_click(self, e):
        expression_to_save = self.full_expression
        
        self.calculator.equals()
        result = self.calculator.get_display_value()
        
        self.history_manager.save_calculation(expression_to_save, result) 
        
        self.display.value = result
        self.full_expression = result
        self.page.update()

    def _map_operator(self, op):
        if op == "x":
            return "*"
        if op == "÷":
            return "/"
        return op

def main(page: Page):
    page.title = "Calculadora"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.window_height = 440
    page.window_width = 380

    calc_app = CalculatorApp(page)
    page.add(calc_app.build_ui())

if __name__ == "__main__":
    app(target=main)