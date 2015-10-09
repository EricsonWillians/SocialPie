virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
  # See: http://stackoverflow.com/questions/23418735/using-python-3-3-in-openshifts-book-example?noredirect=1#comment35908657_23418735
  #execfile(virtualenv, dict(__file__=virtualenv)) # for Python v2.7
  #exec(compile(open(virtualenv, 'rb').read(), virtualenv, 'exec'), dict(__file__=virtualenv)) # for Python v3.3
  # Multi-Line for Python v3.3:
  exec_namespace = dict(__file__=virtualenv)
  with open(virtualenv, 'rb') as exec_file:
    file_contents = exec_file.read()
  compiled_code = compile(file_contents, virtualenv, 'exec')
  exec(compiled_code, exec_namespace)
except IOError:
  pass
