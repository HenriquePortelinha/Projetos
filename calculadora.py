from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLabel
from PySide6.QtCore import Qt

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFixedSize(400, 400)
        self.setWindowTitle("Calculadora")
        
      
        self.grid = QGridLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget)
        
        
        self.display = QLabel("0")
        self.display.setStyleSheet("font-size: 30px; qproperty-alignment: AlignRight;")
        self.display.setFixedHeight(50)
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        
       
        self.criar_botoes()
        
      
        self.expressao = ""

    def criar_botoes(self):

        botoes = {
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
            '0': (4, 0), '.': (4, 1), '=': (4, 2), '+': (4, 3),
            'CLEAR': (5, 0)
        }
        
        for texto, posicao in botoes.items():
            botao = QPushButton(texto)
            botao.setFixedSize(80, 80)
            self.grid.addWidget(botao, *posicao)
            if texto == '=':
                botao.clicked.connect(self.calcular)
            elif texto == 'CLEAR':
                botao.clicked.connect(self.limpar_display)
            else:
                botao.clicked.connect(lambda _, t=texto: self.atualizar_display(t))

    def atualizar_display(self, texto):
        if self.display.text() == "0" and texto not in "+-*/":
            self.display.setText(texto)
        else:
            self.display.setText(self.display.text() + texto)
        
    def calcular(self):
        try:
            expressao = self.display.text()
            resultado = eval(expressao)
            self.display.setText(str(resultado))
        except Exception:
            self.display.setText("Erro")

    def limpar_display(self):
        self.display.setText("0")
        self.expressao = ""

app = QApplication([])
window = Calculadora()
window.show()
app.exec()
