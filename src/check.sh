#!/bin/bash

function red() {
	printf "\e[1;31m$1\e[0;37m\n"
}

function green() {
	printf "\e[1;32m$1\e[0;37m\n"
}

function blue() {
	printf "\e[1;34m$1\e[0;37m\n"
}

function yellow() {
	printf "\e[1;33m$1\e[0;37m\n"
}

function purple() {
	printf "\e[1;35m$1\e[0;37m\n"
}
