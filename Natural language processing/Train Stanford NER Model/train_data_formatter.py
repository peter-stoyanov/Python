"""Prepare training data for Stanford NER classifier.

    Reads xml files with the following structure:
    <data>
        <row>
            <id>9598114</id>
            <type>Organization</type>
            <name>MIT Sloan School</name>
            <text> ... </text>
        </row>
    </data>

"""

import os
# from xml.dom.minidom import parse
import xml.dom.minidom
import nltk

def main():
    """Prepare training data for Stanford NER classifier"""

    dir_path = os.getcwd() + "\\Natural language processing\\Train Stanford NER Model"

    rows = read_from_file(dir_path)

    # store word-tag pairs in a dictionary grouped by article Id as key
    article_tagged_tokens = {}

    for article in rows:

        article_id = article.getElementsByTagName("id")[0].childNodes[0].data
        siera_entity_type = article.getElementsByTagName("type")[0].childNodes[0].data
        entity_name = article.getElementsByTagName("name")[0].childNodes[0].data.lower()
        text = article.getElementsByTagName("text")[0].childNodes[0].data

        if article_id not in article_tagged_tokens:
            # load article words with default 'O' tag only the first time the article is read
            sentences = nltk.sent_tokenize(text)
            article_tagged_tokens[article_id] = [list((word.lower(), 'O')) for sentence in sentences for word in nltk.word_tokenize(sentence)]

        # update default tag if the entity name parts are equal to the current word token
        for word_tag in article_tagged_tokens[article_id]:
            for entity_name_part in entity_name.split():
                if entity_name_part == word_tag[0]:
                    word_tag[1] = get_stanford_tag(siera_entity_type)

    flat_list_tags = [pair for value in article_tagged_tokens.values() for pair in value]

    save_to_file(dir_path, flat_list_tags)

def read_from_file(dir_path):
    """Read and parse raw articles data"""
    try:
        import_file = dir_path + "\\raw_train_data.xml"

        # Open XML document using minidom parser
        dom_tree = xml.dom.minidom.parse(import_file)
        collection = dom_tree.documentElement

        return collection.getElementsByTagName("row")

    except IOError:
        print("Could not read file: " + import_file)


def save_to_file(dir_path, tagged_tokens):
    """Serialize token - tag pairs to file"""
    try:

        export_file = dir_path + "\\formatted_train_data.tsv"
        file = open(export_file, mode="w", encoding="utf8")

        for (word, tag) in tagged_tokens:
            line = word + '\t' + tag
            file.write(line + '\n')

    except IOError:
        print("Could not write file: " + export_file)
    finally:
        file.close()

def get_stanford_tag(siera_tag):
    """Returns the corresponding Stanford NER tag on given Siera entity tag"""

    mapping = {
        'Individual' : lambda _: 'PERS',
        'Location' : lambda _: 'LOC',
        'Organization' : lambda _: 'ORG',
        'Brand' : lambda _: 'O',
        'Publication' : lambda _: 'O',
        'Hashtag' : lambda _: 'O'
    }

    return mapping[siera_tag](None) if siera_tag in mapping else 'O'

if __name__ == '__main__':
    main()
