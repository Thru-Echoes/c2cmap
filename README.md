# C2CMap: Chick-to-Chick Mapping

**This is an Ornithological project (bird research) but could be applied to other audio-video processing.** 

Mapping chick tactile interactions between siblings from video and audio nest box recordings.

### Getting started 

The entire *c2cmap* project is being developed within the **dash00/tensorflow-python3-jupyter Docker image.** 

This allows native containerization functionality to easily deploy, ship, and scale. Also, Tensorflow and other deep learning packages are installed within the docker image. Lasltly, the docker image can be run locally (or deployed on a server) and will spin up a localhost with **Jupyter notebook server** running on it. This will have a top directory of *notebooks* and a subdirectory *notebooks/c2cmap* that contains this repository. 

#### Getting this image 

Either pull from Docker hub or pull from Github:

1. Docker 

```
$ docker pull dash00/tensorflow-python3-jupyter
```

2. Github 

Get the files of the GitHub repository [tensorflow-python3-jupyter](https://github.com/dash00/tensorflow-python3-jupyter) by downloading the ZIP file or by cloning the repository:

```
$ git clone https://github.com/dash00/tensorflow-python3-jupyter.git
```

Open a terminal and set the current working directory to the newly created folder with the project files. 

```
$ cd tensorflow-python3-jupyter
$ docker build .
```

##### Run this image 

*Run without persistent changes to directories*

```
$ docker run -it -p 8888:8888 dash00/tensorflow-python3-jupyter
```

*Run with persistent changes to directories*

```
$ docker run -it -p 8888:8888 -v /$(pwd)/notebooks:/notebooks dash00/tensorflow-python3-jupyter
```
