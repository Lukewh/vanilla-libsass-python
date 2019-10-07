# libsass-python

This is a proof of concept to test the output of libsass-python against node-sass for Vanilla Framework SCSS library.

## Install
### Python

`pip install -r requirements.txt`

### Node

`npm install`

## Run

`python app.py`

This will compile the SCSS from `static/scss/styles.scss` to `static/css/styles.css` (with sourcemaps).

# This does not autoprefix the generated CSS

I can't find a Python module anywhere that prefixes CSS