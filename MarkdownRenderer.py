'''This program will read in a markdown format file (.md) 
It will output a static HTML page from the md file.'''

import markdown


with open(input("Please enter the filename you wish to convert (.md): "), encoding='utf-8') as markdown_file:
    data = markdown_file.read()

    with open('example.html', mode='w', encoding='utf-8') as html_file:
        html_file.write(markdown.markdown(data, output_format='html5'))
        