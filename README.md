# Deep-Learning-Training

## Installation
Use pip to install all requirements.

```bash
pip3 install -r requirements.txt
```

Download the dataset from kaggle.
```bash
https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset?datasetId=550917
```

Extract the downloaded file into a new folder "dataset". Your folder structure should now look like this.
```bash

```

Then run this command to rearrange the dataset.
```bash
python3 main.py --create_dataset --dataset [Choose a name]
```

## Usage

```bash
usage: main.py [-h] [--create_dataset] [--dataset DATASET] [--load LOAD] [--save SAVE] [--train] [--evaluate] [--predict PREDICT] [--epochs EPOCHS]

Cats and Dogs Deep Learning Classifier

options:
  -h, --help         show this help message and exit
  --create_dataset   Create dataset
  --dataset DATASET  Dataset path
  --load LOAD        Load model weights
  --save SAVE        Save model weights
  --train            Train model
  --evaluate         Evaluate model
  --predict PREDICT  Image path to predict
  --epochs EPOCHS    Define number of epochs
```

## License
MIT
