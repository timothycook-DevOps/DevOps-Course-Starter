FROM python:3.9-buster as base

# update os
RUN apt-get update

# set working directory
WORKDIR /todo-app

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
SHELL [ "bash", "-lc" ]

# Install new python version and set as default
RUN pyenv install 3.9.0
RUN pyenv global 3.9.0

# Copy over files
COPY . /todo-app

# Install poetry and Flask and project dependancies
RUN pip install poetry flask
RUN poetry install

# Expose port 5000
EXPOSE 5000

# Add the directory containing poetry to the path environmental variables
ENV PATH=/root/.pyenv/shims:$PATH

# Define ENTRYPOINT 
ENTRYPOINT [ "poetry" ]

# Production environment
FROM base as production

# Install Gunicorn
RUN pip install gunicorn

# Run gunicorn for production
CMD [ "run", "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app" ]

# Development environment
FROM base as development

# Enable debugging for dev environment
ENV FLASK_ENV=development

# Run flask for development
CMD [ "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]

# Testing environment
FROM base as test

RUN pip install pytest

# Enable debugging for test environment
ENV FLASK_ENV=development

# ENTRYPOINT ["poetry", "run", "pytest"]
ENTRYPOINT ["poetry", "run"]
# ENTRYPOINT ["run", "poetry"]
# CMD ["run", "poetry", "pytest", "test_View_Model_Unit.py"]