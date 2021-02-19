# Web Maturity Status

## Description
Web version of the banana maturity status classifier that you can see [here.](https://github.com/kellycastrof/IA-MaturityStatusClassification)


## Installation
```
git clone https://github.com/kellycastrof/web-maturitystatus.git
cd web-maturitystatus/MaturityStatus

```
You can create a virtual environment to install all the necessary modules.


## Requirements

- keras
- tensorflow
- django
- rest framework
- numpy
- pillow 


Run the following command
```
pip install -r requirements.txt 
```
### With a virtual environment
```
pip install virtualenv
cd env/Scripts
```
If you use Unix distribution  ``` source activate ```
In Windows ``` activate.bat ```

Return to MaturityStatus folder and install with ``` pip install -r requirements.txt  ```


## Model
Go to the release part of this repository and download the model and weights files (.h5). Make sure to download them to model folder.


## How to start
```
python manage.py runserver
```




