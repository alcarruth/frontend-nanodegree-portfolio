
# Udacity FEND - P1: Build a Portfolio Site

## Quick Start

Download project:

`$ git clone git@github.com:alcarruth/frontend-p1-portfolio.git`

`$ cd frontend-p1-portfolio/dist`

View regular portfolio:

`$ google-chrome portfolio.html`

or, for version with inline images:

 `$ google-chrome portfolio_inline.html`

## Features

 * media queries implement responsive design
 * `python/portfolio.py` generates `dist/portfolio.html`, `dist/portfolio_inline.html` and `dist/portfolio.css`
 * `portfolio.css` is the concatenation of `colors.css`, `style.css` and `sizes.css` 
 * image sizes reduced using `grunt` and `imageMagick`
 * Featured Work section includes six sites
 * Two featured works are from my nano degree projects and these also exhibit responsive design
 * "Fresh Tomatoes" is from FSND P1
 * "Jane Doett" is from portfolio mockup pdf

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

