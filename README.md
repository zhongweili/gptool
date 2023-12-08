<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>GPTOOL</h1>
<h3>◦ Unveil the Power of Code, One Git at a Time!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/license/zhongweili/gptool?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/zhongweili/gptool?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/zhongweili/gptool?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/zhongweili/gptool?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

##  Table of Contents
- [ Table of Contents](#-table-of-contents)
- [ Overview](#-overview)
- [ Features](#-features)
- [ repository Structure](#-repository-structure)
- [ Modules](#modules)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running gptool](#-running-gptool)
    - [ Tests](#-tests)
- [ Roadmap](#-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---


##  Overview

The GPTool repository provides a Python-based tool for efficient management and interaction with the OpenAI API. It uses Pydantic for data validation, handles custom logging levels, and facilitates vector database indexing. Functions like chatting with OpenAI service, indexing the database, and retrieving relevant functions are included. A critical feature of GPTool is its ability to map and execute custom functions with parameter formatting and type validation. This offers developers an easy and robust way to extend and manage their interactions with the OpenAI API.

---

##  Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The architecture is segregated into modular components: services, types and utilities. Each caters to a specific functionality, creating good cohesion and low coupling.|
| 📄 | **Documentation**  | There is no explicit documentation provided in the repository. Instructions & clarifications were assumed based on the coded functions and class interfaces.|
| 🔗 | **Dependencies**   | Depends on external libraries including OpenAI, Pydantic and Qdrant-client for operation. Managed using Poetry for Python package and dependency management.|
| 🧩 | **Modularity**     | High modularity with clear separation of functionalities across modules like config, services, types and utils. The codebase follows DRY(Don't Repeat Yourself) principle.|
| 🧪 | **Testing**        | There's no presence of testing or test suites, so the effectiveness of existing codebase and its resiliency to future changes cannot be assessed.|
| ⚡️ | **Performance**    | The performance efficiency can't be assessed from the available codebase as no specific performance optimization or considerations are visible.|
| 🔐 | **Security**       | Security is implied via encrypted OpenAI key. No additional security measures or error handling mechanisms are visible in the codebase.|
| 🔀 | **Version Control**| The Git repository shows only one commit. Proper use of version control with clean, dedicated commits covering single functionality is not observed.|
| 🔌 | **Integrations**   | The system integrates with OpenAI for functionalities and Qdrant-client for managing a vector database, demonstrating good interaction with external services.|
| 📶 | **Scalability**    | Scalability isn't explicitly addressed, but the modular design and encapsulated functionalities can accommodate growth with additional modules and services.|

---


##  Repository Structure

```sh
└── gptool/
    ├── gptool/
    │   ├── config.py
    │   ├── gptool.py
    │   ├── services/
    │   │   ├── defaultvectordb_service.py
    │   │   └── openai_service.py
    │   ├── types/
    │   │   ├── abstract_vectordb.py
    │   │   ├── function.py
    │   │   └── log_level.py
    │   └── utils/
    │       ├── file_utilities.py
    │       ├── format_config_args.py
    │       ├── inspection_utilities.py
    │       ├── logger.py
    │       ├── model_utilities.py
    │       └── openai_utilities.py
    ├── poetry.lock
    └── pyproject.toml

```

---


##  Modules

<details closed><summary>Root</summary>

| File                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [pyproject.toml](https://github.com/zhongweili/gptool/blob/main/pyproject.toml) | The code represents the project structure of gptool, a Python-based tool used for managing OpenAI API functions efficiently through Pydantic validation and vector database indexing. The tool's main modules include configurations, services-specifically OpenAI & database services, multiple utility modules for file handling, configuration formatting, and logging purposes, and defines custom types for different tasks. The code also outlines dependencies for the project, such as openai, pydantic, and qdrant-client. |
| [poetry.lock](https://github.com/zhongweili/gptool/blob/main/poetry.lock)       | The code provided shows a directory tree structure for a tool called gptool. The tool consists of various Python scripts and modules that manage configurations, services (including a default vector database service and an OpenAI service), types of data, and essential utilities. The poetry.lock file is an auto-generated file by Poetry for package dependency management, featuring the specifications of a package named anyio. This package is used for handling asynchronous event loop implementations.                |

</details>

<details closed><summary>Gptool</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [config.py](https://github.com/zhongweili/gptool/blob/main/gptool/config.py) | The config.py is a part of a tool for configuring and managing interaction details with OpenAI. This tool makes use of Pydantic for data validation and error handling, and it defines a Config class for setting the OpenAI credentials, the directory for functions, the VectorDB class reference, and the log level. The configuration can be set up and handled via set_config function, whereas get_config and get_function_map functions retrieve the current configuration and function mapping respectively.                                          |
| [gptool.py](https://github.com/zhongweili/gptool/blob/main/gptool/gptool.py) | The provided code defines a Python class, `Gptool`, that acts as an interface for working with the OpenAI service. It initializes with several optional configuration arguments, including an OpenAI key and URL. The class methods allow for conversations with the service (`chat`), indexing a vector database (`index`), retrieving relevant functions (`get_top_n_functions`), and calling the OpenAI API with or without functions (`call_openai`, `call_openai_no_function`), finally providing a mechanism to run specific functions(`run_function`). |

</details>

<details closed><summary>Types</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [abstract_vectordb.py](https://github.com/zhongweili/gptool/blob/main/gptool/types/abstract_vectordb.py) | This Python code defines abstract methods for a vector database (VectorDB) in a tool named gptool. It includes methods for indexing VectorDB, searching VectorDB based on a specific query, and formatting the search results. The AbstractVectorDB can't be instantiated directly, but it provides a template for subclasses where the abstract methods should be implemented. It uses function mapping from a configuration file during initialization, for deeper functionality. |
| [log_level.py](https://github.com/zhongweili/gptool/blob/main/gptool/types/log_level.py)                 | The code represents an enumeration LogLevel offering pre-defined constant values for logging levels. These include debug, info, warning, error, and critical. This enumeration can be used in any logging scenario to control and categorize messages by their importance.                                                                                                                                                                                                          |
| [function.py](https://github.com/zhongweili/gptool/blob/main/gptool/types/function.py)                   | The `Function` class within the `function.py` file encapsulates function metadata such as name, description, and parameters. It leverages python callable and utility functions to validate input types, format parameters, and handle callable invocation. The class includes methods to format the parameters, dynamically call the stored function, and present function information in a clear, standardized format.                                                            |

</details>

<details closed><summary>Utils</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [model_utilities.py](https://github.com/zhongweili/gptool/blob/main/gptool/utils/model_utilities.py)           | The model_utilities.py code provides functions for scanning Pydantic models in a given module. It finds models based on a keyword, checks if an attribute is of Enum type or Optional, verifies if an attribute is in array form, gets array item types, and evaluates if a model is an Enum based array. It also retrieves possible values for Enum-based attributes, extracts default values, and identifies the types of items in Enum-based arrays.                                                                         |
| [logger.py](https://github.com/zhongweili/gptool/blob/main/gptool/utils/logger.py)                             | The provided code, located in `gptool/utils/logger.py`, defines a function `get_logger()`. This function helps set up a standard logger for the application, allowing logging with varying levels as imported from `gptool.types.log_level`. The logger uses a console handler to output logs, with timestamps and log levels indicated. It defaults to updating the logging level of an existing handler, if present.                                                                                                          |
| [inspection_utilities.py](https://github.com/zhongweili/gptool/blob/main/gptool/utils/inspection_utilities.py) | The provided Python code contains a function `get_input_parameter_type` that uses Python's inspect module to extract the type of the input parameter from a given function. Specifically, it searches function's parameters for an annotation containing Input. If such an annotation is found, its respective type is returned. If not, an exception is raised. The function expects a callable as input and returns a type of pydantic's BaseModel.                                                                           |
| [format_config_args.py](https://github.com/zhongweili/gptool/blob/main/gptool/utils/format_config_args.py)     | The provided Python script includes three key functions: get_user_package_path, inject_env_vars, and format_config_args. get_user_package_path retrieves the path of the caller's module. inject_env_vars checks for and reads a local json file containing environment variables-specifically the OPENAI_KEY. format_config_args incorporates these two functions to prepare the configuration arguments, ensuring the functions_directory is correctly formatted or defaults to functions.                                    |
| [file_utilities.py](https://github.com/zhongweili/gptool/blob/main/gptool/utils/file_utilities.py)             | The provided code forms part of a Python-based utility, gptool, used to dynamically load and manage Python modules and associated functions from a specified directory. It contains functions to load a module from a file, retrieve function directories, and create a map of available functions. The map is built by walking through the functions_directory, loading each function.py module found, verifying the function attribute's presence, and then storing them in a dictionary with the function’s name as the key. |
| [openai_utilities.py](https://github.com/zhongweili/gptool/blob/main/gptool/utils/openai_utilities.py)         | The provided script is part of a broader package named gptool. The specific script, openai_utilities.py, contains a function named get_latest_user_message. This function processes a list of message dictionaries and returns the most recent message made by the user. If no user message is found within the list, the function returns None.                                                                                                                                                                                |

</details>

<details closed><summary>Services</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [defaultvectordb_service.py](https://github.com/zhongweili/gptool/blob/main/gptool/services/defaultvectordb_service.py) | The code describes a DefaultVectorDBService class that uses OpenAI and Qdrant services. It initializes a database client and builds an index of function embeddings through the OpenAI service. Furthermore, it allows searching the index for the most similar function embeddings based on a given query. The search results are limited to the top_n most similar function names.                                                                                         |
| [openai_service.py](https://github.com/zhongweili/gptool/blob/main/gptool/services/openai_service.py)                   | The provided code is for a Python service under the tool gptool. This OpenAIService uses the OpenAI API. It initializes with API credentials from config and offers functionalities like creating embeddings and chat completions. The create_embeddings method outputs a list of float values, chat method gives a conversational response, and get_embeddings_size returns the size of an embedding. These functionalities facilitate interfacing with the OpenAI's model. |

</details>

---

##  Getting Started

###  Installation

Install:
```sh
# pip
pip install gptool

# peotry
poetry add sageai
```

###  Running gptool

Create a functions directory in the root directory, and add your functions.

Initialize the instance
```python
from gptool.gptool import Gptool

tool = Gptool(openai_key="", openai_url="")
```

Index the vector DB
```python
tool.index()
```

Chat
```python
message = "What's the weather like in Toronto right now?"
response = tool.chat(
    messages=[{"role": "user", "content": message}],
    model="gpt-3.5-turbo-1106",
    top_n=5,
)
```


---


##  Project Roadmap

> - [X] `ℹ️  Task 1: Implement basic features`
> - [ ] `ℹ️  Task 2: Add tests`
> - [ ] `ℹ️  Task 3: Support streaming response`


---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/zhongweili/gptool/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/zhongweili/gptool/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/zhongweili/gptool/issues)**: Submit bugs found or log feature requests for ZHONGWEILI.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License


This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](https://github.com/zhongweili/gptool/blob/main/LICENSE) file.

[**Return**](#Top)

---

