import cv2
import numpy as np

def apply_oil_painting_filter(image, radius=7, intensity=6):
    # Convertir l'image en flottant
    img_float = np.float32(image)

    # Appliquer un filtre de flou gaussien pour réduire le bruit
    img_blur = cv2.GaussianBlur(img_float, (radius, radius), 0)

    # Calculer la différence entre l'image floue et l'image d'origine
    diff = cv2.absdiff(img_float, img_blur)

    # Ajouter l'intensité pour obtenir l'effet de peinture à l'huile
    img_oil_painting = img_float + intensity * diff

    # Limiter les valeurs des pixels entre 0 et 255
    img_oil_painting = np.clip(img_oil_painting, 0, 255)

    # Convertir l'image en uint8
    img_oil_painting = np.uint8(img_oil_painting)

    return img_oil_painting

def apply_pencil_sketch_filter(image):
    # Convertir l'image en niveaux de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou gaussien pour réduire le bruit
    img_blur = cv2.GaussianBlur(gray_image, (21, 21), 0, 0)

    # Inverser l'image floue
    inverted_blur = 255 - img_blur

    # Appliquer le filtre de couleur pour créer l'effet de dessin au crayon
    pencil_sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

    return pencil_sketch

# Charger l'image
image_path = 'bmw.jpg'  # Remplacez par le chemin de votre image
image = cv2.imread(image_path)

# Appliquer le filtre de peinture à l'huile
oil_painting_image = apply_oil_painting_filter(image)

# Appliquer le filtre de dessin au crayon
pencil_sketch_image = apply_pencil_sketch_filter(image)

# Afficher les images
cv2.imshow('Oil Painting Filter', oil_painting_image)
cv2.imshow('Pencil Sketch Filter', pencil_sketch_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
