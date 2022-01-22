import time
import sys
import libdaq
import xlwt
import datetime
import math
from ctypes import *
from PyQt5.QtWidgets import *
from device import *
from mohao2 import Ui_Micrometer
from PyQt5 import QtWidgets

file = xlwt.Workbook()
sheet1 = file.add_sheet(u'sheet 1', cell_overwrite_ok=True)

def adc1_config_channel(device):
    ch_range=libdaq.CHANNEL_RANGE_0_P5V
    ch_couplemode=libdaq.ADC_CHANNEL_DC_COUPLE
    ch_refground=libdaq.ADC_CHANNEL_REFGND_RSE

    for channel in range(0,4):
        device.ADC1.config_channel_ex(channel,ch_range,ch_couplemode,ch_refground)

def adc1_sync_mode_example(device):
    class MyPyQT_Form(QtWidgets.QWidget,Ui_Micrometer):
        def __init__(self):
            super(MyPyQT_Form, self).__init__()
            self.setupUi(self)
            self.i=1
            self.lin=1 #excel数据保存行的变量
            self.col=3 #excel数据保存列的变量
            self.k=1 #组变量
            self.j=1 #测点数变量
            self.station_name='' #站点名数据
            self.pushButton_5.clicked.connect(self.getText)
            self.words=''
            self.textEdit_5.setText('')

        def getText(self):
            self.textEdit_5.setText('')
            text1, ok = QInputDialog.getText(self, '请输入站点', '起始站：')
            text2, ok = QInputDialog.getText(self, '请输入站点', '终点站：')
            self.lineEdit.setText('测试区间：'+str(text1) + '到' + str(text2))
            self.station_name = str(text1)+str(text2)
            #print(self.station_name)

        def start(self):
            channellist = [0, 2]

            sample_mode = libdaq.ADC_SAMPLE_MODE_SYNC
            frequency = 10000  # 1kHz
            cycles = 10

            group_interval = 0

            device.ADC1.set_sample_parameter_ex(channellist, sample_mode, frequency, cycles, group_interval)
            device.ADC1.clear_buffer()
            device.ADC1.send_trigger()
            time.sleep(2)
            data_len = cycles * len(channellist)
            (errorcode, result) = device.ADC1.read_analog(data_len)
            # print(result)
            a = result[0:20:2]
            b = result[1:20:2]
            aaa = 0
            bbb = 0
            for aa in range(0, len(a)):
                aaa = aaa + a[aa]
                # print(aaa)
            for bb in range(0, len(b)):
                bbb = bbb + b[bb]
            aav = aaa / cycles
            bav = bbb / cycles
            agg = "%2.4f " % (-3.82725 * (aav) + 0.752)
            bgg = "%2.4f " % (-3.82725 * (bav) + 1.178)
            self.textEdit_2.setText(str(agg))
            self.textEdit_4.setText(str(bgg))

            # 写入数据从 0 开始计数
            sheet1.write(0, 0, "第%d组测量"% (self.k))  # 第1行，第1列
            sheet1.write(1, 0, "测点")  # 第1行，第1列
            sheet1.write(1, 1, "垂磨量")  # 第1行，第2列
            sheet1.write(1, 2, "侧磨量")  # 第1行，第2列
            sheet1.write(self.lin+1, 0, self.lin)  # 第2行，第1列
            sheet1.write(self.lin+1, 1, agg)  # 第2行，第2列
            sheet1.write(self.lin+1, 2, bgg)  # 第2行，第2列

            self.lin += 1
            self.col += 1
            curr_time = datetime.datetime.now()
            time_str = curr_time.strftime("%Y%m%d")
            ttt=str(time_str)
            file.save(ttt+self.station_name+"区间的第" + str(self.k) + "组数据.xls")  #文件命名
            self.textEdit_5.setText('第%d组测量 第%d个测点\n数据已自动保存成功！\n该组测量垂磨量和侧磨量如上面对话框所示\n如该组数据有异常，请点击删除当前组数据按钮，并点击测量按钮再次测量' % (self.k,self.j))
            self.j+=1

        def delete(self):
            self.j -= 1
            self.textEdit_5.setText('第%d组测量 第%d个测点的数据删除成功！\n请点击测量按钮再次测量该测点！' % (self.k, self.j))
            self.lin -= 1

        def next(self):
            self.j=self.k+1
            self.textEdit_5.setText('第%d组数据测量结束，\n第%d组数据测量开始！'%(self.k,self.j))
            self.j=1
            self.k+=1
            self.lin=1
            for i in range(1000):
                sheet1.write(i, 0, "")  # 第1行，第2列
                sheet1.write(i, 1, "")  # 第1行，第2列
                sheet1.write(i, 2, "")  # 第1行，第2列


        def new(self): #还原行列，组数，测点数
            self.i=1
            self.lin=1 #excel数据保存行的变量
            self.col=3 #excel数据保存列的变量
            self.k=1 #组变量
            self.j=1 #测点数变量
            self.station_name='' #站点名数据
            self.textEdit_5.setText('操作成功！！请输入新的站点区间信息！')
            self.lineEdit.setText('')
            for i in range(1000):
                sheet1.write(i, 0, "")  # 第1行，第2列
                sheet1.write(i, 1, "")  # 第1行，第2列
                sheet1.write(i, 2, "")  # 第1行，第2列

#'<span style=\" color: #ff0000;\">%s</span>' % （XXXX）-----XXXX红色
        def info(self):
            self.words=('-----------------------------------欢迎使用-----------------------------------\n'
                                '\n按钮功能说明：'
                                '\n\n请输入站点：点击后会弹出输入框，请依次输出起始站点和终点站'
                                '\n\n测量：当你将速测磨耗尺固定好之后，点击一次测量，垂磨量和侧磨量将显示出来，并自动保存'
                                '\n\n删除当前测点：点击后，自动保存的上一组数据将被删除'
                                '\n\n开始下一组：在同一个测试区段如果有多组测试，请在测试完第一组后点击一下该按钮，软件将会创建一个新的文件'
                                '\n\n开始新的区段：当前区段测试完成后，点击一下会清空区段信息，这时需要输入新的区段信息'
                                '\n\n保存并退出：保存测试过的所有数据为.xls格式，并自动命名，格式为：年月日+区段名+的第X组测试\n'
                                '\n--------------------------------感谢使用本产品--------------------------------')

            self.textEdit_5.setText(self.words)


        def end(self):
            sys.exit()
    if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        demo = MyPyQT_Form()
        demo.show()
        sys.exit(app.exec_())

    class Child(QMainWindow, Ui_Child):
        def __init__(self):
            super(Child, self).__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(self.close)

        def OPEN(self):
            self.show()

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = Main()
        ch = Child()
        main.show()
        main.pushButton.clicked.connect(ch.OPEN)
        sys.exit(app.exec_())

def main_example():
    #传感器内置函数
    index=0
    libdaq.libdaq_init()
    device_count=libdaq.libdaq_device_get_count()
    if(device_count < 0 ):
        print("no device detected!\n")
        return
    device_name = create_string_buffer(b'0', 100)
    libdaq.libdaq_device_get_name(index,byref(device_name),len(device_name))
    print("device: %s deteced"%(device_name.value))
    device=libdaq.DAQUSB1141(device_name)
    device.DAC1.set_value(0)
    device.DAC2.set_value(5.0)
    adc1_config_channel(device)
    adc1_sync_mode_example(device)

if __name__ == '__main__':
    main_example()