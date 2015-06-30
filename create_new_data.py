from splat.models import Splat, Painting, PaintingStyle


with open('painting_styles_dataset.csv') as infile:
    data = infile.readlines()
    for painting_style in data:
        style_data = painting_style.split(',')
        PaintingStyle.objects.create(id=style_data[0], description=style_data[1])