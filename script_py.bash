#!/bin/bash
for i in $(ls ./jupyter_files/*.ipynb)
	do
		echo "$i" 
		jupyter nbconvert --to script $i
		mv -f ./jupyter_files/*.py ./python_files/
done; 
