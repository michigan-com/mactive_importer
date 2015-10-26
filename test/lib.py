import os

src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/feeds')
dest_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/dest_dir')

def get_test_images(include_path=False):
    """ Get an array of the test images located in data/feeds. Only gets
        png and jpg atm
    """

    photo_regex = "\.(jpg|png)$"
    images = []
    for file in os.listdir(src_dir):
        if photo_regex.find(file):
            images.append(os.path.join(src_dir, file) if include_path else file)

    return images
