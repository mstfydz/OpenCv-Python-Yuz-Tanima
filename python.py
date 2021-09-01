import numpy  #Temel Numpy kutuphanesini eklemek icin gerekli komut.
import cv2    #OpenCv kutuphanesini ekleme icin gerekli komut.

fotograf = cv2.imread('resim.jpg') #Ayni klasorde bulunan fotografi yuklemek icin kullanilan ilgli komut.

fotografGri = cv2.cvtColor(fotograf, cv2.COLOR_BGR2GRAY) #Renk duzeni olarak Red,Green,Blue(RGB) olan fotografi manipule ederek gri tonlarina ceviren ilgili komut.
cv2.imwrite("peakupGri.jpg",fotografGri)  #Gri olarak manipule ettigimiz fotografi kaydetmek icin kullandigimiz komut.

ret,fotografBW = cv2.threshold(fotografGri,110,240,cv2.THRESH_BINARY) #binarization dedigimiz yontem ile fotograftaki pixel renklerini siyah ve beyaz olarak sinirlandirdik.
cv2.imshow('Binary Fotograf', fotografBW) #binarization yontemi ile manipule edilmis fotografi kaydetmek icin kullandigimiz komut.

cv2.imshow('Orijinal Fotograf', fotograf) #Fotografin orijinal halini ekranda gosteren komut.
cv2.imshow('Gri tonlarina cevrilmis fotograf', fotografGri) #Fotografin gri tonlarina donusturulmus halini ekranda gosteren komut.
cv2.imwrite("peakup01.jpg",fotografBW) #Fotografin binarization yontemi ile siyah ve beyaz halini ekranda gosteren komut

cv2.waitKey(0) #Klavyeden herhangi bir tus ile cikis yapmamizi saglayan komut.
cv2.destroyAllWindows()