#! /usr/bin/python3

import json
import os 
import codecs
from zipfile import ZipFile

config_file_path = 'settings.json' 

def load_config(config_file_path):
  with open(config_file_path) as uat_settings:
    return json.load(uat_settings)

def load_scripts(scripts_path):
  scripts = []
  for file in os.listdir(scripts_path):
      if file.endswith('.sql'):
        scripts.append(file)
  return scripts

def create_csv_file(config, server):
  scripts_path = config['scriptsPath']
  scripts = load_scripts(scripts_path)
  output_dir = '{scripts_path}/{filename}'.format(filename = config['filename'], scripts_path = scripts_path)

  with codecs.open(output_dir, 'w', encoding=config['encoding']) as file:
    for index, script in enumerate(scripts, start=1):
      line = '{index},{script},{server},{database}\n'.format(
        index = index, 
        script = script,
        server = server,
        database = config['database'])
      file.write(line)
    file.close()
  
def get_all_file_paths(directory):
  file_paths = []
  for root, directories, files in os.walk(directory):
    for filename in files:
      if filename.endswith('.zip'):
        continue
      filepath = os.path.join(root,filename)
      file_paths.append(filepath)
  return file_paths

def zip_files(scripts_path,server):
  file_paths = get_all_file_paths(scripts_path)

  print('The following Files will be zipped:')
  for path in file_paths:
    print(path)

  zip_filename = '{scripts_path}/{server}.zip'.format(server = server, scripts_path = scripts_path) 
  with ZipFile(zip_filename, 'w') as zip:
    for file in file_paths:
      filename = file[file.rfind('/') + 1:]
      zip.write(file, filename)
  zip.close()

  print('All files zipped sucessfully!')
  print('File Name : {name}'.format(name = zip_filename))

def run(config_file_path):
  config = load_config(config_file_path)
  servers = config['servers']
  scripts_path = config['scriptsPath']
  for server in servers:
    create_csv_file(config, server)
    zip_files(scripts_path, server)

run(config_file_path)
