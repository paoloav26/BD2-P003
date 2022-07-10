# BD2-P003 Facial Recognition 😎

## Integrantes 🙋‍♂️
- Matias Avendaño Vargas  [Matias222]
- Paolo Armas Vega [Paoloav26]

## Profesor 🦾
- Heider Sanchez Enriquez

## Objetivos Principales 🎯
- Este proyecto está enfocado al uso una estructura multidimensional para dar soporte a las búsqueda y 
recuperación eficiente de imágenes en un servicio web de reconocimiento facial.

## Comenzando 🚀
### Pre-requisitos 📋
- Python >= 3.8
### Despliegue 📦
- Ejecutar archivo __init__.py de la carpeta server
### Dataset
- El conjunto de fotografías del laboratorio 11 que consta de 13233 imágenes de 5749 personas distintas.
### Librerías empleados
-Pickle: Facilita el guardado de diccionarios en memoria secundaria, esto lo empleamos para extraer los vectores característicos del dataset sólo una vez.
\\
-Face Recognition: Permite la extracción de los vectores característicos de cada fotografía, estos son 128 dimensional.
\\
-Rtree: Genera el índice Rtree en memoria secundaria, contiene una función que devuelve los K elementos más cercanos a una query.  
\\
-Faiss: 




