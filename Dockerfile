FROM python:3.9-buster

# update os
RUN apt-get update

# set working directory and copy in files 
WORKDIR /todo-app
COPY . /todo-app

# Pyenv dependancies
RUN apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
      xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# Clone pyenv
RUN  git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Set pyenv PATH variable
RUN  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
RUN  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

# Initilise pyenv
RUN  echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

# Refresh shell for PATH changes to take effect
SHELL ["bash", "-lc"]

# Install new python version and set as default
RUN pyenv install 3.9.0
RUN pyenv global 3.9.0

# Install poetry and Gunicorn and project dependancies
RUN pip install poetry gunicorn flask
RUN poetry install

# Set environment to run
# RUN export FLASK_ENV=production

EXPOSE 5000

# Add the directory containing poetry to the path environmental variables
ENV PATH=/root/.pyenv/shims:$PATH

# ENTRYPOINT [ "bash" ]
ENTRYPOINT [ "poetry" ]

# Run gunicorn
CMD [ "run", "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app" ]