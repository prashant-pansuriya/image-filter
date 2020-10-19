import cv2


def get_filter_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if action == "NO_FILTER":
        filter = img

    elif action == "COLORIZED":
        filter = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    elif action == "GRAYSCALE":
        filter = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    elif action == "BLURRED":
        widht, height = img.shape[:2]
        if widht > 500:
            k = (50,50)
        elif widht > 200 and widht <= 500:
            k = (25, 25)
        else:
            k = (10, 10)
        blur = cv2.blur(img, k)
        filter = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

    elif action == "BINARY":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _ ,filter = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filter = cv2.bitwise_not(img)

    return filter

