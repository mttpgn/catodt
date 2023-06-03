#!/usr/bin/env python3

import os
import sys
from odf import text, teletype
from odf.opendocument import load, OpenDocumentText
from odf.style import Style, TextProperties
import pypandoc


def cleanupIntermediaryFiles(output_file):
    temp_file = output_file.replace('.pdf', '.odt') if output_file.endswith('.pdf') else output_file
    md_file = temp_file.replace('.odt', '.md')
    html_file = temp_file.replace('.odt', '.html')
    cleanup_done = False
    if os.path.exists(md_file):
        os.remove(md_file)
        cleanup_done = True
    if os.path.exists(html_file):
        os.remove(html_file)
        cleanup_done = True
    return cleanup_done


def concatenateDocuments(directory, output_file):
    files = sorted(os.listdir(directory))
    all_doc = OpenDocumentText()
    odt_files_exist = False
    # Define a new style for Chapter headings
    chapter_style = Style(name="ChapterStyle", family="paragraph")
    chapter_props = TextProperties(fontweight="bold", fontsize="28pt")
    chapter_style.addElement(chapter_props)
    # Add the style to the document's automatic styles
    all_doc.automaticstyles.addElement(chapter_style)
    for file in files:
        file_path = os.path.join(directory, file)
        if file.endswith('.odt'):
            doc = load(file_path)
            # Concatenate ODT documents
            for paragraph in doc.getElementsByType(text.P):
                para_text = teletype.extractText(paragraph)
                new_paragraph = text.P(
                    stylename=chapter_style if para_text.startswith("Chapter") else None,
                    text=para_text
                )
                all_doc.text.addElement(new_paragraph)
                odt_files_exist = True
    if not odt_files_exist:
        print("Error: No ODT files found in the directory.")
        sys.exit(1)
    # Save the concatenated document as ODT
    temp_file = output_file.replace('.pdf', '.odt') if output_file.endswith('.pdf') else output_file
    all_doc.save(temp_file)
    # Convert to PDF using pypandoc if output_file ends with .pdf
    if output_file.endswith('.pdf'):
        html_file = temp_file.replace('.odt', '.html')
        pypandoc.convert_file(temp_file, 'html', outputfile=html_file)
        with open(html_file, 'r') as f:
            lines = f.readlines()
        with open(html_file, 'w') as f:
            for line in lines:
                if line.strip().startswith("<p>Chapter"):
                    line = line.replace("<p>Chapter", "<h1>Chapter")
                    line = line.replace("</p>", "</h1>")
                f.write(line)
        pypandoc.convert_file(
            html_file,
            'pdf',
            outputfile=output_file,
            extra_args=['--pdf-engine=xelatex'],
        )
    cleanupIntermediaryFiles(output_file)
    return output_file


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: concatenate_documents.py <directory> <output_file>")
        sys.exit(1)
    directory = sys.argv[1]
    output_file = sys.argv[2]
    output_file = concatenateDocuments(directory, output_file)
    print(f"Concatenated document saved as {output_file}")
