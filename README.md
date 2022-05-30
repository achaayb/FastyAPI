<div id="top"></div>
<br />
<div align="center">
  <a href="#">
    <img src="https://imgs.search.brave.com/Xftt8kk2m5f-q7wfrFC45rKBq7j4wZlIAX6iji82T3o/rs:fit:1023:369:1/g:ce/aHR0cHM6Ly9mYXN0/YXBpLnRpYW5nb2xv/LmNvbS9pbWcvbG9n/by1tYXJnaW4vbG9n/by10ZWFsLnBuZw" alt="Logo">
  </a>

  <h3 align="center">FastyAPI</h3>

  <p align="center">
    A FastAPI based Stack boilerplate for heavy loads.
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    .
    <a href="#donations">Donations</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
	<li><a href="#built-with">Built with</a></li> 
	<li><a href="#features">Features</a></li>
	<li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#environment-setup">Environment setup</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-and-testing">Running and testing</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#donations">Donations</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

FastyAPI is a FastAPI-based Stack boilerplate designed for large-scale workloads and simple development in mind.

Here's why:

- FastAPI provides such a great development experience due to its simple structure and auto-generated docs.
- we've improved this further by providing you with a simple design pattern, no subfolders ❤️
- every Stack element is carefully chosen and tested/optimized against heavy workloads
- boilerplate code for different situations, WebSocket, crud, etc.. yet without the bloat.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

Our stack is as follows

- [Gunicorn](https://fastapi.tiangolo.com/deployment/server-workers/) is a Python Web Server Gateway Interface (WSGI) HTTP server. It is a pre-fork worker model
- [FastAPI](https://nextjs.org/) is a Web framework for developing RESTful APIs in Python.
- [Celery](https://docs.celeryq.dev/) **soon** + optional
- [Flower](https://flower.readthedocs.io/en/latest/) **soon** + optional
- [AIOredis](https://aioredis.readthedocs.io/) asyncio Redis client library.
- [Motor](https://motor.readthedocs.io/) presents a coroutine-based API for non-blocking access to MongoDB
- [MongoDB](https://svelte.dev/) is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.
- [Docker](https://www.docker.com/) **soon** **container** is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.

<p align="right">(<a href="#top">back to top</a>)</p>

### Features

- ✔️ Fully done
- ⌛ Needs Tweaks

- [x] [✔️] Auto generated Swagger Documentation
- [x] [✔️] http input validation
- [x] [✔️] MongoDB crud with smart returns
- [x] [✔️⌛] JWT authentication
- [x] [✔️⌛] WebSocket cross-server private and broadcast
- [ ] WebSocket http protocols implementation (GET/POST/PATCH/DELETE)
- [ ] [⌛] WebSocket json input validation
- [ ] Celery and Flower
- [ ] Unit testing
- [ ] Application and Server health graphs

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

Set of instructions to get started with FastyAPI

### Prerequisites

- [Python3](https://computingforgeeks.com/how-to-install-python-3-on-centos)
- pip3
- venv
  ```sh
   pip3 install virtualenv
  ```
- [CentOS preferably](https://www.centos.org/centos-linux)
- [MongoDB](https://phoenixnap.com/kb/install-mongodb-on-centos-8)
- [Redis](https://www.linode.com/docs/guides/install-and-configure-redis-on-centos-7)

### Environment setup

1. Create the project environment directory
   ```sh
   mkdir project_name
   ```
2. Create the environment
   ```sh
   cd project_name
   python3 -m virtualenv .
   ```
3. Activate the environment
   ```sh
   source bin/activate
   ```

### Installation

4. Clone the repo
   ```sh
   git clone https://github.com/achaayb/FastyAPI
   ```
5. Install the dependencies
   ```sh
   cd FastyAPI
   pip3 install -r requirements.txt
   ```
6. Configure [.env](https://github.com/achaayb/FastyAPI/blob/master/.env) to your need
   - better configuration soon
   - please run mongo and Redis on your local machine **for now**

### Running and testing

7. run FastyAPI on gunicorn with uvicorn workers
   ```sh
   gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
   ```
8. api test
   - navigate to : http://localhost:5000
   - the response should be something like this :
     ```json
     { "data": "", "code": "success", "message": "FastyAPI live!" }
     ```
9. swaggers docs
   - navigate to : http://localhost:5000/docs
10. websocket test
    - **username** : http://localhost:5000/static/test1.html
    - **username2** : http://localhost:5000/static/test2.html

### Minify the boilerplate to your needs

11. **soon**

<p align="right">(<a href="#top">back to top</a>)</p>

See the [open issues](https://github.com/achaayb/FastyAPI/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions are what makes the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## Donations

If this project was useful or you believe it's interesting, feel free to donate ❤️

Paypal Link : [Paypal.me](https://paypal.me/pseudorox)

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

Project Link: [https://github.com/achaayb/FastyAPI](https://github.com/achaayb/FastyAPI)

<p align="right">(<a href="#top">back to top</a>)</p>
