
# Udacity FEND - P1: Build a Portfolio Site

## Quick Start

Download project:

`$ git clone git@github.com:alcarruth/frontend-p1-portfolio.git`

To view regular portfolio:

`$ google-chrome dist/portfolio.html`

or, for version with inline images:

 `$ google-chrome dist/portfolio_inline.html`

## Features

 * Site uses media queries implement responsive design.
 * Inline image version is generated on the fly.
 * `python/portfolio.py` generates `dist/portfolio.html`, `dist/portfolio_inline.html` and `dist/portfolio.css`.
 * `portfolio.css` is the concatenation of `colors.css`, `style.css` and `sizes.css`.
 * The image sizes are reduced using `grunt` and `imageMagick`.
 * The Featured Work section includes six sites, two from my other nano degree projects.
 * *Fresh Tomatoes* is from FSND P1
 * *Jane Doett* is from portfolio `mockup.pdf` exercise.
 * *Fresh Tomatoes* and *Jane Doett* also feature responsive design.

## Directory Structure Overview

 * `dist/portfolio.html`
 * `dist/portfolio_inline.html` (with inline data url images)
 * `dist/images/*.jpg` - images to be href'd or inlined
 * `dist/style/portfolio.css`
 * `python/portfolio.py`
 * `python/portfolio_util.py`
 * `src/images/` - includes Gruntfile.js
 * `src/style/colors.css` - contains all color settings
 * `src/style/sizes.css` - contains the media queries and all size settings
 * `src/style/style.css` - fonts and general appearance
 * `src/templates/*.html` - templates used by `portfolio.py`

