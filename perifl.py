import sys
from pathlib import Path

from PySide6.QtCore import Qt, QUrl, QSize
from PySide6.QtGui import (
    QDesktopServices,
    QPixmap,
    QPainter,
    QPainterPath,
    QIcon
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton
)

import qtawesome as qta


# ============================================================
# CAMINHOS
# ============================================================

PASTA_PROJETO = Path(__file__).resolve().parent

CAMINHO_FOTO = PASTA_PROJETO / "assets" / "perfil.png"


# ============================================================
# BOTÃO DOS LINKS
# ============================================================

class LinkButton(QPushButton):

    def __init__(self, texto, url, icone, cor_icone):
        super().__init__()

        self.url = url

        self.setText(texto)

        # Mãozinha ao passar o mouse
        self.setCursor(Qt.PointingHandCursor)

        self.setFixedHeight(48)

        self.setIcon(
            qta.icon(
                icone,
                color=cor_icone
            )
        )

        self.setIconSize(
            QSize(25, 25)
        )

        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #d2d2da;

                border: none;

                font-size: 13px;

                text-align: left;

                padding: 5px 10px;
            }

            QPushButton:hover {
                background-color: #363641;

                color: white;

                border-radius: 8px;
            }
        """)

        self.clicked.connect(self.abrir_link)

    def abrir_link(self):

        QDesktopServices.openUrl(
            QUrl(self.url)
        )


# ============================================================
# JANELA
# ============================================================

class Perfil(QWidget):

    def __init__(self):
        super().__init__()

        self.configurar_janela()
        self.criar_interface()

    # ========================================================
    # JANELA
    # ========================================================

    def configurar_janela(self):

        self.setWindowTitle("Perfil")

        self.setFixedSize(
            500,
            650
        )

        # FOTO COMO ÍCONE DA JANELA
        self.setWindowIcon(
            QIcon(str(CAMINHO_FOTO))
        )

        # REMOVE O FUNDO BRANCO
        self.setStyleSheet("""
            QWidget {
                background-color: #202028;
            }
        """)

    # ========================================================
    # INTERFACE
    # ========================================================

    def criar_interface(self):

        layout_principal = QVBoxLayout(self)

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.setAlignment(
            Qt.AlignCenter
        )

        # ====================================================
        # CARD
        # ====================================================

        card = QFrame()

        card.setFixedSize(
            400,
            580
        )

        card.setObjectName("card")

        card.setStyleSheet("""
            QFrame#card {
                background-color: #292934;

                border-radius: 10px;
            }
        """)

        layout_card = QVBoxLayout(card)

        layout_card.setContentsMargins(
            45,
            25,
            45,
            30
        )

        layout_card.setSpacing(5)

        layout_card.setAlignment(
            Qt.AlignTop
        )

        # ====================================================
        # FOTO DE PERFIL
        # ====================================================

        area_foto = QWidget()

        area_foto.setFixedHeight(160)

        area_foto.setStyleSheet("""
            background-color: transparent;
        """)

        layout_foto = QHBoxLayout(area_foto)

        layout_foto.setAlignment(
            Qt.AlignCenter
        )

        layout_foto.setSpacing(15)

        # ----------------------------------------------------
        # PARÊNTESE ESQUERDO
        # ----------------------------------------------------

        esquerda = QLabel("(")

        esquerda.setStyleSheet("""
            QLabel {
                color: #637fd2;

                font-size: 120px;

                background-color: transparent;
            }
        """)

        # ----------------------------------------------------
        # FOTO
        # ----------------------------------------------------

        foto = QLabel()

        foto.setFixedSize(
            115,
            115
        )

        foto.setAlignment(
            Qt.AlignCenter
        )

        foto.setStyleSheet("""
            QLabel {
                background-color: transparent;
            }
        """)

        pixmap_foto = QPixmap(str(CAMINHO_FOTO))

        pixmap_foto = pixmap_foto.scaled(
            115,
            115,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        foto.setPixmap(pixmap_foto)

        # ----------------------------------------------------
        # PARÊNTESE DIREITO
        # ----------------------------------------------------

        direita = QLabel(")")

        direita.setStyleSheet("""
            QLabel {
                color: #637fd2;

                font-size: 120px;

                background-color: transparent;
            }
        """)

        layout_foto.addWidget(esquerda)

        layout_foto.addWidget(foto)

        layout_foto.addWidget(direita)

        # ====================================================
        # NOME
        # ====================================================

        nome = QLabel(
            "João Guilherme Zonfrilli"
        )

        nome.setAlignment(
            Qt.AlignCenter
        )

        nome.setStyleSheet("""
            QLabel {
                color: #6599e8;

                font-size: 21px;

                font-weight: bold;

                background-color: transparent;
            }
        """)

        # ====================================================
        # DESCRIÇÃO
        # ====================================================

        descricao = QLabel(
            "Desenvolvedor de Software • Python • PySide6"
        )

        descricao.setAlignment(
            Qt.AlignCenter
        )

        descricao.setWordWrap(True)

        descricao.setStyleSheet("""
            QLabel {
                color: #c2c2ca;

                font-size: 11px;

                background-color: transparent;
            }
        """)

        # ====================================================
        # ESPAÇO
        # ====================================================

        espaco = QWidget()

        espaco.setFixedHeight(15)

        espaco.setStyleSheet("""
            background-color: transparent;
        """)

        # ====================================================
        # LINKEDIN
        # ====================================================

        linkedin = LinkButton(
            "linkedin.com/in/joaoguilhermezmr",
            "https://www.linkedin.com/in/joaoguilhermezmr/",
            "fa5b.linkedin",
            "#0A66C2"
        )

        # ====================================================
        # GITHUB
        # ====================================================

        github = LinkButton(
            "github.com/gui60hz",
            "https://github.com/gui60hz",
            "fa5b.github",
            "#ffffff"
        )

        # ====================================================
        # WHATSAPP
        # ====================================================

        whatsapp = LinkButton(
            "(67) 99294-1206",
            "https://wa.me/5567992941206",
            "fa5b.whatsapp",
            "#25D366"
        )

        # ====================================================
        # INSTAGRAM
        # ====================================================

        instagram = LinkButton(
            "@jota.pxd",
            "https://www.instagram.com/jota.pxd",
            "fa5b.instagram",
            "#E1306C"
        )

        # ====================================================
        # ADICIONAR AO CARD
        # ====================================================

        layout_card.addWidget(area_foto)

        layout_card.addWidget(nome)

        layout_card.addWidget(descricao)

        layout_card.addWidget(espaco)

        layout_card.addWidget(linkedin)

        layout_card.addWidget(github)

        layout_card.addWidget(whatsapp)

        layout_card.addWidget(instagram)

        layout_principal.addWidget(card)

    # ========================================================
    # FOTO CIRCULAR
    # ========================================================

    def criar_foto_circular(self, caminho, tamanho):

        caminho = str(caminho)

        pixmap_original = QPixmap(caminho)

        # Verifica se encontrou a foto
        if pixmap_original.isNull():

            print("ERRO: Foto não encontrada!")

            print("O programa procurou aqui:")

            print(caminho)

            return QPixmap()

        pixmap_original = pixmap_original.scaled(
            tamanho,
            tamanho,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        resultado = QPixmap(
            tamanho,
            tamanho
        )

        resultado.fill(
            Qt.transparent
        )

        painter = QPainter(resultado)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        caminho_circular = QPainterPath()

        caminho_circular.addEllipse(
            0,
            0,
            tamanho,
            tamanho
        )

        painter.setClipPath(
            caminho_circular
        )

        painter.drawPixmap(
            0,
            0,
            pixmap_original
        )

        painter.end()

        return resultado


# ============================================================
# EXECUTAR
# ============================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # ÍCONE TAMBÉM DEFINIDO PARA O APLICATIVO
    app.setWindowIcon(
        QIcon(str(CAMINHO_FOTO))
    )

    janela = Perfil()

    janela.show()

    sys.exit(app.exec())