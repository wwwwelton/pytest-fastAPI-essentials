# Pytest FastAPI Essentials
## Pytest
[Pytest](https://docs.pytest.org/en/7.2.x/) is a testing framework for the [Python programming language](https://www.python.org/doc/essays/blurb/). It provides a convenient way to write tests for your Python code, and supports a variety of test types, such as [unit tests](https://en.wikipedia.org/wiki/Unit_testing), [functional tests](https://en.wikipedia.org/wiki/Functional_testing), and [integration tests (E2E)](https://en.wikipedia.org/wiki/Integration_testing).

## FastAPI
[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (hence the name), web framework for building [APIs](https://www.ibm.com/topics/rest-apis) with [Python](https://www.python.org/doc/essays/blurb/) based on the asynchronous programming model. It is designed to be easy to use and to provide high performance for building [APIs](https://www.ibm.com/topics/rest-apis) quickly.

### Pytest FastAPI Essentials
This small project aims to study and test the endpoints created with [fastAPI](https://fastapi.tiangolo.com/) using [pytest](https://docs.pytest.org/en/7.2.x/). Nothing too deep, just an initial guide in the style of "[freeCodeCamp](https://www.freecodecamp.org/) essentials".

## Getting started
#### Requirements:
- [Python 3.10](https://www.python.org/downloads/)
- [pip 23.0](https://pip.pypa.io/en/stable/cli/pip_install/)
- [virtualenv 20.17](https://virtualenv.pypa.io/en/latest/installation.html)

**Follow the steps below**
```bash
# Clone the project and access the folder
git clone https://github.com/wwwwelton/pytest-fastAPI-essentials && \
cd pytest-fastAPI-essentials

# Create a virtual called for example "venv"
virtualenv venv

# Activate your virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the test suite from the root folder
# The project folder structure generated with "tree -L 1"
# .
# ├── app
# ├── LICENSE
# ├── README.md
# ├── requirements.txt
# └── venv
pytest app/test_main.py

# Run uvicorn to access fastAPI endpoints
# in the WebBrowser address http://localhost:8000/
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# You can access OpenAPI/Swagger at http://localhost:8000/docs

# To stop the server press "control + c" keys in the terminal
# and to exit the virtual environment type in the terminal:
deactivate

# Tips:
# install a package with pip:
pip install "package_name"
# list installed python packages:
pip freeze
# add your recently installed packages to the project:
pip freeze > requirements.txt

# Well done!
```

## Useful links
| Subject | Link |
| - | - |
| Pytest docs | https://docs.pytest.org/en/7.2.x/ |
| FastAPI docs | https://fastapi.tiangolo.com/ |
| Unit and Integration Testing (E2E) | https://www.geeksforgeeks.org/difference-between-unit-testing-and-integration-testing/ |
| FastAPI Testing Docs | https://fastapi.tiangolo.com/tutorial/testing/#__tabbed_1_2 |
| FastAPI Bigger Applications | https://fastapi.tiangolo.com/tutorial/bigger-applications/ |
| FastAPI JSON Encoder | https://fastapi.tiangolo.com/tutorial/encoder/ |
| Python venv | https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv |

## 📝 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

---

Made by: Welton Leite 👋 [See my linkedin](https://www.linkedin.com/in/welton-leite-b3492985/)
