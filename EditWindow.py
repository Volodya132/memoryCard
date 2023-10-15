from  PyQt5.QtWidgets import *

import Question
def editWindow():
    window = QDialog()

    editBtn = QPushButton("Редагувати")

    questLbl = QLabel("Редагувати питання")
    questLbl1 = QLabel("Правильна відповідь")
    questLbl2 = QLabel("Неправильна відповідь")
    questLbl3 = QLabel("Неправильна відповідь")
    questLbl4 = QLabel("Неправильна відповідь")

    questEdit = QLineEdit(Question.qeust[Question.currentQuest]["питання"])
    questEdit1 = QLineEdit(Question.qeust[Question.currentQuest]["Правильна відповідь"])
    questEdit2 = QLineEdit(Question.qeust[Question.currentQuest]["не правильна1"])
    questEdit3 = QLineEdit(Question.qeust[Question.currentQuest]["не правильна2"])
    questEdit4 = QLineEdit(Question.qeust[Question.currentQuest]["не правильна3"])

    mainLine = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(questLbl)
    h1.addWidget(questEdit)

    h2 = QHBoxLayout()
    h2.addWidget(questLbl1)
    h2.addWidget(questEdit1)

    h3 = QHBoxLayout()
    h3.addWidget(questLbl2)
    h3.addWidget(questEdit2)

    h4 = QHBoxLayout()
    h4.addWidget(questLbl3)
    h4.addWidget(questEdit3)

    h5 = QHBoxLayout()
    h5.addWidget(questLbl4)
    h5.addWidget(questEdit4)

    h6 = QHBoxLayout()

    mainLine.addLayout(h1)
    mainLine.addLayout(h2)
    mainLine.addLayout(h3)
    mainLine.addLayout(h4)
    mainLine.addLayout(h5)
    mainLine.addLayout(h6)

    h6.addWidget(editBtn)

    def addEditFunc():
        Question.qeust[Question.currentQuest] = {

                "питання": questEdit.text(),
                "Правильна відповідь": questEdit1.text(),
                "не правильна1": questEdit2.text(),
                "не правильна2": questEdit3.text(),
                "не правильна3": questEdit4.text()
            }

        window.close()

    editBtn.clicked.connect(addEditFunc)
    window.setLayout(mainLine)
    window.show()
    window.exec()




