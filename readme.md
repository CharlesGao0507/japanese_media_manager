# Japanese Media Manager

![license](https://img.shields.io/badge/license-MIT-green)
![pytest](https://github.com/zqmillet/japanese_media_manager/actions/workflows/pytest.yml/badge.svg)
![pylint](https://github.com/zqmillet/japanese_media_manager/actions/workflows/pylint.yml/badge.svg)
![flake8](https://github.com/zqmillet/japanese_media_manager/actions/workflows/flake8.yml/badge.svg)
![mypy](https://github.com/zqmillet/japanese_media_manager/actions/workflows/mypy.yml/badge.svg)
[![codecov](https://codecov.io/gh/zqmillet/japanese_media_manager/branch/main/graph/badge.svg?token=XV3ZZ6JX15)](https://codecov.io/gh/zqmillet/japanese_media_manager)
[![Documentation Status](https://readthedocs.org/projects/japanese-media-manager/badge/?version=latest)](https://japanese-media-manager.readthedocs.io/zh_CN/latest/?badge=latest)

Japanese Media Manager (jMM) is a CLI tool for management of Japanese xxx media. The name of Japanese Media Manager pays tribute to tMM, which is short for tinyMediaManager.

## Contents

<!-- vim-markdown-toc GFM -->

* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installing](#installing)
* [Running the tests](#running-the-tests)
    * [unit tests](#unit-tests)
    * [coding style tests](#coding-style-tests)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)
* [ToDo](#todo)

<!-- vim-markdown-toc -->

## Getting Started

### Prerequisites

- System OS: Windows, Linux, MacOS[^1].
- Python: 3.7+.

### Installing

``` bash
pip install jmm
```

## Running the tests

### unit tests

If you want to run the tests, you need to install requirements first.

``` bash
pip install -r testcases/requirements.txt
```

Then run all tests by following command.

``` bash
pytest --app-id <app_id> --app-key <app_key>
```

where:

- `<app_id>` is the APP ID of Baidu translation service[^2].
- `<app_key>` is the APP Key of Baidu translation service.

If you does not specify the arguments `<app_id>` or `<app_key>`, the testcases about class `Translator` will be ignored.

### coding style tests

- pylint: you can check the quality of all code with [pylint](https://pylint.org/).

  ``` bash
  # pip install pylint
  pylint japanese_media_manager testcases
  ```

- flake8: it is a wrapper around these tools:

  - PyFlakes,
  - pycodestyle,
  - Ned Batchelder's McCabe script.

  You can run [flake8](https://flake8.pycqa.org/en/latest/) check by following command.

  ``` bash
  # pip install flake8
  flake8 japanese_media_manager testcases
  ```

- mypy: all code in directory `japanese_media_manager` observe [PEP 484](https://www.python.org/dev/peps/pep-0484/), you can use [mypy](http://mypy-lang.org/) to static type check.

  ``` bash
  # pip install mypy
  python -m mypy japanese_media_manager
  ```

## Contributing

I love your contribution! You can make contributing to this project as easy and transparent as possible, whether it's:

- reporting a bug,
- discussing the current state of the code,
- submitting a fix,
- proposing new features, or
- becoming a maintainer.

## License

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to [AVDC](https://github.com/moyy996/AVDC) and [Movie_Data_Capture](https://github.com/yoshiko2/Movie_Data_Capture). They are both excellent tools, and give a great inspiration to me. 

## ToDo

- [x] crawlers
  - [x] javbus crawler
  - [x] javdb crawler
  - [x] airav crawler
  - [x] arzon crawler
  - [x] avsox crawler
- [x] translator
- [x] models
  - [x] video
  - [x] star
- [ ] cache
- [ ] scripts
  - [x] generate configuration
  - [ ] scrape video
- [ ] manual
  - [x] autodoc
  - [x] introduction
  - [ ] usage
  - [ ] framework

[^1]: Theoretically, jMM can run on any OS, in which Python3 can be deployed. But, I just test jMM on these three OSs.
[^2]: You need to regist Baidu account and request the service of translation, then you will get APP ID and APP Key.
