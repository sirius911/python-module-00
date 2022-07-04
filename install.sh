#!/bin/sh

MYPATH="/goinfre/$USER/miniconda3

#Download & install conda
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH

# For zsh
$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc

#Create an environment for 42AI
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyl
