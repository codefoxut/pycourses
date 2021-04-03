
class Bitmap:
    def  __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print("About to draw image.")
    image.draw()
    print("done drawing image")


if __name__ == '__main__':
    bmp = Bitmap('facepalm.jpg')
    draw_image(bmp)
    print("# step 2")
    bmp = Bitmap('facepalm1.jpg')
    print("# step 3")
    lbmp = LazyBitmap('facepalm.jpg')
    draw_image(lbmp)