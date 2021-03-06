# Cookiecutter-demo: Convert a TensorFlow notebook into a productive level project.

## Initialize the project organization.

Test the basic function of cookiecutter.

### Requirements to use the cookiecutter template:

---

- Python 3.7.4 64-bit (anaconda)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.7.0: This can be installed with pip by or conda depending on how you manage your Python packages:

```bash
$ pip install cookiecutter
```

or

```bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

To start a new project, run:

```bash
cookiecutter https://github.com/drivendata/cookiecutter-data-science
```

Use defalut setting, to fill in basic information of your project.

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org

## Downloand TensorFlow Notebook

Prepare the notebook for conversion. I choose the notebook from Google's tensorflow demo.

```bash
$ curl -o notebooks/demo.ipynb https://storage.googleapis.com/tensorflow_docs/docs/site/en/tutorials/quickstart/beginner.ipynb
```

or

```bash
$ curl -o notebooks/demo2.ipynb https://storage.googleapis.com/tensorflow_docs/docs/site/en/tutorials/keras/classification.ipynb
```

---

## Run Test (Pytest)

pytest will run all files of the form test\__.py or _\_test.py in the current directory and its subdirectories. More generally, it follows standard test discovery rules.

### Test one file

```bash
$ pytest src/tests/unit/test_sum.py
```

```bash
================================================== test session starts ===================================================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.12.0
rootdir: /Users/caihaocui/Documents/CodeWithMosh/Python/Modules/cookiecutter_demo
collected 4 items

src/tests/unit/test_sum.py ....                                                                                    [100%]

=================================================== 4 passed in 0.03s ====================================================
```

### Test all the test\*.py files

```bash
$ pytest
$ python -m pytest src/tests/unit/
```

```python
(base) ➜  cookiecutter_demo git:(master) ✗ pytest
===================================== test session starts =====================================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.12.0
rootdir: /Users/caihaocui/Documents/CodeWithMosh/Python/Modules/cookiecutter_demo
collected 6 items

src/tests/unit/test_fraction_sum.py ..                                                  [ 33%]
src/tests/unit/test_sum.py ....                                                         [100%]

====================================== 6 passed in 0.05s ======================================
```

## Run Unit Test

[python unittest](https://docs.python.org/3.7/library/unittest.html)

```bash
(base) ➜  cookiecutter_demo git:(master) ✗ cd src
(base) ➜  src git:(master) ✗ python -m unittest discover -s tests/unit/ -v
test_bad_type (test_fraction_sum.TestSum) ... ok
test_list_fraction (test_fraction_sum.TestSum) ... ok
test_bad_type (test_sum.TestSum) ... ok
test_list_int (test_sum.TestSum) ... ok
test_sum (test_sum.TestSum) ... ok
test_sum_tuple (test_sum.TestSum) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
