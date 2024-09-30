from pynput import keyboard
from PyQt5.QtWidgets import QFrame, QFormLayout, QLabel
import src.utils.filemanager as f_mgr
import src.utils.timer as timer
import threading


class KeyCounter:
    def __init__(self):
        self.key_map: dict[str, int] = f_mgr.read_data_from(timer.get_today_date_str() + ".txt")

        self.save_data_thread = threading.Thread(
            target=f_mgr.run_interval_with, args=(f_mgr.write_today_log_with, self.key_map, "w"), daemon=True)
        self.stop_thread_event = threading.Event()

        self.exit_key = keyboard.Key.esc
        self.listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release)
        self.shortcut = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+h': self.on_activate_h,
            '<ctrl>+<alt>+i': self.on_activate_i,
            '<ctrl>+c': self.on_ctrl_c,
            '<ctrl>+v': self.on_ctrl_v})

        self.start()

    def __del__(self):
        self.stop()

    def load_data(self, data):
        self.key_map = data

    def save_data(self):
        f_mgr.write_today_log_with(self.key_map)

    def start(self):
        self.save_data_thread.start()
        self.listener.start()

    def stop(self):
        self.listener.stop()
        self.stop_thread_event.set()
        self.save_data()
        self.key_map.clear()

    def start_with_join(self):
        self.listener.join()

    def setting_exit_key(self, key):
        self.exit_key = key

    def __on_press(self, key):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            if key.char in self.key_map:
                self.key_map[key.char] += 1
            else:
                self.key_map[key.char] = 1
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            if key in self.key_map:
                self.key_map[key] += 1
            else:
                self.key_map[key] = 1

    def __on_release(self, key):
        # print('{0} released'.format(key))
        if key == self.exit_key:
            return False

    def on_activate_h(self):
        print('<ctrl>+<alt>+h pressed')
        pass

    def on_activate_i(self):
        print('<ctrl>+<alt>+i pressed')

    def on_ctrl_c(self):
        print('<ctrl>+c pressed')

    def on_ctrl_v(self):
        print('<ctrl>+v pressed')

    def enable_shortcut(self):
        self.shortcut.start()


class KeyCounterDlg(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bar_chart_btn = None
        self.key_counter = KeyCounter()
        self.init_ui()
        self.hide()

    def init_ui(self):
        self.setWindowTitle("KeyCounter")
        main_lyt = QFormLayout()
        lbl = QLabel("Test")
        main_lyt.addWidget(lbl)
        self.setLayout(main_lyt)
