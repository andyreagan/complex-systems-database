from jinja2 import Environment
from urllib.request import urlopen
from json import loads
from os.path import isfile
from datetime import datetime
import click


def latexescape(value, format='%H:%M / %d-%m-%Y'):
    return value.replace("#", r"\#").replace("%", r"\%")


env = Environment()
env.filters['latexescape'] = latexescape

PAPER_LIST_TEMPLATE = env.from_string(r"""
\begin{longtable}{c p{\rtcolw}}
{% for paper in papers %}
\parbox[c]{1.9cm}{ \href{ {{- paper.titlelink -}} }{\includegraphics[height=1.8cm]{figures/{{ paper.image -}} }} }
& \parbox[c]{\rtcolw}{\textbf{ {{- loop.revindex }}. {{ paper.title | latexescape -}} }  \hfill {{ paper.year }} \\ {% for author in paper.author %} {{ author.fullname }}{% if not loop.last %},{% endif %} {% endfor -%} } \\
{% endfor %}
 \end{longtable}
""")

PAPER_LIST_TEMPLATE_RESUME = env.from_string(r"""{% for paper in papers -%}
\textcolor{linkcolor}{\href{ {{- paper.titlelink -}} }{ {{- paper.title | latexescape -}} } }

{% for author in paper.author -%} {{ author.fullname -}} {% if not loop.last %},{% endif %} {% endfor %}

{% if paper.journalpagelink %}\textit{ {{- paper.journal -}} }, \textbf{ {{- paper.volume -}} }, {{ paper.pages }}, {{ paper.year }}{% else %}Preprint available on the \textcolor{linkcolor}{\href{ {{- paper.arxivlink -}} }{arXiv}}{%- endif -%}.
{# \includegraphics[height=1.8cm]{figures/{{ paper.image -}} }} } #}
\vspace{6px}
{% endfor %}
""")

PRESS_LIST_TEMPLATE = env.from_string(r'''\begin{longtable}{c p{\rtcolw}}
{% for press in press_all %}
\parbox[c]{1.1cm}{ \href{ {{- press.url -}} }{\includegraphics[width=1.1cm]{figures/{{ press.image -}} }} }
& \parbox[c]{\rtcolw}{ {\small \textcolor{blue}{\textit{\href{ {{- press.title -}} } { {{- press.title -}} } } } }\\ \textbf{ {{- press.organization -}} }, {{ press.date }} }\\
{% endfor %}
 \end{longtable}
''')

PRESS_LIST_TEMPLATE_TWO_ROWS = env.from_string(r'''\begin{longtable}{c p{7.5cm} c p{7.5cm} }
{% for press in press_selected %}
\parbox[c]{1.1cm}{ \href{ {{- press.url -}} }{\includegraphics[width=1.1cm]{figures/{{ press.image -}} }} }
& \parbox[c]{7.5cm}{ {\small \textcolor{blue}{\textit{\href{ {{- press.url -}} } { {{- press.title -}} } } } }\\ \textbf{ {{- press.organization -}} }, {{ press.formatted_date }} } {% if loop.index is divisibleby(2) %} \\
\rule{0pt}{5ex}{% else %} & {% endif %} {% endfor %}
 \end{longtable}
''')


@click.command()
@click.argument('username')
@click.option('--filename', default=None, help="Prefix to use for output tex files.")
def main(username, filename):
    if filename is None:
        filename = username
    endpoint = urlopen(
        "http://vermontcomplexsystems.org/api/v1/person/?format=json&uname={}".format(username))
    result_raw = endpoint.read().decode('utf-8')
    result_json = loads(result_raw)
    for result in result_json["objects"]:
        print("found user {}".format(result["fullname"]))

    print("using the first user result")
    my_result = result_json["objects"][0]

    for paper in my_result["papers"]:
        print("found paper {}".format(paper["title"]))
        # save the figures
        image_link = "http://vermontcomplexsystems.org/{}".format(
            paper["image"])
        print(image_link)
        image_filename = list(image_link.split(
            "/")[-1].replace(" ", "-").replace("%20", "-").replace(".", "-"))
        image_filename[-4] = "."
        image_filename = "".join(image_filename)
        if not isfile("figures/" + image_filename):
            f = open("figures/" + image_filename, "wb")
            f.write(urlopen(image_link).read())
            f.close()
        image_filename_square = image_filename[:-4] + \
            "-200x200-rounded" + image_filename[-4:]
        paper["image"] = image_filename
        paper["image"] = image_filename_square
        # paper["image"] = image_filename
        max_authors = 5
        if len(paper["author"]) > max_authors:
            paper["author"] = paper["author"][:(max_authors + 1)]
            paper["author"][max_authors] = {"fullname": "et. al."}

    for press in my_result["press_selected"]:
        print("found press {}".format(press["title"]))
        # save the figures
        image_link = "http://vermontcomplexsystems.org/{}".format(
            press["image"])
        print(image_link)
        image_filename = list(image_link.split(
            "/")[-1].replace(" ", "-").replace("%20", "-").replace(".", "-"))
        # image_filename = image_filename.replace(".","_").replace("%","_")
        image_filename[-4] = "."
        image_filename = "".join(image_filename)
        print(image_filename)
        if not isfile("figures/" + image_filename):
            f = open("figures/" + image_filename, "wb")
            f.write(urlopen(image_link).read())
            f.close()
        # press["image"] = image_filename
        image_filename_square = image_filename[:-
                                               4] + "-100x100" + image_filename[-4:]
        press["image"] = image_filename
        press["image"] = image_filename_square
        press["title"] = press["title"].replace("&", "\&")
        press["date"] = datetime.strptime(press["date"], "%Y-%m-%dT%H:%M:%S")
        press["formatted_date"] = press["date"].strftime("%B %-d, %Y")

    # render and save the template
    f = open("{0}.papers.tex".format(filename), "w")
    f.write(PAPER_LIST_TEMPLATE.render(my_result))
    f.close()

    # render and save the template
    f = open("{0}.papers-resume.tex".format(filename), "w")
    f.write(PAPER_LIST_TEMPLATE_RESUME.render(my_result))
    f.close()

    # render and save the template
    f = open("{0}.press.tex".format(filename), "w")
    f.write(latexescape(PRESS_LIST_TEMPLATE.render(my_result)))
    f.close()

    # render and save the template
    f = open("{0}.press-tworows.tex".format(filename), "w")
    f.write(latexescape(PRESS_LIST_TEMPLATE_TWO_ROWS.render(my_result)))
    f.close()


if __name__ == '__main__':
    main()
