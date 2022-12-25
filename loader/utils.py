def save_picture(picture):
    correct_types = ['png', 'jpg']

    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in correct_types:
        return

    picture.save(f"./uploads/{filename}")
    return f"uploads/{filename}"

