import os
import sys
from tkinter import filedialog
from tkinter import *
import numpy as np
from PIL import Image
import glob

window=Tk()
window.title("메이플 믹스염색표 생성기")
window.geometry("320x460+100+100")
window.resizable(False, False)

label=Label(window, text="믹스염색표 생성기", width=40, height=4, fg="black")
label.pack()

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())

def helpWindow():
    global new
    new = Toplevel()
    new.title("사용방법")
    new.geometry("320x200+150+150")
    label=Label(new, text="사용방법\n\n1. 위컴알(WzCompareR2)에서 원하는 헤어를 골라 저장한다.\n→ 검은색부터 갈색까지 총 8개의 이미지를 한 폴더에 저장하는데, 이때 이미지는 반드시 위에서부터 1, 2, 3, 4, 5, 6, 7, 8의 숫자를 매겨 png 파일로 저장한다.\n2. 본 생성기에 이미지 소스 파일이 있는 폴더를 지정한 뒤, 결과물을 저장할 폴더를 지정한다.\n3. 실행 버튼을 눌러 결과물을 확인한다.\n예외처리를 하나도 안했기 때문에 버그가 나지 않도록 사용방법 숙지할 것!", width=43, fg="black", wraplength = 300, justify="left", anchor="nw")
    new.resizable(False, False)
    label.pack()

def makeWindow():
    global new
    new = Toplevel()

global srcFolder
global saveFolder


def srcAdress():
	window.srcFolder = filedialog.askdirectory()
	#window.file = filedialog.askopenfile(initialdir='path', title='select file', filetypes=(('jpeg files', '*.jgp'), ('all files', '*.*')))
	srcLabel.configure(text="소스를 저장한 폴더 : " + window.srcFolder)

def saveAdress():
	window.saveFolder = filedialog.askdirectory()
	saveLabel.configure(text="결과물을 저장할 폴더 : " + window.saveFolder)


def resource_path(relative_path):
    try:
        # PyInstaller에 의해 임시폴더에서 실행될 경우 임시폴더로 접근하는 함수
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
    
def deleteAllFiles(filepath) :
    if os.path.exists(filepath):
        for file in os.scandir(filepath):
            os.remove(file.path)
        return 'Remove All File'
    else :
        return 'Directory Not Found'


def execute():
    global result_file_path
    global source_file_path
    global temp_file_path

    createFolder(window.saveFolder + "/temp/")

    # 현재 위치 정의
    current_path = os.path.dirname(__file__)

    # 이미지 폴더 위치 정의
    image_path = os.path.join(current_path, "data")

    result_file_path = window.saveFolder + "/"
    source_file_path = window.srcFolder + "/"
    temp_file_path = window.saveFolder + "/temp/"
    background = Image.open(os.path.join(image_path, "clear.png"))
    backgroundChar = Image.open(os.path.join(image_path, "clear2.png"))
    blackPixelImg = Image.open(os.path.join(image_path, 'blackPixel.png'))
    sortBG = Image.open(os.path.join(image_path, "sortBG.png"))
    basicSortBG = Image.open(os.path.join(image_path, "basicSortBG.png"))

    # 1. mixHair.py
    검 = Image.open(source_file_path + "1.png")
    빨 = Image.open(source_file_path + "2.png")
    주 = Image.open(source_file_path + "3.png")
    노 = Image.open(source_file_path + "4.png")
    초 = Image.open(source_file_path + "5.png")
    파 = Image.open(source_file_path + "6.png")
    보 = Image.open(source_file_path + "7.png")
    갈 = Image.open(source_file_path + "8.png")

    mixArray = [검, 빨, 주, 노, 초, 파, 보, 갈]


    blackPixel = np.array(blackPixelImg)

    bgpix = np.array(backgroundChar)
    bgwidth, bgheight = backgroundChar.size
    #픽셀 비교 및 옮길 x, y좌표 설정


    pix = np.array(검)
    width, height = 검.size
    print(width, height)
    print(bgwidth, bgheight)

    realX = 0
    realY = 0
    # print(blackPixel[0][1]) 왼쪽칸이 height고 오른쪽이 width임
    for j in range (height) :
        for i in range (width) :
            try :
                if (np.array_equal(pix[j][i], blackPixel[0][0]) 
                and np.array_equal(pix[j][i+1], blackPixel[0][0]) 
                and np.array_equal(pix[j][i+2], blackPixel[0][0])
                and np.array_equal(pix[j][i+3], blackPixel[0][0])
                and np.array_equal(pix[j][i+4], blackPixel[0][0])
                and np.array_equal(pix[j][i+5], blackPixel[0][0])
                and np.array_equal(pix[j][i+6], blackPixel[0][0])
                and np.array_equal(pix[j][i+7], blackPixel[0][0])
                and np.array_equal(pix[j][i+8], blackPixel[0][0])
                and np.array_equal(pix[j][i+9], blackPixel[0][0])
                and np.array_equal(pix[j][i+11], blackPixel[0][0])
                and np.array_equal(pix[j][i+12], blackPixel[0][0])
                and np.array_equal(pix[j][i+13], blackPixel[0][0])
                and np.array_equal(pix[j][i+14], blackPixel[0][0])
                and np.array_equal(pix[j][i+15], blackPixel[0][0])
                and np.array_equal(pix[j][i+16], blackPixel[0][0])
                and np.array_equal(pix[j][i+17], blackPixel[0][0])) :
                    realX = i
                    realY = j
                    print((j, i), end=" ")
            except IndexError :
                print()
    print()
    for i in range (bgwidth) :
        if (np.array_equal(bgpix[bgheight-5][i], blackPixel[0][0])) :
            print(i, end=" ")
    print()

    bgX = 25
    bgY = 85


    # 이미지 이동 및 저장
    i = 0
    j = 0
    k = 1
    for j in range (8) :
        for i in range(8) : 
            mix = Image.blend(mixArray[j], mixArray[i], alpha=.5)
            background.paste(mix, box = (bgX-realX, bgY-realY))
            background.save(temp_file_path + f'{k}.png')
            i = i + 1
            k = k + 1
        j = j + 1

    #mix, box = (11, 17)

    # 2. sorting.py
    imgList = glob.glob(temp_file_path + '*.png')

    k = 1
    for i in range(1, 9):
        for j in range(1, 9):
            img2 = Image.open(temp_file_path + f'{k}.png')
            sortBG.paste(img2, (80 * (j-1), 90* (i-1)))
            k += 1

    sortBG.save(result_file_path + '1.png')


    # 3. basicSorting.py
    k = 0
    for i in range(1, 9):
        for j in range(1, 9):
            try :
                img2 = Image.open(temp_file_path + f'{9*k+1}.png')
                basicSortBG.paste(img2, (80 * (j-1), 90* (i-1)))
                k += 1
            except FileNotFoundError:
                None

    basicSortBG.save(result_file_path + '2.png')

    deleteAllFiles(window.saveFolder + "/temp/")
    os.rmdir(window.saveFolder + "/temp/")



button = Button(window, text="사용방법", overrelief="groove", width=40, height=3, command=helpWindow, repeatdelay=1000, repeatinterval=100)
button.pack()

# 소스 폴더
srcLabel=Label(window, text="소스를 저장한 폴더 : " , width=40, height=3, fg="black", wraplength=300, justify="left", anchor="nw")
srcLabel.pack()
srcButton = Button(window, text="소스 폴더 지정", overrelief="groove", width=40, height=3, command=srcAdress, repeatdelay=1000, repeatinterval=100)
srcButton.pack()

# 결과물 폴더
saveLabel=Label(window, text="결과물을 저장할 폴더 : ", width=40, height=3, fg="black", wraplength=300, justify="left", anchor="nw")
saveLabel.pack()
saveButton = Button(window, text="결과물 폴더 지정", overrelief="groove", width=40, height=3, command=saveAdress, repeatdelay=1000, repeatinterval=100)
saveButton.pack()



exeButton = Button(window, text="실행", overrelief="groove", width=40, height=3, command=execute, repeatdelay=1000, repeatinterval=100)
exeButton.pack()

label=Label(window, text="made by 정윤", width=40, height=4, fg="black")
label.pack()



window.mainloop()