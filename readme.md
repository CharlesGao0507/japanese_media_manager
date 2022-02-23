# Japanese Media Manager

![license](https://img.shields.io/badge/license-MIT-green)
![pytest](https://github.com/zqmillet/japanese_media_manager/actions/workflows/pytest.yml/badge.svg)
![pylint](https://github.com/zqmillet/japanese_media_manager/actions/workflows/pylint.yml/badge.svg)
![flake8](https://github.com/zqmillet/japanese_media_manager/actions/workflows/flake8.yml/badge.svg)
![mypy](https://github.com/zqmillet/japanese_media_manager/actions/workflows/mypy.yml/badge.svg)
[![codecov](https://codecov.io/gh/zqmillet/japanese_media_manager/branch/main/graph/badge.svg?token=XV3ZZ6JX15)](https://codecov.io/gh/zqmillet/japanese_media_manager)
[![Documentation Status](https://readthedocs.org/projects/japanese-media-manager/badge/?version=latest)](https://japanese-media-manager.readthedocs.io/zh_CN/latest/?badge=latest)

Japanese Media Manager (jMM) is a CLI tool for management of Japanese xxx media. The name of Japanese Media Manager pays tribute to tMM, which is short for tinyMediaManager.

## Getting Started

### Prerequisites

- System OS: Windows, Linux, MacOS[^1].
- Python: 3.7+.

### Installing

## Running the tests

If you want to run the tests, you need to install requirements first.

``` bash
pip install -r testcases/requirements.txt
```

Then run all tests by following command.

``` bash
pytest --app-id <app_id> --app-key <app_key> --reruns 5 --cov=japanese_media_manager --cov-report term-missing
```

where:

- `<app_id>` is the APP ID of Baidu translation service[^2].
- `<app_key>` is the APP Key of Baidu translation service.

If you does not specify the arguments `<app_id>` and `<app_key>`, the testcases about class `Translator` will be ignored.

### Break down into end to end tests

### And coding style tests

## Deployment

## Built With

## Contributing

## Versioning


## Authors

* **Qiqi**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

## ToDo

[^1]: Theoretically, jMM can run on any OS, in which Python3 can be deployed. But, I just test jMM on these three OSs.
[^2]: You need to regist Baidu account and request the service of translation, then you will get APP ID and APP Key.
