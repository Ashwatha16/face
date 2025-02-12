from actions.google_drive_utils import download_images_from_drive
from actions.face_matching import match_faces
from actions.display_results import display_images
from actions.email_sender import send_email_with_images

# Paths & Configurations
reference_image_path = r"I:\Ashu-Files\project\QR FACE\Face-Matching-using-DeepFace-master\uploads\me.jpg"  # Change to your reference image
google_drive_folder_id = "1VlDby99dH2Sg-QH4yFkM_oIWAN_dFi1i"  # Replace with your Drive folder ID 
receiver_email = "bigiljd282@gmail.com"  # ✅ Update with recipient email

# Download only missing images from Drive
group_photos = download_images_from_drive(google_drive_folder_id)

# Perform Face Matching
matched_images, unmatched_images = match_faces(reference_image_path, group_photos)

# Display Results
display_images(matched_images, "Matched ✅")
display_images(unmatched_images, "Unmatched ❌")

# Send matched images via email
send_email_with_images(receiver_email, matched_images)

