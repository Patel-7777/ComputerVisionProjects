
import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):
    
    def __init__(self, parent = None):
        super(window, self).__init__(parent)

        self.resize(1900, 970)
        self.setMinimumSize(QSize(804, 593))

        self.setStyleSheet("color:rgb(153, 0, 0);")
    

        
        self.frame=QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(0.8)
        self.frame.resize(1900,970)
        self.frame.setStyleSheet("background-image:url(back10_resize.jpg)")

        
        
        

        self.scaleFactor = 1.0
        
        
        self.label3 = QLabel(self)
        self.label3.setGeometry(80, 400, 200, 31)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(70)
        self.label3.setFont(font)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setText("OUTPUT IMAGE")


        self.label4 = QLabel(self)
        self.label4.setGeometry(80, 450, 1797, 497)
        self.label4.setStyleSheet("border: 2px solid white;\n"
                                "border-radius: 5px")
        self.label4.setText("")

        self.label4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label4.setScaledContents(True)
        self.label4.setStyleSheet("background:transparent;")
        
        
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidget(self.label4)

        self.scrollArea.setGeometry(80, 450, 1800, 500)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("background:transparent")
        
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setGeometry(50, 50, 1900, 120)

        self.verticalLayout =QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)



        self.Heading = QLabel(self.layoutWidget)

        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Heading)
        self.Heading.setText("Object Detection")
        
        self.label1 =QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(70)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label1)
        self.label1.setText("DEVELOPED  BY  DRASHTI FEFAR")
        
        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setGeometry(50, 250, 1000, 50)

        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(30, 0, 30, 0)


        self.label2 = QLabel(self.layoutWidget1)
        font =QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(70)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label2)
        self.label2.setText("SELECT  IMAGE")
        
        self.lineEdit = QLineEdit(self.layoutWidget1)

        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit.setStyleSheet("background:transparent;")
    
        self.browse = QPushButton(self.layoutWidget1)
        self.browse.setStyleSheet(*{"color:white;background-color: rgb(70, 73, 255);"})

        font =QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(70)
        self.browse.setFont(font)
        self.browse.clicked.connect(self.Open1)
        self.horizontalLayout.addWidget(self.browse)
        self.browse.setText("BROWSE")

        self.zoom_in = QPushButton(self)
        self.zoom_in.setStyleSheet(*{"color:white;background-color: rgb(70, 73, 255);"})

        self.zoom_in.clicked.connect(self.zoomIn)

        self.zoom_in.setText("+")
        font =QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(100)
        self.zoom_in.setFont(font)
        self.zoom_in.setGeometry(100, 460, 51, 30)
        
        self.zoom_out = QPushButton(self)
        self.zoom_out.setStyleSheet(*{"color:white;background-color: rgb(70, 73, 255);"})
        self.zoom_out.setObjectName("zoom_out")
        self.zoom_out.clicked.connect(self.zoomOut)
#         self.verticalLayout_2.addWidget(self.zoom_out)
        self.zoom_out.setText("-")
        font =QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(100)
        self.zoom_out.setFont(font)
        self.zoom_out.setGeometry(100, 500, 51, 30)
        

        
        self.button1=QPushButton("DETECT",self)
        self.button1.setGeometry(80,320,150,50)
        self.button1.clicked.connect(self.ObjectDetection)
        font =QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(70)
        self.button1.setFont(font)
        self.button1.setStyleSheet(*{"color:white;background-color: rgb(128, 43, 0);"})
        self.scrollArea.mouseMoveEvent = self.mouseMoveEventLeft
        self.scrollArea.mousePressEvent = self.mousePressEventLeft
        self.scrollArea.mouseReleaseEvent = self.mouseReleaseEventLeft
        
        self.label4.setCursor(Qt.OpenHandCursor)
        self.label4.setCursor(Qt.OpenHandCursor)
    
    
    
    def mousePressEventLeft(self, event):
        self.pressed = True
        self.label4.setCursor(Qt.ClosedHandCursor)
        self.initialPosX = self.scrollArea.horizontalScrollBar().value() + event.pos().x()
        self.initialPosY = self.scrollArea.verticalScrollBar().value() + event.pos().y()

    def mouseReleaseEventLeft(self, event):
        self.pressed = False
        self.label4.setCursor(Qt.OpenHandCursor)
        self.initialPosX = self.scrollArea.horizontalScrollBar().value()
        self.initialPosY = self.scrollArea.verticalScrollBar().value()

    def mouseMoveEventLeft(self, event):
        if self.pressed:
            self.scrollArea.horizontalScrollBar().setValue(self.initialPosX - event.pos().x())
            self.scrollArea.verticalScrollBar().setValue(self.initialPosY - event.pos().y())
    
    
    
    
    
    
    def ObjectDetection(self):
        config_file='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        frozen_model='frozen_inference_graph.pb'
        model = cv2.dnn_DetectionModel(frozen_model,config_file)
        classLabels=[]
        file_name='Label.txt'
        with open(file_name,'r') as fpt:
            classLabels=fpt.read().rstrip('\n').split('\n')
        model.setInputSize(320,320)
        model.setInputScale(1.0/127.5)
        model.setInputMean((127.5,127.5,127.5))
        
        frame=cv2.imread(self.path[0])
        


        font_scale=2
        font=cv2.FONT_HERSHEY_SIMPLEX
        classindex,confidence,bbox=model.detect(frame,confThreshold=0.55)
        print(classindex)
        if len(classindex)!=0:
            for index,conf,boxes in zip(classindex.flatten(),confidence.flatten(),bbox):
                if index<=80:
                    cv2.rectangle(frame,boxes,(0,0,255),2)
                    cv2.putText(frame,classLabels[index-1],(boxes[0]+10,boxes[1]+40),font,fontScale=font_scale,thickness = 2,color=(255,0,0))
        frame=cv2.resize(frame,(self.label4.width(),self.label4.height()))
        

        self.image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_BGR888)
        self.label4.setPixmap(QPixmap.fromImage(self.image))
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.lineEdit.setText("")
        


        
        
        
        
    def Open1(self):

        self.path = QFileDialog.getOpenFileName(self.layoutWidget1, 'Open a file', '',
                                        'All Files (*.jpeg *.jpg *.png)')
        if self.path != ('', ''):
            print("File path : "+ self.path[0])
        
            self.lineEdit.setText(self.path[0])
            

            
            
            
    def zoomIn(self):
        
        self.scaleImage(1.25)
        
        
    def zoomOut(self):
        
        self.scaleImage(0.8)
        
        
    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.label4.resize(self.scaleFactor * self.label4.pixmap().size())
   

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)
        
    
        
    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))
        
        
        
def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

    
if __name__ =='__main__':
    main()
