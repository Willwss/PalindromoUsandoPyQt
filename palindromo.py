import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Verificador de Palíndromo")
        self.setGeometry(600, 600, 600, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.entrada = QLineEdit(self)
        layout.addWidget(self.entrada)

        self.resultado = QLabel(self)
        layout.addWidget(self.resultado)

        botao = QPushButton("Verificar Palíndromo", self)
        botao.clicked.connect(self.verificar_palindromo)
        layout.addWidget(botao)

    def verificar_palindromo(self):
        palavra = self.entrada.text().strip()
        if not palavra:
            self.resultado.setText("Por favor, insira uma palavra.")
        else:
            self.resultado.setText("A palavra é um palíndromo." if eh_palindromo(palavra) else "A palavra não é um palíndromo.")

app = QApplication(sys.argv)
janela = JanelaPrincipal()
janela.show()
sys.exit(app.exec_())
