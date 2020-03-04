[![codebeat badge](https://codebeat.co/badges/82f490f7-cebb-485e-a80b-db8c14c7fdb8)](https://codebeat.co/projects/github-com-ali-heidari-scm-master)

# scm

Simple Cent-os Management is a tool to set basic configs of a Cent OS server.
**NOTE: THIS IS A TRAINING PROJECT, DO NOT USE IT UNLESS YOU WANT TO CONTRIBUTE OR LEARN.**

## Requirements

1. CentOS 7+ x64
2. 1GB Free storage 
3. Python3

## Usage

1. `pip3 install -r requirements.txt`
2. `sudo python3 main.py`
3. **In case of failure because of python complaining about one of these reasons:**
    * No iscpy_core module exists
    * No method named WriteToFile/AddZone exists
use this `pip3 install git+https://github.com/ali-heidari/iscpy.git`

## The packages

1. cURL
    * Handles network requests
2. XAMPP
    * XAMPP is All-In-One. Little tricky but when you get familiar with it, you will be happy how everything managed.
    * [What is inside XAMPP](https://en.wikipedia.org/wiki/XAMPP#Components)

## Naming convention

We stick to the name convention described here:
[Python Naming Conventions](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)

## Coding rules

We use code beat to measure standard coding. You can check the rules here:
[CodeBeat rules](https://hub.codebeat.co/docs/language-supported)
