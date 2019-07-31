import cv2
import pytesseract
import win32clipboard
import re
import sys

# tesseract commmad 불러오기
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 결과 텍스트 값 클립보드 저장
def setClipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()

def ocrClip(Image):
    im_gray = cv2.imread(Image, cv2.IMREAD_GRAYSCALE)
    (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
#     cv2.imwrite('bw_image.png', im_bw)
    text = pytesseract.image_to_string(im_bw, lang='eng', config="--psm 8 --oem 3")
    setClipboard(text)
    return text

def main(Image):
    captcha_data = ocrClip(Image)
    print("Before Analyzing : \t" + captcha_data)
    text = re.compile("\d\d\d\d\d\d")
    matchobj=text.search(captcha_data)
    if matchobj == None:
        return '111111'

    print("After analyzing : \t" + matchobj.group())

    return matchobj.group()
	
if __name__ == "__main__" :
    main(sys.argv[1])
