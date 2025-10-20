# -*- coding: utf-8 -*-
"""
Our transform requires installation of docx2txt 
"""
import mimetypes
from Products.PortalTransforms.interfaces import ITransform
from zope.interface import implementer
from Products.PortalTransforms.libtransforms.commandtransform import popentransform

# Alternative 'manual transform:
# from docx import Document 


@implementer(ITransform)
class word_docx_to_text(popentransform):
    __name__ = "word_docx_to_text"
    inputs = ("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    output = "text/plain"
    output_encoding = "utf-8"    
    binaryName = "docx2txt"
    binaryArgs = "- -enc UTF-8 -"
    

def register():
    return word_docx_to_text()


