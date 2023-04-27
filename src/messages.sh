#!/bin/sh

red() {
	printf "\e[1;31m$1\e[0;37m\n"
}

green() {
	printf "\e[1;32m$1\e[0;37m\n"
}

blue() {
	printf "\e[1;34m$1\e[0;37m\n"
}

yellow() {
	printf "\e[1;33m$1\e[0;37m\n"
}
