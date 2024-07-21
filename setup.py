name: Publish Python Package

on:
  push:
    branches:
      - main  

jobs:
  build-and-publish:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Check if setup.py is modified
      id: check_setup
      run: |
        if git diff --name-only HEAD^ HEAD | grep -q "setup.py"; then
          echo "setup.py changed"
          echo "changed=true" >> $GITHUB_ENV
        else
          echo "setup.py not changed"
          echo "changed=false" >> $GITHUB_ENV
        fi

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
      if: env.changed == 'true'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel twine
      if: env.changed == 'true'

    - name: Build package
      run: |
        python setup.py sdist bdist_wheel
      if: env.changed == 'true'

    - name: Publish package
      env:
        TWINE_USERNAME: _token_
        TWINE_PASSWORD: ${{ secrets.token }}
      run: |
        twine upload dist/*
      if: env.changed == 'true'
