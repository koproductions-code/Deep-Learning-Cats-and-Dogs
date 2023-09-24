#!/usr/bin/env python3

from util.Dataset import Dataset
from util.Manager import Manager
import argparse
import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='Cats and Dogs Deep Learning Classifier')

parser.add_argument("--create_dataset", action="store_true", help="Create dataset")
parser.add_argument('--dataset', type=str, default=None, help='Dataset path')

parser.add_argument("--load", type=str, help="Load model weights")
parser.add_argument("--save", type=str, help="Save model weights")

parser.add_argument("--train", action="store_true", help="Train model")
parser.add_argument("--evaluate", action="store_true", help="Evaluate model")
parser.add_argument("--predict", type=str, help="Image path to predict")

parser.add_argument('--epochs', type=int, default=10, help='Define number of epochs')


if __name__ == "__main__":
    args = parser.parse_args()
    
    if args.dataset is None:
        raise ValueError("You must specify a dataset path")

    dataset = Dataset(args.dataset)

    if args.create_dataset:
        dataset.create_dataset()
    else:
        manager = Manager(dataset)
        if args.load is not None:
            manager.load(args.load)
        
        if args.train:
            manager.train(args.epochs)

        if args.evaluate:
            manager.evaluate()

        if args.save is not None:
            manager.save(args.save)

        if args.predict is not None:
            manager.predict(args.predict)