import face_recognition
from PIL import Image, ImageDraw

image_of_emily = face_recognition.load_image_file('./img/known/Emily Blunt.jpg')
emily_face_encoding = face_recognition.face_encodings(image_of_emily)[0]

image_of_graham = face_recognition.load_image_file('./img/known/Graham Norton.jpg')
graham_face_encoding = face_recognition.face_encodings(image_of_graham)[0]

image_of_john = face_recognition.load_image_file('./img/known/John Krasinski.jpg')
john_face_encoding = face_recognition.face_encodings(image_of_john)[0]

image_of_kylie = face_recognition.load_image_file('./img/known/Kylie Minogue.jpg')
kylie_face_encoding = face_recognition.face_encodings(image_of_kylie)[0]

image_of_tom = face_recognition.load_image_file('./img/known/Tom Holland.jpg')
tom_face_encoding = face_recognition.face_encodings(image_of_tom)[0]

#  Create arrays of encodings and names
known_face_encodings = [
  emily_face_encoding,
  graham_face_encoding,
  john_face_encoding,
  kylie_face_encoding,
  tom_face_encoding
]

known_face_names = [
  "Emily Blunt",
  "Graham Norton",
  "John Krasinski",
  "Kylie Minogue",
  "Tom Holland"
]

# Load test image to find faces in
test_image = face_recognition.load_image_file('./img/groups/John-Emily.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left - 5, top - 15), (right + 5, bottom + 5)), outline=(0,0,0), width=3)

  # Draw label
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left - 5,bottom - text_height + 30), (right + 5, bottom + 5)), fill=(0,0,0), outline=(255,255,255))
  draw.text((left, bottom - text_height + 17.5), name, fill=(255,255,255))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('identify output image.jpg')