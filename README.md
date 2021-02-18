# MultiClass CNN proof of concept

## Guia para correr

1. Correr el jupyter notebook "multicnn_training.ipynb"
2. Descomprimir el archivo 'tar' descargado, esto creara la carpeta `output_model`.
3. Configurar el archivo 'config.ini':
    1. `samples_path` debe contener la direccion hacia el conjunto de datos (el llamado "dataset" en el jupyter notebook).
    2. `model_path` debe contener la direccion hacia la carpeta del modelo: `output_model`
    3. corroborar que los parametros de las imagenes son los mismos que los definidos en el jupyter notebook.
4. Instalar dependencias, en una terminal correr:
    1. `python3 -m install pip --upgrade --user`
    2. `python3 -m pip install -r requirements.txt --user`
5. Correr `predict.py`:
    1. ir a `src/`.
    2. correr `predict.py`:
        ```shell
        python3 predict.py -c <path_to_configfile> -I <path_to_img>
        ```
    3. Donde `<path_to_configfile>` es la direccion hacia el archivo 'config.ini', y <path_to_img> es la direccion a la imagen que deseamos clasificar.
