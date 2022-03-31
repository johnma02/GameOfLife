#!/bin/bash

#This is a simple shell script that is called by main.py in order to move saved gifs to user set directories
#Args: file name, newDirectory, pathName

if [ $2 -eq 1 ] ; then
  if [ -d $3 ] ; then
    echo "Error: directory or file already exists"
    exit 1
  fi
  echo "Creating new directory at $3"
  echo "Saving game to $3"
  mkdir $3
  mv $1 $3

else
  if [ -d $3 ] ; then
    if [ -f $1 ] ; then
      echo "Error: file already exists in named directory with same name!"
      exit 1
    fi
    echo "Saving game to $3"
    mv $1 $3
  else
    echo "Error: path not found"
    exit 1
  fi
fi
echo "Successfully saved $1 to $3"
exit 0
