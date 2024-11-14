from flet import *


TAMANHO = 70
BORDA = 10

def main(page: Page):
    page.title = "Calculadora"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.window_height = 440
    page.window_width = 380

    operadores = {"+", "-", "x", "/"}

    display = TextField(value="", text_align=TextAlign.RIGHT, width=310, read_only=True, text_size=30)

    def click_botao(e):
        if display.value == "0":
            display.value = ""
        if display.value and display.value[-1] in operadores and e.control.data in operadores:
            return
        display.value += str(e.control.data)
        page.update()

    def click_limpar(e):
        display.value = ""
        page.update()

    def click_igual(e):
        display.value = str(eval(display.value.replace("x", "*")))
        page.update()

    page.add(
        Column([
            Row([
                display
            ], alignment= MainAxisAlignment.CENTER),
            Row([
                ElevatedButton("7", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, data=7, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("8", width =TAMANHO, height =TAMANHO, bgcolor = colors.BLUE_500, color = colors.WHITE, data =8, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("9", width =TAMANHO, height =TAMANHO, bgcolor = colors.BLUE_500, color = colors.WHITE, data =9, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("+", width =TAMANHO, height =TAMANHO, bgcolor = colors.BLUE_500, color = colors.WHITE, data ="+", on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA)))
            ], alignment= MainAxisAlignment.CENTER),
            Row([
                ElevatedButton("4", width =TAMANHO, height =TAMANHO, bgcolor = colors.BLUE_500, color = colors.WHITE, data =4, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("5", width =TAMANHO, height =TAMANHO, bgcolor = colors.BLUE_500, color = colors.WHITE, data =5, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("6", width =TAMANHO, height =TAMANHO, bgcolor = colors.BLUE_500, color = colors.WHITE, data =6, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("-", width =TAMANHO, height =TAMANHO, bgcolor = colors.BLUE_500, color = colors.WHITE, data ="-", on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA)))
            ], alignment= MainAxisAlignment.CENTER),
            Row([
                ElevatedButton("1", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, data=1, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("2", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, data=2, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("3", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, data=3, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("x", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, data="x", on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA)))
            ], alignment= MainAxisAlignment.CENTER),
            Row([
                ElevatedButton("C", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, on_click=click_limpar, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("0", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, data=0, on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("=", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, on_click=click_igual, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA))),
                ElevatedButton("÷", width=TAMANHO, height=TAMANHO, bgcolor=colors.BLUE_500, color=colors.WHITE, data="/", on_click=click_botao, style=ButtonStyle(shape=RoundedRectangleBorder(radius=BORDA)))
            ], alignment= MainAxisAlignment.CENTER),
        ])
    )

if __name__ == "__main__":
    app(target = main)