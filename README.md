# Favicon Gen - Team 66

> ## Table of contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Repo Setup](#repo-setup)
- [Setup the Project](#setup-the-project)
    - [Virtual Environment](#virtual-environment)
    - [Django Installation](#django-installation)
  - [Env Setup](#env-setup)
- [List of available endpoints](#list-of-available-endpoints)
- [Status](#contributors)
- [Contributors](#contributors)
- [Contributing to the project](#contributing-to-the-project)
#


## Overview

A platform that allows users to generate favicons, from icons and related HTML codes to embed. Users perform specific actions dependent on if they are unauthenticated or not.
<br>
<br>
>User: Unauthenticated
- Visit the platform to view basic information about it
- View and Interact with the documentation
- Register to view more details
- No access to use until registered

>User: Authenticated
- Full access to the platform
- Allow user upload icon
- Generate favicon (downloadable as zip)
- Generate html code for favicon
- Allow user save data and come back to download or use


#
> ## Technologies Used
| <b><u>Stack</u></b> | <b><u>Usage</u></b> |
| :------------------ | :------------------ |
| **`Django`**      | API      |
| **`HTML/CSS`**      | Frontend            |
| **`Javascript`**      | Frontend logic            |

#
> ## Repo Setup

<p align="justify">
To setup the repo, first fork the favicon-gen-team-66 repo, then clone the forked repository to create a copy on the local machine.
</p>

    $ git clone https://github.com/<github-user>/favicon-gen-team-66.git


<p align="justify">
Change directory to the cloned repo and set the original Favicon Gen Team 66 repository as the "upstream" and your forked repository as the "origin".
</p>

    $ git remote add upstream https://github.com/zuri-training/favicon-gen-team-66.git

#

> ## Setup the Project

<p align="justify">
The first step requires the download and installation of Python (if not installed) and a check to confirm that pip and the necessary dependencies are properly installed.
</p><br>

<p align="justify">
After the installation of Python, setup the project environment with pip and a virtual environment in the command prompt, powershell or gitbash terminal.
</p>
<br>

> ### Virtual Environment
<p align="justify">
A virtual environment creates an isolated Python environment containing all the packages necessary for the project.
</p>

`*Note:`

- This project was setup using the gitbash terminal. Some of the commands used might not work with command prompt or powershell.

* If a "pip command not found error" is encountered, download get-pip.py and run `phython get-pip.py` to install it.

###

    $ pip install virtualenv

Navigate to the cloned local project folder. Create a virtual environment folder and activate the environment by running the following commands in the gitbash terminal.

###

    $ python -m venv venv
    $ source venv/scripts/activate


> ### Django Installation
<p align="justify">
Once the virtual environment is active, the next step is the Django installation. Django is an open source Python web application framework thats helps with the rapid development of secure websites.
</p>

###

    $ (venv) pip install django

<p align="justify">
After installing Django, install Django REST framework in the gitbash terminal. The Django REST framework is a flexible toolkit for building Web based APIs. The REST framework was used for the creation of APIs, serialization and the authentication process for this project.
</p>

###

    $ (venv) pip install djangorestframework

Install all the necessary dependencies for the project. A few of them are listed below.

| <b><u>Modules</u></b>     | <b><u>Usage</u></b>           |
| :------------------------ | :---------------------------- |
| **`django-extensions`** | Custom extensions for Django |
| **`asgiref`**            | Async HTTP requests              |
| **`python-decouple`**      | Virtual environment configuration     |

An exhaustive list can be found in the requirements.txt file included in this project. The modules can be 'batch installed' using the `pip install -r requirements.txt` command.
```shell
$ cd favicon-gen-team-66

$ pip install -r requirements.txt
```


> ### Env Setup
Next create a `.env` file by using the sample.env. Retrieve your secret key from settings.py and place it within the `.env` file.
#


> ## List of available endpoints

| <b><u>View</u></b> | <b><u>URL</u></b> | 
| :---         | :---         |
| `Register User`| http://127.0.0.1:8000/register |
| `Login User`| http://127.0.0.1:8000/login |
| `Logout User` | http://127.0.0.1:8000/logout |
| `User profile` | http://127.0.0.1:8000/profile |
| `User List` | http://127.0.0.1:8000/users
 |
| `Favicon Generator` | http://127.0.0.1:8000/faviconer/add
 |

> ## Status
This project is a work in progress and is currently under development.

#

> ## Contributors

This Project was created by the members of Favicon Gen Team 66 during the Project Phase of the Zuri Internship.

#
> ## Contributing to the project

If you find something worth contributing, please fork the repo, make a pull request and add valid and well-reasoned explanations about your changes or comments.

Before adding a pull request, please note:

- This is an open source project.
- Your contributions should be inviting and clear.
- Any additions should be relevant.
- New features should be easy to contribute to.

All **`suggestions`** are welcome!
#
> ##### README Created by `pauline-banye`


#

TODO
- frontend setup
- testing
- linting & precommit
- swagger documentation
- deployed link
