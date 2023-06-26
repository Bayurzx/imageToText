[![license](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)  
[![Tweet](https://img.shields.io/twitter/url/https/github.com/Bayurzx/imageToText.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20this%20out:%20https://github.com/Bayurzx/imageToText)  
[![Twitter](https://img.shields.io/twitter/follow/AdebayoOmolumo)](https://twitter.com/AdebayoOmolumo)


Image to Text Python Script
===========================

This Python script allows you to extract text from images using the EasyOCR library. It processes a directory of images and converts them into text, saving the results in an output file.

Prerequisites
-------------

Before running the script, ensure you have the following dependencies installed:

-   Python 3.x

To install the required dependencies, follow these steps:

1.  Clone this repository to your local machine.
2.  Navigate to the project directory using the command line.
3.  Create a virtual environment by running the following command:

``` bash

`python -m venv .env`
```
1.  Activate the virtual environment:

-   On Windows, run the following command:

``` powershell

`.\.env\Scripts\Activate.ps1`
```
-   On macOS/Linux, run the following command:

``` bash

`source .env/bin/activate`
```
1.  Install the dependencies from the `requirements.txt` file:

``` bash

`pip install -r requirements.txt`
```
Usage
-----

1.  Place your images in the same directory or specify the image directory in the script.
2.  Run the script using the following command:

``` bash

`python run.py`
```
1.  The script will process each image in the specified directory and extract the text. The results will be saved in the `output.txt` file.

Customization
-------------

-   You can modify the supported languages by editing the list passed to the `easyocr.Reader` constructor in the script.
-   Adjust the image directory or file extensions to process by modifying the script accordingly.

Feel free to explore and modify the script as per your requirements!

License
-------

This project is licensed under the [MIT License](./LICENSE).

Acknowledgements
----------------

This script utilizes the EasyOCR library, which can be found at: <https://github.com/JaidedAI/EasyOCR>

Please make sure to acknowledge and credit the EasyOCR library when using this script