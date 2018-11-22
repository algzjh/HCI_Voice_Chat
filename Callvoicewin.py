# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QStyleFactory
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QIcon
from voice import *
from tts import *
from playmp3 import *
from turing import *
from genRecord import *
import asr_json

class MyMainWindow(QMainWindow, Ui_MainWindow):
	msg_id = 0
	after_my_msg_signal = pyqtSignal(str)

	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.initUI()
		# self.thread = Worker()

	def initUI(self):
		self.setWindowTitle('VoiceChat')
		self.setWindowIcon(QIcon('./images/icon1.png'))
		# self.playButton.clicked.connect(self.aftereClickedPlayBtn)
		self.sendMsgLineEdit.returnPressed.connect(self.readMyMessage)
		self.after_my_msg_signal.connect(self.responseMyMessage)
		self.play_PushButton_3.clicked.connect(self.doRecord)


	def text2Voice(self, msg, id):
		print('msg: ',msg, 'id: ', id)
		my_per = self.perComboBox.currentIndex()
		my_vol = self.volHorizontalSlider.value()
		my_sdp = self.sdpHorizontalSlider_2.value()
		my_pit = self.pitHorizontalSlider_3.value()
		if my_per >= 2:
			my_per = my_per + 1
		print("my_per: ",my_per," my_vol: ",my_vol,"my_sdp: ",my_sdp,"my_pit: ",my_pit)
		mp3_path = text2Mp3(msg, id, my_per, my_vol, my_sdp, my_pit)
		print('mp3_path: ', mp3_path)
		playMp3(mp3_path)

	def responseMyMessage(self, msg):
		response_msg = get_response(msg)
		self.chatTextEdit.append("Robot: "+response_msg)

		# my_per = self.perComboBox.currentIndex()
		# my_vol = self.volHorizontalSlider.value()
		# my_sdp = self.sdpHorizontalSlider_2.value()
		# my_pit = self.pitHorizontalSlider_3.value()
		# if my_per >= 2:
		# 	my_per = my_per + 1
		# respondThread = Worker(args= (response_msg, self.msg_id, my_per, my_vol, my_sdp, my_pit,))
		# respondThread.start()
		# respondThread.wait()

		self.text2Voice(response_msg, self.msg_id)
		self.msg_id = self.msg_id + 1

	def readMyMessage(self):
		msg = self.sendMsgLineEdit.text()
		self.sendMsgLineEdit.clear()
		self.chatTextEdit.append("Me: "+msg)

		# my_per = self.perComboBox.currentIndex()
		# my_vol = self.volHorizontalSlider.value()
		# my_sdp = self.sdpHorizontalSlider_2.value()
		# my_pit = self.pitHorizontalSlider_3.value()
		# if my_per >= 2:
		# 	my_per = my_per + 1
		# readThread = Worker(args = (msg, self.msg_id, my_per, my_vol, my_sdp, my_pit,))
		# readThread.start()
		# readThread.wait()

		self.text2Voice(msg, self.msg_id)
		self.msg_id = self.msg_id + 1
		self.after_my_msg_signal.emit(msg)

	def doRecord(self):
		print("Begin to record.........")
		r = GenAudio()
		r.read_audio()
		r.save_wav("./test.wav")
		result_dic = asr_json.getText()
		result_dic = eval(result_dic)
		print("result_dic: ",result_dic)
		print(type(result_dic))
		if "result" in result_dic.keys():
			my_word = result_dic["result"]
		else:
			my_word = "录音失败"
		print("my_word: ", my_word[0][:-1])
		self.sendMsgLineEdit.clear()
		self.sendMsgLineEdit.setText(my_word[0][:-1])




class Worker(QThread):
	# worker_trigger = pyqtSignal()
	def __init__(self, args):
		super(Worker, self).__init__()
		self.args = args
		# self.message = msg
		# self.idnum = id
		# self.my_per = per
		# self.my_vol = vol
		# self.my_sdp = sdp
		# self.my_pit = pit

	def run(self):
		print("This is Thread")
		print(self.args)
		mp3_path = text2Mp3(self.args[0], self.args[1], self.args[2], self.args[3], self.args[4], self.args[5])
		print(mp3_path)
		playMp3(mp3_path)
		# self.worker_trigger.emit()

if __name__=="__main__":
	app = QApplication(sys.argv)
	QApplication.setStyle(QStyleFactory.create('Fusion'))
	myWin = MyMainWindow()  
	myWin.show()  
	sys.exit(app.exec_())  