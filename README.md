# Baguette

A deep, transformer-based English-French translation application.

## Description

I have always loved French.  Although I grew up in an English-speaking family, I had the opportunity to take French classes throughout grade school and immediately took a liking to the language. I began to study French on my own after finishing my undergraduate degree and eventually became fluent enough to move to Quebec; I lived completely immersed in French for four years while pursuing my Master's degree and working full-time afterwards. 

Throughout my journey to fluency I often longed for an accurate French translator that was not prone to the numerous flaws of the statical machine translation models that were prevalent during the 1990's and 2000's. Thanks to tremendous advances in NLP, the advent of deep learning, and exponential increases in computing power, the translation applications of my dreams are now possible. The objective of this project is to create an English-to-French translation model from scratch using the transformer architecture described in [Attention Is All You Need](https://arxiv.org/abs/1706.03762).

The project contains several key components:

1. Creation of a data preprocessing pipeline to clean, partition, and tokenize text samples
2. Development of a transformer-based deep neural network architecture in PyTorch
3. Elaboration of a training script to optimize the model's parameters
4. Evaluation of the final model using statistical performance metrics

## Getting Started

### Installing

To install, simply clone the repository onto your machine and use your virtual environment creation tool to recreate the environment with the provided `requirements.txt` file. If you have Anaconda or Miniconda, you can instead use the `environment.yml` to reproduce the environment.

### Configuration

No configuration is required aside from recreating the virtual environment.

### Executing program

The application can be run locally through the command line. With the virtual environment activated, navigate to the `baguette/app/` directory and execute one of the following commands: 

- `python preprocess_data.py`
- `python train_model.py`

### Testing

This application uses the PyTest unit testing library to test the main classes and functions; tests are stored in the `test_app.py` file. To test the application, navigate to the `baguette/app/` directory through the command line and execute the following command: 
```
pytest test_app.py
```

### Updating the environment files

Any time the application's virtual environment is modified, the environment files must be updated to reflect the change.

To update the `requirements.txt` file, run the following command:
```
pip list --format=freeze > requirements.txt
```
To update the `environment.yml` file, run the following command:
```
conda env export > environment.yml
```

## Authors

David LaJambe

## License

This project is licensed under the Apache License version 2.0 - see the LICENSE.md file for details
