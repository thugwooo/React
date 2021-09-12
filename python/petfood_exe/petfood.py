import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:/Users/india/OneDrive/바탕 화면/code/파이썬/petfood_exe/petfood.ui")[0]

breed_num = 9
liked = [0 for _ in range(14)]
unliked = [0 for _ in range(14)]
unliked = [0 for _ in range(17)]
size_num = 0
when = [0 for _ in range(4)]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        
        self.breed_1.clicked.connect(self.breedFunction)
        self.breed_2.clicked.connect(self.breedFunction)
        self.breed_3.clicked.connect(self.breedFunction)
        self.breed_4.clicked.connect(self.breedFunction)
        self.breed_5.clicked.connect(self.breedFunction)
        self.breed_6.clicked.connect(self.breedFunction)
        self.breed_7.clicked.connect(self.breedFunction)
        self.breed_8.clicked.connect(self.breedFunction)
        self.breed_9.clicked.connect(self.breedFunction)
        self.breed_10.clicked.connect(self.breedFunction)
        
        self.like_1.clicked.connect(self.likedFunction)
        self.like_2.clicked.connect(self.likedFunction)
        self.like_3.clicked.connect(self.likedFunction)
        self.like_4.clicked.connect(self.likedFunction)
        self.like_5.clicked.connect(self.likedFunction)
        self.like_6.clicked.connect(self.likedFunction)
        self.like_7.clicked.connect(self.likedFunction)
        self.like_8.clicked.connect(self.likedFunction)
        self.like_9.clicked.connect(self.likedFunction)
        self.like_10.clicked.connect(self.likedFunction)
        self.like_11.clicked.connect(self.likedFunction)
        self.like_12.clicked.connect(self.likedFunction)
        self.like_13.clicked.connect(self.likedFunction)
        self.like_14.clicked.connect(self.likedFunction)

        self.unlike_1.clicked.connect(self.unlikedFunction)
        self.unlike_2.clicked.connect(self.unlikedFunction)
        self.unlike_3.clicked.connect(self.unlikedFunction)
        self.unlike_4.clicked.connect(self.unlikedFunction)
        self.unlike_5.clicked.connect(self.unlikedFunction)
        self.unlike_6.clicked.connect(self.unlikedFunction)
        self.unlike_7.clicked.connect(self.unlikedFunction)
        self.unlike_8.clicked.connect(self.unlikedFunction)
        self.unlike_9.clicked.connect(self.unlikedFunction)
        self.unlike_10.clicked.connect(self.unlikedFunction)
        self.unlike_11.clicked.connect(self.unlikedFunction)
        self.unlike_12.clicked.connect(self.unlikedFunction)
        self.unlike_13.clicked.connect(self.unlikedFunction)
        self.unlike_14.clicked.connect(self.unlikedFunction)

        self.all_1.clicked.connect(self.allFunction)
        self.all_2.clicked.connect(self.allFunction)
        self.all_3.clicked.connect(self.allFunction)
        self.all_4.clicked.connect(self.allFunction)
        self.all_5.clicked.connect(self.allFunction)
        self.all_6.clicked.connect(self.allFunction)
        self.all_7.clicked.connect(self.allFunction)
        self.all_8.clicked.connect(self.allFunction)
        self.all_9.clicked.connect(self.allFunction)
        self.all_10.clicked.connect(self.allFunction)
        self.all_11.clicked.connect(self.allFunction)
        self.all_12.clicked.connect(self.allFunction)
        self.all_13.clicked.connect(self.allFunction)
        self.all_14.clicked.connect(self.allFunction)
        self.all_15.clicked.connect(self.allFunction)
        self.all_16.clicked.connect(self.allFunction)
        self.all_17.clicked.connect(self.allFunction)

        self.size_1.clicked.connect(self.sizeFunction)
        self.size_2.clicked.connect(self.sizeFunction)
        self.size_3.clicked.connect(self.sizeFunction)
        self.size_4.clicked.connect(self.sizeFunction)
        self.size_5.clicked.connect(self.sizeFunction)

        self.when_1.clicked.connect(self.whenFunction)
        self.when_2.clicked.connect(self.whenFunction)
        self.when_3.clicked.connect(self.whenFunction)
        self.when_4.clicked.connect(self.whenFunction)

        self.pushButton.clicked.connect(self.clickbutton)

    def breedFunction(self):            # 강아지 종
        if self.breed_1.isChecked() : breed_num = 0
        elif self.breed_2.isChecked() : breed_num = 1
        elif self.breed_3.isChecked() : breed_num = 2
        elif self.breed_4.isChecked() : breed_num = 3
        elif self.breed_5.isChecked() : breed_num = 4
        elif self.breed_6.isChecked() : breed_num = 5
        elif self.breed_7.isChecked() : breed_num = 6
        elif self.breed_8.isChecked() : breed_num = 7
        elif self.breed_9.isChecked() : breed_num = 8
        elif self.breed_10.isChecked() : breed_num = 9
        



    def likedFunction(self):
        if self.like_1.isChecked() : liked[0] = self.like_1.isChecked
        if self.like_2.isChecked() : liked[1] = self.like_2.isChecked
        if self.like_3.isChecked() : liked[2] = self.like_3.isChecked
        if self.like_4.isChecked() : liked[3] = self.like_4.isChecked
        if self.like_5.isChecked() : liked[4] = self.like_5.isChecked
        if self.like_6.isChecked() : liked[5] = self.like_6.isChecked
        if self.like_7.isChecked() : liked[6] = self.like_7.isChecked
        if self.like_8.isChecked() : liked[7] = self.like_8.isChecked
        if self.like_9.isChecked() : liked[8] = self.like_9.isChecked
        if self.like_10.isChecked() : liked[9] = self.like_10.isChecked
        if self.like_11.isChecked() : liked[10] = self.like_11.isChecked
        if self.like_12.isChecked() : liked[11] = self.like_12.isChecked
        if self.like_13.isChecked() : liked[12] = self.like_13.isChecked
        if self.like_14.isChecked() : liked[13] = self.like_14.isChecked
        return liked

    def unlikedFunction(self):
        if self.unlike_1.isChecked() : unliked[0] = self.unlike_1.isChecked
        if self.unlike_2.isChecked() : unliked[1] = self.unlike_2.isChecked
        if self.unlike_3.isChecked() : unliked[2] = self.unlike_3.isChecked
        if self.unlike_4.isChecked() : unliked[3] = self.unlike_4.isChecked
        if self.unlike_5.isChecked() : unliked[4] = self.unlike_5.isChecked
        if self.unlike_6.isChecked() : unliked[5] = self.unlike_6.isChecked
        if self.unlike_7.isChecked() : unliked[6] = self.unlike_7.isChecked
        if self.unlike_8.isChecked() : unliked[7] = self.unlike_8.isChecked
        if self.unlike_9.isChecked() : unliked[8] = self.unlike_9.isChecked
        if self.unlike_10.isChecked() : unliked[9] = self.unlike_10.isChecked
        if self.unlike_11.isChecked() : unliked[10] = self.unlike_11.isChecked
        if self.unlike_12.isChecked() : unliked[11] = self.unlike_12.isChecked
        if self.unlike_13.isChecked() : unliked[12] = self.unlike_13.isChecked
        if self.unlike_14.isChecked() : unliked[13] = self.unlike_14.isChecked

    def allFunction(self):
        if self.all_1.isChecked() : all[0] = self.all_1.isChecked
        if self.all_2.isChecked() : all[1] = self.all_2.isChecked
        if self.all_3.isChecked() : all[2] = self.all_3.isChecked
        if self.all_4.isChecked() : all[3] = self.all_4.isChecked
        if self.all_5.isChecked() : all[4] = self.all_5.isChecked
        if self.all_6.isChecked() : all[5] = self.all_6.isChecked
        if self.all_7.isChecked() : all[6] = self.all_7.isChecked
        if self.all_8.isChecked() : all[7] = self.all_8.isChecked
        if self.all_9.isChecked() : all[8] = self.all_9.isChecked
        if self.all_10.isChecked() : all[9] = self.all_10.isChecked
        if self.all_11.isChecked() : all[10] = self.all_11.isChecked
        if self.all_12.isChecked() : all[11] = self.all_12.isChecked
        if self.all_13.isChecked() : all[12] = self.all_13.isChecked
        if self.all_14.isChecked() : all[13] = self.all_14.isChecked
        if self.all_15.isChecked() : all[14] = self.all_15.isChecked
        if self.all_16.isChecked() : all[15] = self.all_16.isChecked
        if self.all_17.isChecked() : all[16] = self.all_17.isChecked

    def sizeFunction(self):
        if self.size_1.isChecked() : size_num = 0
        elif self.size_2.isChecked() : size_num = 1
        elif self.size_3.isChecked() : size_num = 2
        elif self.size_4.isChecked() : size_num = 3
        elif self.size_5.isChecked() : size_num = 4

    def whenFunction(self):
        if self.when_1.isChecked() : when[0] = self.when_1.isChecked()
        if self.when_2.isChecked() : when[1] = self.when_2.isChecked()
        if self.when_3.isChecked() : when[2] = self.when_3.isChecked()
        if self.when_4.isChecked() : when[3] = self.when_4.isChecked()

    def clickbutton(self):
        year = self.year_1.toPlainText()
        # 여기서 모듈 불러오기
        
        # self.food_1.setText(여기에 return값 넣기(stringtype))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
