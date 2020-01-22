# Python_Assignment2

![welcome](https://github.com/hahatori/Python_Assignment1/blob/master/images/welcome1.jpg)

This is an independent Assignment. You can find the contents, software，document and license down here. This README.md file describes the entire repository, like how it can be run, problems and solutions, the expected and actual results, etc. In addition, this directory contains the main program, environment and some required files. 

My student id is 201308685.

## Table of Contents

- [Introduction](#introduction)
- [Software](#software)
- [Run](#run)
- [Issues](#issues)
- [Results](#results)
- [License](#license)

## Introduction

There are 2 x(400 by 400) raster maps called **death.parishes.txt** and **death.rats.txt**. One is average rats caught per week per 100m x 100m square(r), another is average population density per 100m x 100m square(p). By weighting the two raster maps and multiplying them together, calculate the average deaths per week per 100m x 100m square(d) and save it as a **death.deaths.txt** file. In addition, consider whether users can automatically input or select weights to change the d.

This project including [death.parishes.txt](https://github.com/hahatori/Python_Assignment2/blob/master/death.parishes.txt), [death.rats.txt](https://github.com/hahatori/Python_Assignment2/blob/master/death.rats.txt), [death.deaths.txt](https://github.com/hahatori/Python_Assignment2/blob/master/death.deaths.txt) and [model.py](https://github.com/hahatori/Python_Assignment2/blob/master/model.py).

See the description of **README.md**. This document provides details about this respository, how to run the software, what to expect when it is run, outline any ‘known issues’ and outline any testing done.

## Software

This project uses [Python](https://www.python.org), [Anaconda](https://www.anaconda.com), [Spyder](https://www.spyder-ide.org) and [Jupyter](https://jupyter.org). Go check them out if you don't have them locally installed.

**Python** is a cross-platform computer programming language. Is an object-oriented dynamically typed language that was originally designed to write automated scripts (shells) and is increasingly being used for independent, large-scale project development as versions are updated and new features are added to the language.

**Anaconda** is an open source Python package manager that contains more than 180 science packages including conda, Python and their dependencies for computational science (data science, machine learning, big data processing and predictive analysis).

**Spyder** is a simple integrated development environment. Its main advantage over other Python development environments is that it mimics the "workspace" of MATLAB, making it easy to view and modify array values.

**Jupyter** is an interactive computing environment that supports more than 40 programming languages. Easy to create and share documentation of literary programs, support real-time code, mathematical equations, visualization, and documentation. Applications include data cleansing and transformation, numerical simulation, statistical modeling, machine learning, etc.

## Run

### Steps: how it can be run （UML图研究一下）



## Issues

See the description of **Document** (改成链接) in Jupyter. This document provides details about the respository, how to run the software, what to expect when it is run, outline any ‘known issues’ and outline any testing done.

### Display multiple plots on one screen

**matplotlib** is a Python 2D drawing library that generates graphics in a variety of hardcopy formats and cross-platform interactive environments. With Matplotlib, developers can generate graphs, histograms, power spectra, bar charts, error graphs, scatter plots, etc. in just a few lines of code.

Using the following code to load the matplotlib package, meaning the screen is divided into 2 x 2, and the p plot will be displayed in the upper left corner of the screen.

```sh
$ import matplotlib.pyplot as plt

  plt.subplot(2,2,1)
  plt.imshow(p)
```

In the same way, display r and d on the same screen:

```sh
$ plt.subplot(2,2,2)
  plt.imshow(r)
  plt.subplot(2,2,3)
  plt.imshow(d) 
```

Output:

![Multiple plots](https://github.com/hahatori/Python_Assignment2/blob/master/three_plot.png)


### List algorithms

When we calculate the weights of p and r, we need to use **weight x raster**. But if we just multiply the list by the weight, like ```l = [1, 2, 3] * 2```, we will get ```[1, 2, 3, 1, 2, 3]```. If we want to get ```[2, 4, 6]```, we can use ```[x*2 for x in l]```. Besides, list can not be directly multiplied by floats, we need import **numpy** package to get ```[0.8, 1.6, 2.4]```,  so the code should be ```numpy.multiply(np.array(l),0.8)```.

### Save the raster map as a text file

After the raster map (d) is generated, we should consider that the **List** cannot be saved as text files directly, and we should set the decimal places of the output. ```numpy.savetxt('death.deaths.txt',d,fmt='%.2f')``` helps us a lot.

### Change the parameter weights (Tkinter)还没写,可以把GUI里的复制过来

## Results下面俩需要改

### Theoretical Results(what is to be expected when it is run)

The expected result is the agents can interact with each other and have a GUI that shows the animation by input or modify parameters.  

Modify the IPython console from GUI.py to run to produce a separate window, called "My Model". The top left corner displays the window menu called "Model". Click on the menu displays a drop-down list named "Run model", continuing to click on it，displays an scatter plot animation.

### Actual Results


## License

[MIT](https://github.com/hahatori/Python_Assignment2/blob/master/LICENSE)© Tori
