import cv2

image = cv2.imread("pirinc.jpg")
cv2.imshow("pirinc", image)
cv2.waitKey()

imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gri",imgGray)
cv2.waitKey()

_, imgBinary = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("siyahbeyaz",imgBinary)
cv2.waitKey()

blur = cv2.GaussianBlur(imgGray, (11, 11), 0)
canny = cv2.Canny(blur, 30, 150, 3)
dilated = cv2.dilate(canny, (1, 1), iterations=0)

(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgBinary, cnt, -1, (0, 255, 0), 2)

print("resimdeki pirinç sayısı : ",len(cnt))