import sys
from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import (
    QDesktopServices,
    QPixmap,
    QPainter,
    QPainterPath
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)


# =========================================================
# ITEM CLICÁVEL
# =========================================================

class LinkItem(QFrame):

    def __init__(self, icon_text, title, value, url):
        super().__init__()

        self.url = url

        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName("linkItem")

        layout = QHBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(14)

        # Ícone
        self.icon_box = QLabel(icon_text)

        self.icon_box.setAlignment(Qt.AlignCenter)
        self.icon_box.setFixedSize(42, 42)

        self.icon_box.setObjectName("iconBox")

        # Área dos textos
        text_layout = QVBoxLayout()

        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(2)

        # Título
        self.title_label = QLabel(title)
        self.title_label.setObjectName("itemTitle")

        # Informação
        self.value_label = QLabel(value)
        self.value_label.setObjectName("itemValue")

        text_layout.addWidget(self.title_label)
        text_layout.addWidget(self.value_label)

        layout.addWidget(self.icon_box)
        layout.addLayout(text_layout)

        layout.addStretch()

    # Quando clicar no item
    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            QDesktopServices.openUrl(
                QUrl(self.url)
            )

        super().mousePressEvent(event)


# =========================================================
# FOTO CIRCULAR
# =========================================================

class AvatarWidget(QWidget):

    def __init__(self, caminho_imagem, tamanho=150):
        super().__init__()

        self.tamanho = tamanho

        self.imagem = QPixmap(
            str(caminho_imagem)
        )

        self.setFixedSize(
            tamanho,
            tamanho
        )

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        painter.setRenderHint(
            QPainter.SmoothPixmapTransform
        )

        # Cria o formato circular
        circulo = QPainterPath()

        circulo.addEllipse(
            0,
            0,
            self.tamanho,
            self.tamanho
        )

        # Recorta a imagem no formato do círculo
        painter.setClipPath(circulo)

        # Caso a imagem exista
        if not self.imagem.isNull():

            foto = self.imagem.scaled(
                self.tamanho,
                self.tamanho,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            # Centralização
            x = (
                foto.width() - self.tamanho
            ) // 2

            y = (
                foto.height() - self.tamanho
            ) // 2

            painter.drawPixmap(
                0,
                0,
                foto,
                x,
                y,
                self.tamanho,
                self.tamanho
            )


# =========================================================
# JANELA
# =========================================================

class PerfilWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Perfil")

        self.resize(
            560,
            720
        )

        self.setup_ui()
        self.apply_style()

    # =====================================================
    # INTERFACE
    # =====================================================

    def setup_ui(self):

        # Layout principal
        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            12,
            12,
            12,
            12
        )

        # Card
        card = QFrame()

        card.setObjectName("card")

        card_layout = QVBoxLayout(card)

        card_layout.setContentsMargins(
            48,
            40,
            48,
            38
        )

        card_layout.setSpacing(12)

        card_layout.setAlignment(
            Qt.AlignTop
        )

        # =================================================
        # FOTO
        # =================================================

        caminho_foto = (
            Path(__file__).parent
            / "foto_perfil.jpg"
        )

        avatar = AvatarWidget(
            caminho_foto,
            150
        )

        card_layout.addWidget(
            avatar,
            alignment=Qt.AlignCenter
        )

        card_layout.addSpacing(10)

        # =================================================
        # NOME
        # =================================================

        nome = QLabel(
            "João Guilherme Zonfrilli"
        )

        nome.setAlignment(
            Qt.AlignCenter
        )

        nome.setObjectName("nome")

        card_layout.addWidget(nome)

        # =================================================
        # USUÁRIO
        # =================================================

        usuario = QLabel(
            "@joao.ramos"
        )

        usuario.setAlignment(
            Qt.AlignCenter
        )

        usuario.setObjectName(
            "usuario"
        )

        card_layout.addWidget(usuario)

        # =================================================
        # DESCRIÇÃO
        # =================================================

        descricao = QLabel(
            "Desenvolvedor de Software • Python • PySide6"
        )

        descricao.setAlignment(
            Qt.AlignCenter
        )

        descricao.setWordWrap(True)

        descricao.setObjectName(
            "descricao"
        )

        card_layout.addWidget(
            descricao
        )

        card_layout.addSpacing(14)

        # =================================================
        # LINHA
        # =================================================

        linha = QFrame()

        linha.setFrameShape(
            QFrame.HLine
        )

        linha.setObjectName(
            "linha"
        )

        card_layout.addWidget(
            linha
        )

        card_layout.addSpacing(14)

        # =================================================
        # LINKEDIN
        # =================================================

        linkedin = LinkItem(
            "in",
            "LinkedIn",
            "linkedin.com/in/joaoguilhermezmr",
            "https://www.linkedin.com/in/joaoguilhermezmr/"
        )

        # =================================================
        # GITHUB
        # =================================================

        github = LinkItem(
            "</>",
            "GitHub",
            "github.com/gui60hz",
            "https://github.com/gui60hz"
        )

        # =================================================
        # WHATSAPP
        # =================================================

        whatsapp = LinkItem(
            "☎",
            "WhatsApp",
            "(67) 99294-1206",
            "https://wa.me/5567992941206"
        )

        # =================================================
        # INSTAGRAM
        # =================================================

        instagram = LinkItem(
            "◎",
            "Instagram",
            "@jota.pxd",
            "https://www.instagram.com/jota.pxd"
        )

        # Adicionando os itens
        card_layout.addWidget(
            linkedin
        )

        card_layout.addWidget(
            github
        )

        card_layout.addWidget(
            whatsapp
        )

        card_layout.addWidget(
            instagram
        )

        # Adiciona card na janela
        main_layout.addWidget(card)

    # =====================================================
    # ESTILIZAÇÃO
    # =====================================================

    def apply_style(self):

        self.setStyleSheet("""

            QWidget {

                background-color: #0f172a;

                color: white;

                font-family: "Segoe UI";

            }


            /* CARD */

            #card {

                background-color: #1b2940;

                border: 1px solid #274266;

                border-radius: 22px;

            }


            /* NOME */

            #nome {

                color: #66ebff;

                font-size: 24px;

                font-weight: 700;

                background: transparent;

            }


            /* USUÁRIO */

            #usuario {

                color: #a7b6cc;

                font-size: 14px;

                background: transparent;

            }


            /* DESCRIÇÃO */

            #descricao {

                color: #f2f5f9;

                font-size: 14px;

                background: transparent;

            }


            /* LINHA */

            #linha {

                color: #314760;

                background-color: #314760;

                max-height: 1px;

                border: none;

            }


            /* ITEM CLICÁVEL */

            #linkItem {

                background-color: transparent;

                border-radius: 12px;

                padding: 6px;

            }


            #linkItem:hover {

                background-color:
                    rgba(255, 255, 255, 0.04);

            }


            /* ÍCONE */

            #iconBox {

                background-color: #334763;

                color: #59d7ff;

                border-radius: 10px;

                font-size: 18px;

                font-weight: bold;

            }


            /* TÍTULO */

            #itemTitle {

                color: #aebad0;

                font-size: 14px;

                background: transparent;

            }


            /* LINK */

            #itemValue {

                color: #ffffff;

                font-size: 15px;

                font-weight: 600;

                background: transparent;

            }

        """)


# =========================================================
# EXECUÇÃO
# =========================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = PerfilWindow()

    window.show()

    sys.exit(
        app.exec()
    )