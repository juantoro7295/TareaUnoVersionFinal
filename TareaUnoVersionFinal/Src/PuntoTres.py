import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os
import cv2

# Ruta al directorio que contiene las imágenes
images_dir = "C:/Users/juanp/Downloads/TareaUnoVersionFinal/Src/lfw"

# Función para cargar las imágenes del directorio especificado
def load_images(directory):
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # Cargar la imagen en escala de grises
            if img is not None:
                images.append(img)
    return images

# Cargar las imágenes del directorio especificado
images = load_images(images_dir)

# Convertir la lista de imágenes a un arreglo numpy
images = np.array(images)

# Aplanar las imágenes a un arreglo unidimensional
images_flat = images.reshape(images.shape[0], -1)

# Calcular la mean face
mean_face = np.mean(images_flat, axis=0)

# Visualizar la mean face
plt.figure(figsize=(5, 5))
plt.imshow(mean_face.reshape(images[0].shape), cmap='gray')
plt.title('Mean Face')
plt.axis('off')
plt.show()

# Centrar los datos
centered_images = images_flat - mean_face

# Utilizar PCA para reducir la dimensionalidad
pca = PCA()
pca.fit(centered_images)

# Función para reconstruir imágenes utilizando PCA
def reconstruct_images(n_components):
    pca = PCA(n_components=n_components)
    pca.fit(centered_images)
    components = pca.transform(centered_images)
    reconstructed_images = pca.inverse_transform(components)
    reconstructed_images += mean_face
    return reconstructed_images

# Número de componentes para cada caso
n_components_list = [1, 3, 20]

# Visualizar las primeras 5 caras utilizando diferentes números de componentes PCA
plt.figure(figsize=(15, 10))
for i, n_components in enumerate(n_components_list, 1):
    reconstructed_images = reconstruct_images(n_components)
    for j in range(5):
        ax = plt.subplot(5, len(n_components_list)+1, i+j*len(n_components_list))
        if j == 0:
            plt.imshow(images[j].reshape(images[0].shape), cmap='gray')
            plt.title('Cara original')
        else:
            plt.imshow(reconstructed_images[j].reshape(images[0].shape), cmap='gray')
            plt.title(f'+ {n_components} comp')
        plt.axis('off')

# Reconstruir las imágenes utilizando el 95% y el 99% de la varianza
variance_ratio_cumsum = np.cumsum(pca.explained_variance_ratio_)
n_components_95 = np.argmax(variance_ratio_cumsum >= 0.95) + 1
n_components_99 = np.argmax(variance_ratio_cumsum >= 0.99) + 1

reconstructed_images_95 = reconstruct_images(n_components_95)
reconstructed_images_99 = reconstruct_images(n_components_99)

# Visualizar las primeras 5 caras con el 95% y el 99% de la varianza explicada
for j in range(5):
    ax = plt.subplot(5, len(n_components_list)+1, (len(n_components_list)+1)*(j+1))
    if j == 0:
        plt.imshow(images[j].reshape(images[0].shape), cmap='gray')
        plt.title('Cara original')
    else:
        plt.imshow(reconstructed_images_95[j].reshape(images[0].shape), cmap='gray')
        plt.title('95% comp' if j == 1 else '99% comp')
    plt.axis('off')

plt.tight_layout()
plt.show()
