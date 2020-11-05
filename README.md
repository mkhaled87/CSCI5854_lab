# Lab Materials for class CSCI 5854 (Foundations of Autonomous Systems)

This repo provides the lab materials for class CSCI 5854 (Foundations of Autonomous Systems), University of Colorado Boulder, USA.
The lab software includes the following suite of tools:
- [SCOTS: a tool for abstraction-based controller synthesis](https://github.com/mkhaled87/scots-ready)
- [OmegaThreads: a tool for controller synthesis from omega-regular specifications](https://github.com/mkhaled87/pFaces-OmegaThreads)


## Installing the required software

To install the required software, we build and use s Docker image.
First, make sure you have docker installed (see Docker installation guide for: [MacOS](https://docs.docker.com/docker-for-mac/install/), [Ubuntu Linux](https://docs.docker.com/engine/install/ubuntu/) or [Windows](https://docs.docker.com/docker-for-windows/install/)). Also, make sure to [configure Docker to use sufficient resources](https://docs.docker.com/config/containers/resource_constraints/) (e.g., enough CPU cores). Otherwise, OmegaThreads will run slower than expected.

Here, we assume you will be using a Linux or MacOS machine. 
Commands will be very similar on Windows if you use Windows PowerShell.

The following steps builds the required Docker image:

### 1- Clone the repository

``` bash
$ git clone https://github.com/mkhaled87/CSCI5854_lab
$ cd CSCI5854_lab
```


### 2- Build the image

``` bash
$ docker build -t csci5854/latest .
```


### 3- Start the container and enter it

``` bash
docker run -it -v ~/docker_shared:/docker_shared csci5854/latest
```



## Building the simulation interfaces

### Building SCOTS's MATLAB interface

You need to have MATLAB installed in your host machine (not inside the Docker container) to be able to simulate the controllers resulting from SCOTS.
Follow the steps that correspond to your operating system. 
Only few operating systems and their distributions are supported.
Contact me directly to give you iinstructions how to build the CUDD library on your OS which is used for the simulation interface.

#### Windows 

- Open MATLAB
- Navigate from inside Matlab to the folder [./scots-matlab/mexfiles/](scots-matlab/mexfiles).
- Run the Matlab script file: [makewin.m](scots-matlab/mexfiles/makewin.m).
- Once the building finishes with success, add the following folders to Matlab's path:
  - [./scots-matlab/](scots-matlab/)
  - [./scots-matlab/mexfiles/](scots-matlab/mexfiles/)

#### MacOS and Linux

### Building OmegaThreads's Python interface



