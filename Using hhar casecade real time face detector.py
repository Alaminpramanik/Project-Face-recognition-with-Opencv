import cv2

def draw_boundary(img,classfier,scalefactor,minNeighbor,color,text):
    gray_img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classfier.detectMultiScale(Gray_img,scalefactor,minNeighbor)
    coords = []

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)
        cv2.putText(img,text,(x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords =[x,y,w,h]

    return  coords

def detect(img, faceCasecade,eyesCasecade,noseCasecade,mouthCasecade):
    color = ("blue"(255,0,0), "red"(0,0,255), "green"(0,255,0), "pink"(255,255,255))
    coords=draw_boundary(img, faceCasecade, 1,1,10, color['blue'],"Face")

    if len(coords)==4:
       roi_img= img[coords[1]:coords[1]*coords[3],coords[0],coords[0],coords[2]]
       coords = draw_boundary(roi_img, eyesCasecade, 1, 1, 14, color['red'], "Eye")
       coords = draw_boundary(roi_img, noseCasecade, 1, 1, 4, color['green'], "Nose")
       coords = draw_boundary(roi_img, mouthCasecade, 1, 1, 20, color['pink'], "Mouth")

    return img


faceCasecade=cv2.Casecadeclassifier("haarcasecade_forntalface_default.xml")
eyesCasecade=cv2.Casecadeclassifier("haarcasecade_eye.xml")
noseCasecade=cv2.Casecadeclassifier("Nariz.xml")
mouthCasecade=cv2.Casecadeclassifier("Mouth.xml")


video_capture=cv2.VideoCapture(-1)

while true:
    _, img= video_capture.read()
    img= detect(img, faceCasecade, eyesCasecade,noseCasecade,mouthCasecade)
    cv2.imshow("face detection",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()