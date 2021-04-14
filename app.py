import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import matplotlib.pyplot as plt

import MainWindow as design

#design.setStylesheet("style.css")

import predict_cancer as pc
import predict_pneumonia as pp


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.filename = None
        # self.setStylesheet("style.css")
        self.setupUi(self)

        self.select_button.clicked.connect(self.get_files)
        self.analyze_button.clicked.connect(self.exec_script)
        

    @QtCore.pyqtSlot()
    def get_files(self):
        selected_filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File')
        self.filename = selected_filename
        self.path_label.setText("File: " + self.filename)
        print(f"[INFO] Filename: " + self.filename)

    @QtCore.pyqtSlot()
    def exec_script(self):
        curr_text = self.comboBox.currentText()
        print(f"[INFO] Selected opteion: {curr_text}")
        result_image = None

        if curr_text == "Pneumonia":
            result_image = pp.predict_image(self.filename)

        if curr_text == "Breast Cancer":
            result_image = pc.predict_image(self.filename)

        if result_image is not None:
            plt.imshow(result_image)
            plt.show()

        print(f"[INFO] Operation done")
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
