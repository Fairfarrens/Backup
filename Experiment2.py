import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage

class ImageDenoisingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.processed_images = []

    def initUI(self):
        self.setWindowTitle('Image Denoising')
        self.layout = QVBoxLayout()

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.load_image_button = QPushButton('Load Image')
        self.load_image_button.clicked.connect(self.load_image_dialog)
        self.layout.addWidget(self.load_image_button)

        self.add_salt_pepper_button = QPushButton('Add Salt & Pepper Noise')
        self.add_salt_pepper_button.clicked.connect(self.add_salt_pepper_noise)
        self.layout.addWidget(self.add_salt_pepper_button)

        self.add_gaussian_button = QPushButton('Add Gaussian Noise')
        self.add_gaussian_button.clicked.connect(self.add_gaussian_noise)
        self.layout.addWidget(self.add_gaussian_button)

        self.mean_filter_button = QPushButton('Mean Filter')
        self.mean_filter_button.clicked.connect(self.apply_mean_filter)
        self.layout.addWidget(self.mean_filter_button)

        self.median_filter_button = QPushButton('Median Filter')
        self.median_filter_button.clicked.connect(self.apply_median_filter)
        self.layout.addWidget(self.median_filter_button)

        self.setLayout(self.layout)

    def load_image_dialog(self):
        filepath, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if filepath:
            self.load_image(filepath)

    def load_image(self, filepath):
        image = cv2.imread(filepath)
        self.current_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.display_image()

    def add_salt_pepper_noise(self):
        noise = np.zeros(self.current_image.shape[:2], np.uint8)
        cv2.randu(noise, 0, 255)
        salt = noise > 245
        pepper = noise < 10
        noisy_image = self.current_image.copy()
        noisy_image[salt] = [255, 255, 255]
        noisy_image[pepper] = [0, 0, 0]
        self.display_image_with_title(noisy_image, "Salt & Pepper Noise")

    def add_gaussian_noise(self):
        mean = 0
        sigma = 25
        gauss = np.random.normal(mean, sigma, self.current_image.shape)
        noisy_image = np.clip(self.current_image + gauss, 0, 255).astype(np.uint8)
        self.display_image_with_title(noisy_image, "Gaussian Noise")

    def apply_mean_filter(self):
        filtered_image = cv2.blur(self.current_image, (5, 5))
        self.display_image_with_title(filtered_image, "Mean Filter")

    def apply_median_filter(self):
        filtered_image = cv2.medianBlur(self.current_image, 5)
        self.display_image_with_title(filtered_image, "Median Filter")

    def display_image(self):
        height, width, channel = self.current_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(self.current_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)

    def display_image_with_title(self, image, title):
        pixmap = self.image_to_pixmap(image)
        new_label = QLabel(self)
        new_label.setPixmap(pixmap)
        self.layout.addWidget(new_label)
        self.processed_images.append((new_label, title))

    def image_to_pixmap(self, image):
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_image)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageDenoisingApp()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())
