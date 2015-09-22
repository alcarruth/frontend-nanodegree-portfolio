#!/usr/bin/env python

import os
import sys

portfolio_root = os.getcwd()
sys.path.append(portfolio_root + '/python')
from portfolio_util import read_file, write_file, data_url, indent

dist_dir = portfolio_root + '/dist/'
src_dir =  portfolio_root + '/src/'
template_dir = portfolio_root + '/src/templates/'

tile_template = read_file(template_dir + 'tile_template.html')
page_template = read_file(template_dir + 'page_template.html')

class Featured_Tile:

    def __init__(self, href, src, alt):
        self.href = href
        self.src = src
        self.alt = alt

    def to_html(self, inline=False):
        if inline:
            img = read_file(dist_dir + self.src, 'b')
            src = data_url(img).strip()
        else:
            src = self.src
        html = tile_template.format(
            featured_tile_href = self.href,
            featured_tile_alt = self.alt,
            featured_tile_src = src
        )
        return html

tiles = [
    Featured_Tile(
        "http://linode-01.armazilla.net/lazy_a_ranch",
        "images/lazy_a_ranch-600.jpg",
        "Lazy A Ranch"
    ),
    Featured_Tile(
        "http://linode-01.armazilla.net/gerberman_jewelers",
        "images/gerberman_jewelers-600.jpg",
        "Gerberman Jewelers"
    ),
    Featured_Tile(
        "http://www.carsonmarketing.com",
        "images/carson_marketing-600.jpg",
        "Carson Marketing"
    ),
    Featured_Tile(
        "http://linode-01.armazilla.net/fresh_tomatoes/fresh_tomatoes.html",
        "images/fresh_tomatoes-600.jpg",
        "Fresh Tomatoes"
    ),
    Featured_Tile(
        "http://www.greenproshouston.com",
        "images/greenpros-600.jpg", 
        "GreenPros"
    ),
    Featured_Tile(
        "http://linode-01.armazilla.net/front-end-ninja/index.html",
        "images/front_end_ninja-600.jpg",
        "Front End Ninja"
    )
]

def gen_html(inline=False):
    featured_tiles = str.join('\n', map(lambda(tile): tile.to_html(inline), tiles))
    page = page_template.format(
        header_logo_alt = "Picture of Al",
        header_logo_src = "images/al_carruth-600.jpg", 
        featured_tiles = indent(featured_tiles,10)
    )
    return page

def gen_css():
    dist_file = 'portfolio.css'
    src_files = ['colors.css', 'style.css', 'sizes.css']
    css = "/* %s generated from %s */\n" % (dist_file, src_files)
    for css_file in src_files:
       css += read_file(src_dir + 'style/' + css_file)
    return css

write_file(gen_html(), dist_dir + 'portfolio.html')
#write_file(gen_html(True), dist_dir + 'portfolio_inline.html')
write_file(gen_css(), dist_dir + 'style/portfolio.css')

