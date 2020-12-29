
Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/bionic64"

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
  
  sudo apt-get update


  # Configure networking
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  auto_correct: true



  # Install pyenv prerequisites
  sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
      xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
  

  # Clone pyenv
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv

  # Set PATH variable
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile

  # Initilise pyenv
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile

  # Refresh shell for PATH changes to take effect
  . ~/.profile

  # Install new python version and set as default
  pyenv install 3.9.0
  pyenv global 3.9.0

  # Install poetry
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python



  SHELL

  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script"
    trigger.run_remote = {privileged: false, inline: "
    # Install dependencies and launch
    cd /vagrant
    poetry install
    poetry run flask run --host=0.0.0.0
"}
end

end