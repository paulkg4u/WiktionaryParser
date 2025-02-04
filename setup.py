from setuptools import setup,find_packages

with open('readme.md', 'r') as readme:
  long_desc = readme.read()

setup(
  name = 'wiktionaryparserntranslate',
  version = '0.0.96',
  description = 'A tool to parse word data from wiktionary.com into a JSON object',
  long_description = long_desc,
  long_description_content_type='text/markdown',
  packages = ['', 'tests', 'utils'],
  data_files=[('testOutput', ['tests/testOutput.json']), ('readme', ['readme.md']), ('requirements', ['requirements.txt'])],
  author = 'Suyash Behera',
  author_email = 'sne9x@outlook.com',
  url = 'https://github.com/paulkg4u/WiktionaryParser', 
  download_url = 'https://github.com/paulkg4u/WiktionaryParser/archive/master.zip', 
  keywords = ['Parser', 'Wiktionary'],
  install_requires = ['beautifulsoup4','requests'],
  classifiers=[
   'Development Status :: 5 - Production/Stable',
  ],
)