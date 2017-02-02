import glob
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv


class Images:
    def __init__(self):
        self.face = 0

    def save_CSV(self):
        dataset = self.load_dataset()

        i=1
        header = []
        for x in dataset[0]:
            header.append("x" + str(i))
            i+=1
        ofile = open('dataset.csv', "w")
        writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        writer.writerow(header)

        for row in dataset:
            writer.writerow(row)

    def load_dataset(self):
        dictionary = []
        image_list = []
        face_info = []

        #prog = re.compile(r'(resized_images/nonface)[0-9]+(.jpg)')

        for image in glob.glob('resized_images/*.jpg'):
            im = Image.open(image).convert('L')
            image_list.append(list(im.getdata()))

        return image_list

    def gerate_BioID(self):
        dataset = []

        for image in glob.glob('BioID/*.pgm'):
            im = Image.open(image).convert('L')
            dataset.append(list(im.getdata()))

        reshape_dataset = np.asarray([np.reshape(ds, (286, 384)) for ds in dataset[:]])
        self.resize_images('face', reshape_dataset, 1500)

    def resize_images(self, name, dataset, range):
        for item in dataset[:range]:
            self.face+=1
            plt.imsave('img.jpg', item, cmap='gray')
            img = Image.open('img.jpg')
            img2 = img.resize((77, 57), Image.ANTIALIAS)
            img2.save('resized_images/' + name + str(self.face) + '.jpg')

img = Images()
img.save_CSV()
