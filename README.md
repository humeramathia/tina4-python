### Tina4Python - This is not a frameowork for Python

Tina4Python is a light-weight routing and twig based templating system based on the [Tina4](https://github.com/tina4stack/tina4-php) stack which allows you to write websites and API applications very quickly.
.
### System Requirements

- Install Poetry:
  ```bash
  pip install poetry
  ```

- Install Jurigged (Enables Hot Reloading):
  ```bash
  pip install jurigged
  ```

### Installation

#### Windows

1. Install Poetry:
    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

2. Add the following path to the system PATH:
   ```
   %APPDATA%\pypoetry\venv\Scripts
   ```

3. Install Tina4Python and Jurigged:
   ```bash
   poetry add tina4_python
   poetry add jurigged
   ```

   **or**

   ```bash
   pip install tina4_python
   pip install jurigged
   ```

### Usage

After defining templates and routes, run the Tina4Python server:

- **Normal Server**:
  ```bash
  poetry run
  ```

- **Server with Hot Reloading**:
  ```bash
  poetry run jurigged main.py
  ```

- **Server on a Specific Port**:
  ```bash
  poetry run main.py 7777
  ```

### Templating


Tina4 uses [Twig](https://twig.symfony.com/) templating to provide a simple and efficient way to create web pages.

1. **Twig Files**: Add your Twig files within the `src/templates` folder. For instance, you might create files like `index.twig`, `base.twig`, etc., containing your HTML structure with Twig templating syntax for dynamic content.

2. **Using Twig**: In these Twig files, you can use Twig syntax to embed dynamic content, control structures, variables, and more. For example:

   ```twig
   <!-- index.twig -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Welcome</title>
   </head>
   <body>
       <h1>Hello, {{ name }}!</h1>
   </body>
   </html>
   ```

### Defining Routes


The routing in Tina4Python can be defined in the `__init__.py` file or any file used as an entry point to your application. Tina4Python provides decorators to define routes easily.

1. **Creating Routes**: Define routes using decorators from Tina4Python to handle HTTP requests.

    Example:
    ```python

   from tina4_python.Router import get
   from tina4_python.Router import response
   import asyncio

    @get("/hello")
    async def hello():
        return response("Hello, World!")
    ```

    This code creates a route for a GET request to `/hello`, responding with "Hello, World!".



### Features
| Completed                | To Do                            |
|--------------------------|----------------------------------|
| Python pip package       | Localization                     |
| Basic environment handling | Enhanced routing                 |
| Basic routing            | Template handling                |
|                          | OpenAPI (Swagger)                |
|                          | Implement JWT for token handling |


### Building and Deployment

#### Using Python

1. Building the package:
    ```bash
    python3 -m pip install --upgrade build
    python3 -m build
    python3 -m pip install --upgrade twine
    python3 -m twine upload dist/*
    ```

#### Using Poetry

1. Building the package:
    ```bash
    poetry build
    ```

2. Publishing the package:
    ```bash
    poetry publish
    ```
