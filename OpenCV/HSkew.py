import cv2
import numpy as np
import logging
import sys

#print(cv2.__version__)

def HomographicSkew(path, queryImg, rootImg, angle=None):
    try:
        #deskewed_img_name = 'deskewed_stub_{}'.format(rootImg)
        #crop_img_name = 'extracted_stub_{}'.format(rootImg)
        adjusted_img_name = 'adj_{}'.format(rootImg)
        # Read Images
        img = cv2.imread(path + queryImg, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(path + rootImg, cv2.COLOR_BGR2GRAY)
        # Features extraction
        sift_features = cv2.xfeatures2d.SIFT_create()
        kp_image, desc_image = sift_features.detectAndCompute(img, None)
        # Feature matching
        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        Match = cv2.FlannBasedMatcher(index_params, search_params)
        kp_grayframe, desc_grayframe = sift_features.detectAndCompute(img2, None)
        #Tweak k if needed
        matches = Match.knnMatch(desc_image, desc_grayframe, k=2)
        points = []
        for m, n in matches:
            if m.distance < 0.6 * n.distance:
                points.append(m)
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in points]).reshape(-1, 1, 2)
        # Finding match homographically
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
        # Perspective transform
        h, w = img.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)
        cord = np.int32(dst)
        # Cropping best rectangle to cover more area
        x1, x2 = cord[0][0][0], cord[1][0][0]
        x3, x4 = cord[2][0][0], cord[3][0][0]
        y1, y2 = cord[0][0][1], cord[1][0][1]
        y3, y4 = cord[2][0][1], cord[3][0][1]
        #If sticker left skewed
        if x2 > x1:
            X1, Y1 = x1, y4
            X2, Y2 = x3, y2
        #If sticker Right skewed
        elif x2 < x1:
            X1, Y1 = x2, y1
            X2, Y2 = x4, y3
        #If sticker no Skewed
        else:
            X1, Y1 = x1, y1
            X2, Y2 = x3, y3

        crop = img2[Y1:Y2,X1:X2]
        #cv2.imwrite(path+crop_img_name, crop)
        #Can set angle if needed.
        deskewed = Deskew(crop, angle)
        #cv2.imwrite(path+deskewed_img_name, deskewed)
        img3 = img2.copy()
        cv2.rectangle(img3, (X1, Y1), (X2, Y2), (255, 255, 255), -1)
        img3[:deskewed.shape[0], :deskewed.shape[1]] = deskewed
        cv2.imwrite(path+adjusted_img_name, img3)
        return "Success"
    except Exception as err:
        logger.log(err)
        return "Failed to convert your image, Check logs"

def Deskew(crop, angle=None):
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    stacked = np.column_stack(np.where(threshold > 0))
    if angle:
        angle = angle
    else:
        angle = cv2.minAreaRect(stacked)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
    (h, w) = crop.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(crop, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    print("[INFO] angle: {:.3f}".format(angle))
    return rotated


if __name__ == '__main__':
    NoOfArgs = len(sys.argv) - 1

    path = str(sys.argv[1])
    #logging.basicConfig(filename='path' + 'logger.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.basicConfig(filename=path + 'logger.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)
    #HomographicSkew('path', 'sticker2.jpg', '503_1_2.tiff')
    if NoOfArgs == 4:
        HomographicSkew(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    elif NoOfArgs == 3:
        HomographicSkew(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Invalid No of arguments")
