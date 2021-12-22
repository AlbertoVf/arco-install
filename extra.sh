#!/bin/bash

# Javascript
sudo npm install -g http-server jshint nodemon # http server
sudo npm install -g typescript @angular/cli @ionic/cli cordova

# composer
curl -sS https://getcomposer.org/installer -o composer-setup.php
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer

#symfony
wget https://get.symfony.com/cli/installer -O - | bash
sudo mv $HOME/.symfony/bin/symfony /usr/local/bin/symfony

# laravel
composer global require laravel/installer

# cups
sudo systemctl start cups
sudo systemctl enable cups

# OH MY ZSH
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
