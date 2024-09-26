from pynput import keyboard
from PyQt5.QtWidgets import QDialog
import src.utils.filemanager as fm
import src.utils.timer as timer


class KeyCounter:
    def __init__(self):
        self.key_map = {}
        self.exit_key = keyboard.Key.esc
        self.listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release)
        self.shortcut = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+h': self.on_activate_h,
            '<ctrl>+<alt>+i': self.on_activate_i,
            '<ctrl>+<c>': self.on_ctrl_c,
            '<ctrl>+<v>': self.on_ctrl_v})

    def load_data(self, data):
        self.key_map = data

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def start_with_join(self):
        self.listener.join()

    def setting_exit_key(self, key):
        self.exit_key = key

    def __on_press(self, key):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            self.key_map[key.char] += 1
        except AttributeError:
            print('special key {0} pressed'.format(key))
            self.key_map[key] += 1

    def __on_release(self, key):
        # print('{0} released'.format(key))
        if key == self.exit_key:
            return False

    def on_activate_h(self):
        print('<ctrl>+<alt>+h pressed')

    def on_activate_i(self):
        print('<ctrl>+<alt>+i pressed')

    def on_ctrl_c(self):
        print('<ctrl>+c pressed')

    def on_ctrl_v(self):
        print('<ctrl>+v pressed')

    def enable_shortcut(self):
        self.shortcut.start()


class KeyCounterDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(self, parent)
        self.bar_chart_btn = None
        self.key_counter = KeyCounter()
        self.key_counter.load_data(fm.read_data_from(timer.get_today_date_str() + ".txt"))
        self.key_counter.start()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("KeyCounter")

    def run_background(self):
        pass
