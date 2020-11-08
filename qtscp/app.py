# -- coding: utf8 --

from PyQt5 import QtWidgets
from __init__ import __version__
from PIL import Image

import qtscp
import aboutqt
import aboutapp
import aboutscp

import pkg_resources
import requests
import pyscp
import sys
import re
import os


s = "\\" if os.name == "nt" else "/"
path = os.path.dirname(os.path.abspath(__file__))


scp = pyscp.wikidot.Wiki('http://scpfoundation.net')


def fixHTML(code):
    return code.replace("<", "&lt;").replace(">", "&gt;")


class QtSCP(QtWidgets.QMainWindow, qtscp.Ui_MainWindow):
    def __init__(self):
        super(QtSCP, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda a: self.getSCP(self.lineEdit.text()))
        self.actionAbout_Qt.triggered.connect(self.about_qt)
        self.actionAbout_QtSCP.triggered.connect(self.about_app)
        self.actionAbout_SCP.triggered.connect(self.about_scp)

        self.textBrowser.installEventFilter(self)

    def about_qt(self):
        modal = AboutQt()
        modal.exec_()

    def about_app(self):
        modal = AboutApp()
        modal.exec_()

    def about_scp(self):
        modal = AboutSCP()
        modal.exec_()

    def resizeEvent(self, event):
        s = self.size()
        btns = self.pushButton.width()
        self.lineEdit.resize(s.width() - btns - 30, self.lineEdit.height())
        self.pushButton.move(s.width() - btns - 10, 10)
        self.textBrowser.resize(s.width(), s.height() - 60)

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

        test = ["Объект №:", "Класс объекта:", "Примеры объектов:", "Описание:", "Особые условия содержания:", r"^Приложение \d{,1}:", r"^Доктор .{,10}:", r"^Д-р .{,10}:", r"^█{,10}:", "Приложение:", "Опрашивающий:", "Опрашиваемый:", "Вступительное слово:", "<Начало записи>", "<Конец записи>", "Рекомендации:", "Выдержка из разбора операции с персоналом:", r"^Приложение .{,10}:", r"^Документ .{,10}:", "ПРЕДУПРЕЖДЕНИЕ:", "ОБЩЕЕ УВЕДОМЛЕНИЕ 001-Альфа:", "КОДОВОЕ ИМЯ:"]

        try:
            for number, string in enumerate(text):
                if string.find("рейтинг:") != -1:
                    del(text[number])

            for number, string in enumerate(text):
                for k in test:
                    try:
                        s = re.search(k, string)
                    except:
                        s = False

                    if s:
                        o = string.split(":")[0]
                        text[number] = text[number].replace(o, "<b>" + o + "</b>")

                    elif "&lt;" in string and "&gt;" in string:
                        text[number] = text[number].replace(fixHTML(k), "<b>" + fixHTML(k) + "</b>")

                    elif string.find(k) != -1:
                        text[number] = text[number].replace(o, "<b>" + o + "</b>")

            if text[0] == "":
                del(text[0])

            if len(images) != 0:
                del(text[0])

            text = "\n".join(text)

        except Exception as e:
            print(e)
            text = "\n".join(text)

        if len(p.images) != 0:
            image = p.images[0]

            r = requests.get(image)
            ext = image.split(".")[-1]

            with open(f"cache{s}image.{ext}", "wb") as img:
                img.write(r.content)

            im = Image.open(f"cache{s}image.{ext}")
            (w, h) = im.size

            if w > 420:
                w = 420

            image_html = f"<p style='text-align: center;'><img src='cache{s}image.{ext}' width='{w}'></p>\n\n"
        else:
            image_html = ""

        title = fixHTML(p.title.replace('/n/n', '').replace('\n', ''))

        msg = f"<div style='margin: 10;'><span style='font-size:20pt; font-weight:900;'>{title}</span>\n\n{image_html}<span style='font-size:11pt'>{text}</span></div>"
        # msg = msg.replace("</b>\n\n<b>", "</b>\n<b>")
        # print(msg)
        # for a in dir(self.textBrowser):
        #     print(a)
        self.textBrowser.setText(msg.replace("\n", "<br/>"))


class AboutQt(QtWidgets.QDialog, aboutqt.Ui_Dialog):
    def __init__(self):
        super(AboutQt, self).__init__()
        self.setupUi(self)

        try:
            qt_version = pkg_resources.get_distribution("PyQt5").version
        except:
            qt_version = "5"

        self.label_2.setText(f'<span style="font-size:24pt; font-weight:400;"><span style="color:#41cd52;">Qt</span> {qt_version}')
        self.pushButton.clicked.connect(self.close)


class AboutApp(QtWidgets.QDialog, aboutapp.Ui_Dialog):
    def __init__(self):
        super(AboutApp, self).__init__()
        self.setupUi(self)

        self.label_2.setText(f'<span style="font-size:24pt; font-weight:496;"><span style="color:#41cd52">Qt</span>SCP</span> <span style="font-size:18pt; font-weight:400;">{__version__}</span>')
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
