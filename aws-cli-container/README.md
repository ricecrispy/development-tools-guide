# Running a ubuntu container with AWS + SAM + Terraform CLI from WSL using VSCode

## Purpose

This project contains a Dockerfile which starts a container in VSCode installed with AWS CLI, AWS SAM CLI, and Terraform CLI

## Pre-requisites

VSCode

WSL with Docker installed

## Setting up

Start WSL and run the following commands:


```
git clone https://github.com/ricecrispy/development-tools-guide.git

cd development-tools-guide/aws-cli-container

code .

```

Follow this [article](https://code.visualstudio.com/blogs/2020/07/01/containers-wsl) to install all the VSCode extensions needed

In VSCode, type `control + shift + p`, then type `Remote-Containers: Reopen in container`

