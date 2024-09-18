## BentoML Serving

### User guide
1. Clone the repo using the following command:
    
    ```bash
        git clone https://github.com/ahmedelsayed968/Bento-Serving.git
    ```
2. install dependecy
    ```bash
    pip install -r requirments.txt
    ```
#### to run the Simple Demp App
1. run the train script in `/src/SimpleBentoService` using the following command:

    ```bash
    python -m src.SimpleBentoService.train
    ```
2. then run the service using:

    ```bash
    bentoml serve src.SimpleBentoService.service:IrisClassifier
    ```
     