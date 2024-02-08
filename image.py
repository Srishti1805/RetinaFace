import cv2
from retinaface import RetinaFace
import argparse


def main():
    # Set up argparse to take image_path as an argument
    parser = argparse.ArgumentParser(
        description='Detect faces using RetinaFace and draw rectangles around them.')
    parser.add_argument('--image_path', type=str,
                        help='Path to the input image')
    args = parser.parse_args()

    # Read the image using the provided image_path
    path = rf"{args.image_path}" 
    print(path)
    image = cv2.imread(path)

    # Detect faces using RetinaFace
    faces = RetinaFace.detect_faces(image)

    # Draw rectangles around detected faces
    for key in faces.keys():
        obj = faces[key]
        face_area = obj['facial_area']
        cv2.rectangle(image, (face_area[2], face_area[3]),
                      (face_area[0], face_area[1]), (255, 0, 0), 2)

    # Save the result image
    cv2.imwrite("result.jpg", image)

    # Show the result using cv2
    cv2.imshow("result", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
