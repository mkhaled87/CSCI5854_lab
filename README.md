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

Building the Docker image may take up to 30 minutes and you may recieve some messages in red.
Ignore the red-messages unless they are errors that stop the building process.

### 3- Start the container and enter it

- For MacOS or Linux Docker hosts, run:
``` bash
docker run -it -v ~/docker_shared:/docker_shared csci5854/latest
```

- For Windows Docker hosts, run:
``` bash
docker run -it -v C:\docker_shared:/docker_shared csci5854/latest
```

Note that we run the docker container and share a volume (i.e., a folder) between it and the host.
In case of MacOS or Linux Docker hosts, the shared folder is located in the at: ~/docker_shared.
In case of Windows Docker hosts, the shared folder is located in the at: C:\docker_shared.


## Building the simulation interfaces

### Building SCOTS's MATLAB interface

You need to have MATLAB installed in your host machine (not inside the Docker container) to be able to simulate the controllers resulting from SCOTS.
Follow the steps that correspond to your operating system. 
Only few operating systems and their distributions are supported.
Contact me directly to give you iinstructions how to build the CUDD library on your OS which is used for the simulation interface.

#### Windows (10 x64)

- Open MATLAB.
- Navigate from inside Matlab to the folder [./scots-matlab/mexfiles/](scots-matlab/mexfiles).
- Run the Matlab script file: [makewin.m](scots-matlab/mexfiles/makewin.m).
- Once the building finishes with success, add the following folders to Matlab's path:
  - [./scots-matlab/](scots-matlab/).
  - [./scots-matlab/mexfiles/](scots-matlab/mexfiles/).

#### MacOS (Catalina) and Linux (Ubuntu 18.04)

- Open a Terminal window and navigate to the folder [./scots-matlab/mexfiles/](scots-matlab/mexfiles).
- For MacOS run:
``` bash
% mkdir cudd
% cp ./cuddMacCatalina/libcudd.a ./cudd
% make
```
- For Ubuntu run:
``` bash
$ mkdir cudd
$ cp ./cuddUbuntu18.04/libcudd.a ./cudd
$ make
```
- Once the building finishes with success, open Matlab add the following folders to Matlab's path:
  - [./scots-matlab/](scots-matlab/)
  - [./scots-matlab/mexfiles/](scots-matlab/mexfiles/)

### Building OmegaThreads's Python interface

The Python interface of OmegaThreads doesn not need to be built.
You will directly call Python modules from inisde the folder [./omegathreads-python/](omegathreads-python/).


## Testing the installation of SCOTS by example

We run an example to test the installtion of SCOTS and its simulation inrerface.
We assume you ran and enered the Docker ciontainer.
Navigate to the vehicle example in SCOTS's examples directory:
``` bash
/# cd /scots/examples/hscc16/vehicle1
```
For SCOTS each example needs to be built separately as SCOTS itself is a header-only library.
Build the example:
``` bash
/# make
```
Run the example's binary:
``` bash
/# ./vehicle
```
The last command will run SCOTS to synthesize a controller for an autonomous vehicle.
The complete details about the example (e.g., vehicle dynamics, the arena, and design requirements) are given in the example source file **vehicle.cc** in the example's folder.
Once SCOTS finiishes synthesizing the controller, copy the generated files (.BDD files) and the simulation script to the shared Docker folder:
``` bash
/# cp *.bdd /docker_shared/
/# cp vehicle.m /docker_shared/
```
Now, keep the terminal open and open MATLAB in your host machine.
Navigate to the shared Docker folder (**C:\docker_shared** in windows, or **~/docker_shared/** in MAcOS/Linux).
You should see the copied files from the Docker container.
Run the MATLAB script (vehicle.m) from inside the MATLAB command line to start the simulation:
``` bash
>> vehicle.m
```
In Windows, generating the simulation results can take up to 10 minues.
MATLAB should then show a figure of the vehicle's arena and the path the vehicle should take to avoid some obstacles before reaching a target.
The figure should look like:
![vehicle_sim_out](images/sim_vehicle.png?raw=true)



