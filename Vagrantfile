Vagrant.configure(2) do |config|
  config.vm.box = "jessie64"
  config.vm.box_url = "https://downloads.sourceforge.net/project/vagrantboxjessie/debian80.box"
  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.synced_folder "~/dev/projects/legere.cc", "/home/webapps/legere.cc"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
  
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get upgrade -y
	sudo apt-get install nginx build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev libreadline-dev python-dev python-pip python-virtualenv -y
    wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tgz
	tar -xzf Python-3.4.2.tgz && cd Python-3.4.2
	./configure --with-zlib
	make && sudo make install
	sudo useradd -a www-data -d /home/webapps webapps
	sudo -i -u webapps; cd ~/legere.cc
  SHELL
end
