# SFIA Project 1 - QA Consulting

E-Commerce application.

## Index
[Brief](#brief)
   * [Solution](#solution)
   * [Setup](#setup)

[Project Management](#pro)

[Risk Assessment](#ris)

[Architecture](#arch)
   * [Entity Relationship Diagrams](#erd)
   * [Use Diagram](#use)
   * [Class Diagram](#cla)
	
[Testing](#testing)
   * [Analyse Report](#report)
     
[Deployment](#depl)
   * [Technologies Used in the Development](#tech)
     
[Interface](#inte)
   * [Demo](#demo)
   
[Author](#auth)


<a name="brief"></a>
## The Brief

To create an OOP-based application with utilisation of supporting tools (Github, Jenkins, Linux ), methodologies ( Agile ) and technologies that encapsulate all core modules covered during QA Intensive training such HTML, Python and SQL ).
Aplication posses the capacity to manipulate a database ( CRUD - create, read, update and delete functionality ) using front end interface created using Flask Python framework.

This project involve concepts from all core training modules, as such:
* Agile
* Python Fundamentals
* Python Testing
* Git
* Continuous Integration
* Basic Linux
* Python Web Development
* Cloud Fundamentals
* Databases

<a name="solution"></a>
### Solution

I decided to create an e-commerce application that would allow the user to create and update own account, add and delete review of the store or product and also add, read and delete product from the products table acessing to the Store page.

<a name="setup"></a>
### Setup
```bash
# create virtual environment
python3 -m venv
# load virtual environment
source venv/bin/activate
# make sure our dependencies are installed
pip install -r requirements.txt
```


<a name="pro"></a>
## Project Management

[![trello.png](https://www.imageupload.net/upload-image/2020/02/20/trello.png)](https://www.imageupload.net/image/RIK6c)

<a name="ris"></a>
## Risk Assessment


<a name="arch"></a>
## Architecture

<a name="erd"></a>
### Entity Relationship Diagrams


<a name="use"></a>
### Use Diagram
[![use-case26853d33381d65c4.png](https://www.imageupload.net/upload-image/2020/02/20/use-case26853d33381d65c4.png)](https://www.imageupload.net/image/RucKy)

<a name="cla"></a>
### Class Diagram
<a href="https://ibb.co/2MtwCvX"><img src="https://i.ibb.co/R601s3L/project-class.png" alt="project-class" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'></a>

<a name="testing"></a>
## Testing
????????????????   tests have been used for automated testing, and SonarLint/SonarQube for static reporting and refactoring.

<a name="report"></a>
### Analyse Report

Picture and resuls of the test


<a name="dep"></a>
## Deployment
The build, test and deployment process was automated using Jenkins, with a webhook to GitHub which was triggered with every push event

This application can be deployed both locally and externally through a virtual machine. The constants.js file has commented out options to switch from an external to local IP address.

[![CI_pipeline.jpg](https://www.imageupload.net/upload-image/2020/02/20/CI_pipeline.jpg)](https://www.imageupload.net/image/Ru0uc)

<a name="tech"></a>
### Technologies Used
* [Trello](https://trello.com/b/VFRNnQYX/project-sfia) - Project Management
* SQLlite - Database
* Docker - Deployment
* Jenkins - CI Server
* Maven - Dependency Management
* pytest - Test Reporting & Static Testing
* [Git](https://github.com/PauloRibeiroIT/Paulo_SFIA1) - VCS
* GCP - Live Environment

<a name="inte"></a>
## Interface
[![sssss.md.png](https://www.imageupload.net/upload-image/2020/02/20/sssss.md.png)](https://www.imageupload.net/image/RuoPp)

<a name="demo"></a>
### Demo
Demo accessible in the url below:


<a name="auth"></a>
## Author
Paulo Ribeiro - DevOps Consultant
2020
