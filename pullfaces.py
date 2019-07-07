from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/groups/ParksAndRec.jpg')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top - 10:bottom + 10, left - 10:right + 10]
    pil_image = Image.fromarray(face_image)

# Saves images
    pil_image.show()
    pil_image.save(f'{top}.jpg')