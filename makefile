# Make to install requirements that come from github repositories
# https://stackoverflow.com/questions/55249689/pip-install-giturl-within-a-docker-environment
git clone https://github.com/JMendes1995/py_heideltime.git
cd REPO_DIR; python setup.py bdist_wheel
cp REPO_DIR/dist/* .
rm -rf REPO_DIR/