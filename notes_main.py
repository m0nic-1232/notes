from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox,QButtonGroup,QRadioButton,
    QPushButton,QLabel,QListWidget,QTextEdit,QLineEdit,QInputDialog)
import json




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Умные заметки')
btn_1 = QPushButton('Создать заметку')
btn_2 = QPushButton('Удалить заметку')
btn_3 = QPushButton('Сохранить заметку')
btn_4 = QPushButton('Добавить к заметке')
btn_5 = QPushButton('Открепить от заметки')
btn_6 = QPushButton('Искать заметки по тегу')
field_1 = QTextEdit()
field_2 = QListWidget()
field_3 = QListWidget()
listt_of_tegs = QLabel('Список тегов')
listt_of_notes = QLabel('Список заметок')
write_teg = QLineEdit()
write_teg.setPlaceholderText('Введите тег...')
horizontal1 = QHBoxLayout()
horizontal2 = QHBoxLayout()
horizontal3 = QHBoxLayout()
horizontal4 = QHBoxLayout()
vertical1 = QVBoxLayout()
vertical1.addWidget(field_1)
vertical2 = QVBoxLayout()
vertical2.addWidget(listt_of_notes)
vertical2.addWidget(field_2)
horizontal1.addWidget(btn_1)
horizontal1.addWidget(btn_2)
horizontal2.addWidget(btn_3)
vertical2.addLayout(horizontal1)
vertical2.addLayout(horizontal2)
vertical2.addWidget(listt_of_tegs)
vertical2.addWidget(field_3)
vertical2.addWidget(write_teg)
horizontal3.addWidget(btn_4)
horizontal3.addWidget(btn_5)
horizontal4.addWidget(btn_6)

vertical2.addLayout(horizontal3)
vertical2.addLayout(horizontal4)
final_line = QHBoxLayout()
final_line.addLayout(vertical1)
final_line.addLayout(vertical2)
main_win.setLayout(final_line)

'''
notes = {
    'Добро пожаловать': {
        'текст': 'В этом приложении можно создавать заметки с тегами',
        'теги': ['умные заметки','инструкция']
    
            },
    'Инструкция': {
        'текст': 'Не забывайте сохранять заметки при выходе из приложения!😁',
        'теги' : ['инструкция','помощь📣']
    }
    
}




with open('notes_data.json', 'w', encoding= 'utf-8') as file:
    json.dump(notes, file,ensure_ascii=False)
'''

with open('notes_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


field_2.addItems(data)


def show_note():
    name = field_2.selectedItems()[0].text()
    field_1.setText(data[name]['текст'])
    field_3.clear()
    field_3.addItems(data[name]['теги'])
field_2.itemClicked.connect(show_note)

def add_note():
    note_name, ok = QInputDialog.getText(main_win, 'Добавить заметку', 'Название заметки')
    if note_name != '':
        data[note_name] = {
            'текст': '',
            'теги': []
        }
        field_2.addItem(note_name)

btn_1.clicked.connect(add_note)



def save_note():
    if field_2.selectedItems():
        name = field_2.selectedItems()[0].text()
        text = field_1.toPlainText()
        data[name]['текст'] = text
        with open('notes_data.json', 'w', encoding= 'utf-8') as file:
            json.dump(data, file,ensure_ascii=False)
btn_3.clicked.connect(save_note)


def del_note():
    if field_2.selectedItems():
        name = field_2.selectedItems()[0].text()
        del data[name]
        with open('notes_data.json', 'w', encoding = 'utf-8') as file:
            json.dump(data,file,ensure_ascii=False)
        field_1.clear()
        field_2.clear()
        field_3.clear()
        field_2.addItems(data)
btn_2.clicked.connect(del_note)

def add_tag():
    if field_2.selectedItems():
        name = field_2.selectedItems()[0].text()
        text = write_teg.text()
        if not text in data[name]['теги']:
            data[name]['теги'].append(text)
            field_3.addItem(text)
            with open('notes_data.json', 'w', encoding = ' utf-8') as file:
                json.dump(data,file,ensure_ascii=False)
            write_teg.clear()
btn_4.clicked.connect(add_tag)

def del_tag():
    if field_3.selectedItems():
        name = field_2.selectedItems()[0].text()
        name_tag = field_3.selectedItems()[0].text()
        data[name]['теги'].remove(name_tag)
        with open('notes_data.json', 'w', encoding = 'utf-8') as file:
            json.dump(data,file,ensure_ascii=False)
        field_3.clear()
        field_3.addItems(data[name]['теги'])
btn_5.clicked.connect(del_tag)

def search_tag():
    if btn_6.text() == 'Искать заметки по тегу':
        text = write_teg.text()
        notes_filtered = {}
        for note in data:
            if text in data[note]['теги']:
                notes_filtered[note] = data[note]
        field_2.clear()
        field_2.addItems(notes_filtered)
        btn_6.setText('Сбросить поиск')
    elif btn_6.text() == 'Сбросить поиск':
        write_teg.clear()
        field_2.clear()
        field_2.addItems(data)
        btn_6.setText('Искать заметки по тегу')
btn_6.clicked.connect(search_tag)




        


















main_win.resize(700,400)
main_win.show()
app.exec_()
