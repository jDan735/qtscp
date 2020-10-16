import sys
from PyQt5 import QtWidgets
from main import qtscp_design
from aboutqt import aboutqt
from aboutapp import aboutapp
from aboutscp import aboutscp
from __init__ import __version__, __qt_version__
from PyQt5 import QtCore
import pyscp
import re


scp = pyscp.wikidot.Wiki('http://scpfoundation.net')


def fixHTML(code):
    return code.replace("<", "&lt;").replace(">", "&gt;")


class QtSCP(QtWidgets.QMainWindow, qtscp_design.Ui_MainWindow):
    def __init__(self):
        super(QtSCP, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda a: self.getSCP(self.lineEdit.text()))
        self.actionAbout_Qt.triggered.connect(self.about_qt)
        self.actionAbout_QtSCP.triggered.connect(self.about_app)
        self.actionAbout_SCP.triggered.connect(self.about_scp)

    def about_qt(self):
        modal = AboutQt()
        modal.exec_()

    def about_app(self):
        modal = AboutApp()
        modal.exec_()

    def about_scp(self):
        modal = AboutSCP()
        modal.exec_()

    def getSCP(self, query):

        try:
            p = scp(query)
            p.title

        except:
            self.textBrowser.setText(f"<span style='font-size:20pt; font-weight:900; color: red;'>404</span><br/>Ребята, не стоит вскрывать эту тему. Вы молодые, шутливые, вам все легко. Это не то. Это не Чикатило и даже не архивы спецслужб. Сюда лучше не лезть. Серьезно, любой из вас будет жалеть. Лучше закройте тему и забудьте, что тут писалось. Я вполне понимаю, что данным сообщением вызову дополнительный интерес, но хочу сразу предостеречь пытливых - стоп. Остальные просто не найдут")
            return

        text = p.text

        # text = re.sub(r"рейтинг: ", "", p.text)

        text = fixHTML(text)
        text = re.sub(r"(\n\n\n|\n\n)", "\n", text)
        text = text.split("\n")

        images = p.images

        try:
            for number, string in enumerate(text):
                if string.find("рейтинг:") != -1:
                    del(text[number])

            for number, string in enumerate(text):
                test = ["Объект №:", "Класс объекта:", "Примеры объектов:", "Описание:", "Особые условия содержания:"]
                for k in test:
                    if string.find(k) != -1:
                        o = string.split(":")[0]
                        text[number] = text[number].replace(o, "<b>" + o + "</b>")

            if text[0] == "":
                del(text[0])

            if len(images) != 0:
                del(text[0])

            text = "\n".join(text)

        except Exception as e:
            print(e)
            text = "\n".join(text)

        title = fixHTML(p.title.replace('\n', ''))
        msg = f"<span style='font-size:20pt; font-weight:900;'>{title}</span>\n\n<span style='font-size:11pt'>{text}</span>"
        msg = msg.replace("</b>\n\n<b>", "</b>\n<b>")
        # print(msg)
        # for a in dir(self.textBrowser):
        #     print(a)
        self.textBrowser.setText(msg.replace("\n", "<br/>"))


class AboutQt(QtWidgets.QDialog, aboutqt.Ui_Dialog):
    def __init__(self):
        super(AboutQt, self).__init__()
        self.setupUi(self)

        self.label_3.setText(f"Version {__qt_version__}")
        self.pushButton.clicked.connect(self.close)


class AboutApp(QtWidgets.QDialog, aboutapp.Ui_Dialog):
    def __init__(self):
        super(AboutApp, self).__init__()
        self.setupUi(self)

        self.label_3.setText(f"Version {__version__}")
        self.pushButton.clicked.connect(self.close)


class AboutSCP(QtWidgets.QDialog, aboutscp.Ui_Dialog):
    def __init__(self):
        super(AboutSCP, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtSCP()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
