# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.209.6/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use hirsuite or bionic on local arm64/Apple Silicon): hirsute, focal, bionic
ARG VARIANT="hirsute"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# Install AWS CLI
RUN su vscode -c "sudo curl -sSL https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip"
RUN su vscode -c "sudo unzip awscliv2.zip"
RUN su vscode -c "sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update"

# Install AWS SAM CLI
RUN su vscode -c "sudo curl -sSL https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip -o awssamcli.zip"
RUN su vscode -c "sudo unzip awssamcli.zip -d sam-installation"
RUN su vscode -c "sudo ./sam-installation/install"

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>


