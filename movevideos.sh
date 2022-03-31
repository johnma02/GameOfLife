#!/bin/bash

VALIDINPUT=0

while [ $VALIDINPUT -eq 0 ]
do
  echo "Would you like to create a new directory to save this video in? [Y/n]"

  read -r NEWDIRECTORY

  if [ $NEWDIRECTORY == "Y" ] ; then
  NEWDIRECTORY=1
  VALIDINPUT=1

  elif [ $NEWDIRECTORY == "n" ] ; then
  NEWDIRECTORY=0
  VALIDINPUT=1
  fi
done

if [ $NEWDIRECTORY -eq 1 ] ; then
  echo "Enter the path for your new directory"
  echo "Your gif will be saved in this directory"
  read PATHNAME
  mkdir $PATHNAME
  mv $1 $PATHNAME

else
  echo "Enter path for directory, press enter if you would like to save to the current working directory (/GameOfLife)"
  read PATHNAME
  PATHEXISTS=0
  while [ PATHEXISTS -eq 0 ]
  do
    if [ -d $PATHNAME] ; then
      mv $1 $PATHNAME
      PATHEXISTS=1
    else
      echo "Error: path does not exist"
    fi
  done
fi

