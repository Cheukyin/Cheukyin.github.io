#Must use source command to run this script, not the dot

mkdir _py_virtualenv 
pip2 install virtualenv && virtualenv _py_virtualenv --no-site-packages && source _py_virtualenv/bin/activate && pip2 install pygments && pip2 install beautifulsoup4
