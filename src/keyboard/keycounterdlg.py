from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton
from src.keyboard.keycounter import KeyCounter
import matplotlib.pyplot as plt
import matplotlib
import src.utils.filemanager as f_mgr
import src.utils.timer as timer

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class KeyCounterDlg(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.graphic_view = None
        self.bar_chart_btn = None
        self.key_counter = KeyCounter()
        self.init_ui()
        self.hide()

    def init_ui(self):
        self.setWindowTitle("KeyCounter")
        main_lyt = QGridLayout()
        all_kinds_chart_btn = QPushButton()
        all_kinds_chart_btn.setText("ALL Charts")
        all_kinds_chart_btn.clicked.connect(self.show_bar_chart)
        main_lyt.addWidget(all_kinds_chart_btn, 0, 0)

        self.setLayout(main_lyt)

    def show_bar_chart(self):
        self.graphic_view = QtWidgets.QGraphicsView()

        canvas = QtableFigureCanvas()
        canvas.show_today_keys_barchart()
        graphic_scene = QtWidgets.QGraphicsScene()
        graphic_scene.addWidget(canvas)
        self.graphic_view.setScene(graphic_scene)
        self.graphic_view.show()

        pass


class QtableFigureCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)

    def show_today_keys_barchart(self):
        today_key_data = f_mgr.read_data_from(timer.get_today_date_str() + ".txt")
        x = today_key_data.keys()
        y = today_key_data.values()
        width = 0.4
        self.axes.bar(x, y, width, align="center")
        self.axes.set_ylabel("Key Count")
