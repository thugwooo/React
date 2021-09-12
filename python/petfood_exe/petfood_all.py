import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import make_division 
import make_feed_arr 
import recommend

division = make_division.make_division()
feed_arr = make_feed_arr.make_feed(division)

form_class = uic.loadUiType("C:/Users/india/OneDrive/바탕 화면/code/파이썬/petfood_exe/petfood.ui")[0]

breed_num = 9
liked = []
unliked = []
alle = []
size_num = 0
when = []

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
        if self.breed_1.isChecked() : breed_num = 1
        elif self.breed_2.isChecked() : breed_num = 2
        elif self.breed_3.isChecked() : breed_num = 3
        elif self.breed_4.isChecked() : breed_num = 4
        elif self.breed_5.isChecked() : breed_num = 5
        elif self.breed_6.isChecked() : breed_num = 6
        elif self.breed_7.isChecked() : breed_num = 7
        elif self.breed_8.isChecked() : breed_num = 8
        elif self.breed_9.isChecked() : breed_num = 9
        elif self.breed_10.isChecked() : breed_num = 0
        



    def likedFunction(self):
        if self.like_1.isChecked() : liked.append(0)
        if self.like_2.isChecked() : liked.append(1)
        if self.like_3.isChecked() : liked.append(2)
        if self.like_4.isChecked() : liked.append(3)
        if self.like_5.isChecked() : liked.append(4)
        if self.like_6.isChecked() : liked.append(5)
        if self.like_7.isChecked() : liked.append(6)
        if self.like_8.isChecked() : liked.append(7)
        if self.like_9.isChecked() : liked.append(8)
        if self.like_10.isChecked() : liked.append(9)
        if self.like_11.isChecked() : liked.append(10)
        if self.like_12.isChecked() : liked.append(11)
        if self.like_13.isChecked() : liked.append(12)
        if self.like_14.isChecked() : liked.append(-1)
        return liked

    def unlikedFunction(self):
        if self.unlike_1.isChecked() : unliked.append(0)
        if self.unlike_2.isChecked() : unliked.append(1)
        if self.unlike_3.isChecked() : unliked.append(2)
        if self.unlike_4.isChecked() : unliked.append(3)
        if self.unlike_5.isChecked() : unliked.append(4)
        if self.unlike_6.isChecked() : unliked.append(5)
        if self.unlike_7.isChecked() : unliked.append(6)
        if self.unlike_8.isChecked() : unliked.append(7)
        if self.unlike_9.isChecked() : unliked.append(8)
        if self.unlike_10.isChecked() : unliked.append(9)
        if self.unlike_11.isChecked() : unliked.append(10)
        if self.unlike_12.isChecked() : unliked.append(11)
        if self.unlike_13.isChecked() : unliked.append(12)
        if self.unlike_14.isChecked() : unliked.append(-1)

    def allFunction(self):
        if self.all_1.isChecked() : alle.append(0)
        if self.all_2.isChecked() : alle.append(1)
        if self.all_3.isChecked() : alle.append(2)
        if self.all_4.isChecked() : alle.append(3)
        if self.all_5.isChecked() : alle.append(4)
        if self.all_6.isChecked() : alle.append(5)
        if self.all_7.isChecked() : alle.append(6)
        if self.all_8.isChecked() : alle.append(7)
        if self.all_9.isChecked() : alle.append(8)
        if self.all_10.isChecked() : alle.append(9)
        if self.all_11.isChecked() : alle.append(10)
        if self.all_12.isChecked() : alle.append(11)
        if self.all_13.isChecked() : alle.append(12)
        if self.all_14.isChecked() : alle.append(13)
        if self.all_15.isChecked() : alle.append(14)
        if self.all_16.isChecked() : alle.append(15)
        if self.all_17.isChecked() : alle.append(-1)

    def sizeFunction(self):
        if self.size_1.isChecked() : size_num = 1
        elif self.size_2.isChecked() : size_num = 2
        elif self.size_3.isChecked() : size_num = 3
        elif self.size_4.isChecked() : size_num = 4
        elif self.size_5.isChecked() : size_num = 5

    def whenFunction(self):
        if self.when_1.isChecked() : when.append(1)
        if self.when_2.isChecked() : when.append(2)
        if self.when_3.isChecked() : when.append(3)
        if self.when_4.isChecked() : when.append(0)

    def clickbutton(self):
        year = self.year_1.toPlainText()

        input_data = [breed_num, liked, unliked, alle, size_num, int(year), when]

        recommend_feed = recommend.recommend_feed(input_data, division, feed_arr)
        recommend_feed_str = ""
        for feed in recommend_feed :
                recommend_feed_str = recommend_feed_str + '\n' + feed['name']


        self.food_1.setText(recommend_feed_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
