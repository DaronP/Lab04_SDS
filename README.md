# Lab04_SDS

Los archivos nbModel.py y dtModel.py contienen los metodos de preprocesamiento y entrenamiento de los modelos de clasificacion Naive Bayes y Desicion Tree, correspondientes. Asi mismo, se adjuntan los modelos en formato .pkl

### Modelo Naive Bayes

Accuracy Score: 0.8900986730180334


                  precision    recall  f1-score   support

           Virus       0.68      0.84      0.75       128
           Other       0.55      0.66      0.60       116
          Trojan       0.96      0.89      0.92      1860
        Backdoor       0.89      0.98      0.93       705
           Worms       0.64      0.72      0.68       130

        accuracy                           0.89      2939
       macro avg       0.74      0.82      0.78      2939
    weighted avg       0.90      0.89      0.89      2939


Este modelo se trabajo con tri-gramas. A pesar de tener un accuracy score de 0.89, hay clases que califica con mejor presicion que otras, asi como Trojans o Backdoors. Otras clases asi como Virus, Worms y otras categorias, no tuvieron una puntuacion tan alta debido a la cantidad de datos que se presentaban en el dataset.

### Modelo Desicion Tree

Accuracy Score: 0.7237155495066349


                  precision    recall  f1-score   support

           Virus       0.96      0.84      0.90       128
           Other       0.81      0.50      0.62       116
          Trojan       0.70      0.98      0.82      1860
        Backdoor       0.86      0.04      0.08       705
           Worms       0.88      0.79      0.83       130

        accuracy                           0.72      2939
       macro avg       0.84      0.63      0.65      2939
    weighted avg       0.76      0.72      0.64      2939


Este modelo tambien se trabajo con tri-gramas. Se obtuvo un accuracy score menor que el anterior, ya sea porque este es mas sencillo. Sin embargo, se obtuvieron mejores presiciones al predecir las clasificaciones.
