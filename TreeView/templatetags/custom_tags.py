import os

from django import template
from dotenv import load_dotenv

from TreeView.models import Paragraph

register = template.Library()

dotenv_path = os.path.join(os.path.abspath(os.curdir), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def get_child_paragraph(parent, num_gen, tab):
    if num_gen == 0:
        return None
    children = Paragraph.objects.select_related('parent').filter(parent_id=parent.id)
    child_list = []
    for children in children:
        child_list.append({
            'title': children.title,
            'url': children,
            'tab': tab,
            'child': get_child_paragraph(children, num_gen - 1, tab * 2),
        })

    return child_list


def get_menu(name, num_gen, tabulate):
    if name:
        paragraphs = Paragraph.objects.filter(title=str(name))
    else:
        paragraphs = Paragraph.objects.filter(parent_id=None)

    paragraph_list = []
    for paragraph in paragraphs:
        paragraph_list.append({
            'title': paragraph.title,
            'url': paragraph,
            'tab': 0,
            'child': get_child_paragraph(paragraph, num_gen, tabulate),
        })
    return {'paragraph_list': paragraph_list}


@register.inclusion_tag('menu.html')
def draw_menu(name=None, num_gen=int(os.getenv("NUM_GEN")), tabulate=int(os.getenv("TABULATE"))):
    return get_menu(name, num_gen, tabulate)
