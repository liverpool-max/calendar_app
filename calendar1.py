import sys
from PySide6.QtWidgets import (
    QCheckBox,QApplication,QCalendarWidget, QWidget, QVBoxLayout, QLabel, QLineEdit,QStackedWidget, QComboBox, QButtonGroup, QPushButton, QMessageBox,QMainWindow
)
from PySide6.QtCore import QTimer, Qt


class  MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar example")
        self.resize(600,400)

        self.stacked_widget = QStackedWidget()
        self.calendar_widget = QWidget()
        calendar_layout = QVBoxLayout()

        layout = QVBoxLayout()

        self.label = QLabel()

        self.calendar = QCalendarWidget()
        self.button = QPushButton("Click me",self)
        self.button.clicked.connect(self.on_click)

        calendar_layout.addWidget(self.calendar)
        calendar_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.calendar_widget.setLayout(calendar_layout)

        self.date_widget = QWidget()
        self.label = QLabel()
        date_layout = QVBoxLayout()
        date_layout.addWidget(self.label,alignment=Qt.AlignCenter)
        self.date_widget.setLayout(date_layout)

        self.stacked_widget.addWidget(self.calendar_widget)
        self.stacked_widget.addWidget(self.date_widget)
        self.setCentralWidget(self.stacked_widget)
        self.button.clicked.connect(self.on_click)


        

    def on_click(self):
        selected_data = self.calendar.selectedDate().toString()
        self.label.setText(selected_data)
        self.stacked_widget.setCurrentWidget(self.date_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

