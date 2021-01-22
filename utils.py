import streamlit.components.v1 as stc
from textblob import TextBlob
from collections import Counter
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')


HTML_RANDOM_TEMPLATE = """<div style='padding:10px;background-color:#E1E2E1;
border-radius: 8px 34px 9px 26px;
-moz-border-radius: 8px 34px 9px 26px;
-webkit-border-radius: 8px 34px 9px 26px;
border: 2px ridge #000000;'>
<h5>Verse of the Day</h5>
<p>{}</p></div>"""


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
HTML_BANNER = """<div style="background-color:#464e5f;padding:10px;border-radius:10px">
<h1 style="color:white;text-align:center;">StreamBible App </h1>
</div>"""

TAGS = {
    'NN': 'green',
    'NNS': 'green',
    'NNP': 'green',
    'NNPS': 'green',
    'VB': 'blue',
    'VBD': 'blue',
    'VBG': 'blue',
    'VBN': 'blue',
    'VBP': 'blue',
    'VBZ': 'blue',
    'JJ': 'red',
    'JJR': 'red',
    'JJS': 'red',
    'RB': 'cyan',
    'RBR': 'cyan',
    'RBS': 'cyan',
    'IN': 'darkwhite',
    'POS': 'darkyellow',
    'PRP$': 'magenta',
    'PRP$': 'magenta',
    'DET': 'black',
    'CC': 'black',
    'CD': 'black',
    'WDT': 'black',
    'WP': 'black',
    'WP$': 'black',
    'WRB': 'black',
    'EX': 'yellow',
    'FW': 'yellow',
    'LS': 'yellow',
    'MD': 'yellow',
    'PDT': 'yellow',
    'RP': 'yellow',
    'SYM': 'yellow',
    'TO': 'yellow',
    'None': 'off'
}


def render_entities(raw_text):
    docx = nlp(raw_text)
    html = displacy.render(docx, style='ent')
    html = html.replace("\n\n", "\n")
    result = HTML_WRAPPER.format(html)
    stc.html(result, height=1000)


def get_tags(docx):
    tagged_docx = TextBlob(docx).tags
    return tagged_docx


def mytag_visualizer(tagged_docx):
    colored_text = []
    for i in tagged_docx:
        if i[1] in TAGS.keys():
            token = i[0]
            # print(token)
            color_for_tag = TAGS.get(i[1])
            result = '<span style="color:{}">{}</span>'.format(color_for_tag, token)
            colored_text.append(result)
    result = ' '.join(colored_text)
    # print(result)
    return result
