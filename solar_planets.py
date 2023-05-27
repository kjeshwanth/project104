import cv2
im2=cv2.imread("solar-system.jpg")
rocket=im2[120:360,400:500]

texttoshow="sun"
cv2.putText(im2,texttoshow,(20,220),
            fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=2,
            color=(0,0,0))
cv2.waitKey(0)

texttoshow="mercury"
cv2.putText(im2,texttoshow,(100,200),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))

cv2.waitKey(0)

texttoshow="venus"
cv2.putText(im2,texttoshow,(200,170),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))
cv2.waitKey(0)

texttoshow="earth"
cv2.putText(im2,texttoshow,(300,170),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))
cv2.waitKey(0)

texttoshow="mars"
cv2.putText(im2,texttoshow,(380,170),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))
cv2.waitKey(0)

texttoshow="jupiter"
cv2.putText(im2,texttoshow,(500,100),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))
cv2.waitKey(0)

texttoshow="saturn"
cv2.putText(im2,texttoshow,(800,140),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))
cv2.waitKey(0)

texttoshow="uranus"
cv2.putText(im2,texttoshow,(980,150),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))
cv2.waitKey(0)

texttoshow="neptune"
cv2.putText(im2,texttoshow,(1100,140),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,
            color=(255,255,255))
cv2.imshow("poster",im2)
cv2.waitKey(0)