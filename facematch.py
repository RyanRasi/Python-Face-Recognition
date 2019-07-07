import face_recognition

image_of_rdj = face_recognition.load_image_file('./img/known/Robert Downey Jr.png')
rdj_face_encoding = face_recognition.face_encodings(image_of_rdj)[0]

unknown_image = face_recognition.load_image_file(
    './img/unknown/Robert-Downey-Jr-Spider-man-Premiere.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces(
    [rdj_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Robert Downey Jr')
else:
    print('This is not Robert Downey Jr')