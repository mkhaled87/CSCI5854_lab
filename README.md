# Lab Materials for class CSCI 5854 (Foundations of Autonomous Systems)

This repo provides the lab materials for class CSCI 5854 (Foundations of Autonomous Systems), University of Colorado Boulder, USA.
The lab software includes the following suite of tools:
- [SCOTS: a tool for abstraction-based controller synthesis](https://github.com/mkhaled87/scots-ready)
- [OmegaThreads: a tool for controller synthesis from omega-regular specifications](https://github.com/mkhaled87/pFaces-OmegaThreads)


# Installing the required software

To install the required software, we build and use s Docker image.
First, make sure you have docker installed (see Docker installation guide for: [MacOS](https://docs.docker.com/docker-for-mac/install/), [Ubuntu Linux](https://docs.docker.com/engine/install/ubuntu/) or [Windows](https://docs.docker.com/docker-for-windows/install/)). Also, make sure to [configure Docker to use sufficient resources](https://docs.docker.com/config/containers/resource_constraints/) (e.g., enough CPU cores). Otherwise, OmegaThreads will run slower than expected.

Here, we assume you will be using a Linux or MacOS machine. 
Commands will be very similar on Windows if you use Windows PowerShell.

The following steps builds the required Docker image:

## 1- Clone the repository

``` bash
$ git clone https://github.com/mkhaled87/CSCI5854_lab
$ cd CSCI5854_lab
```


## 2- Build the image

``` bash
$ docker build -t csci5854/latest .
```


## 3- Start the container and enter it

``` bash
docker run -it -v ~/docker_shared:/docker_shared csci5854/latest
```



# Building the simulation interfaces

## Building SCOTS's MATLAB interface

## Building OmegaThreads's Python interface



