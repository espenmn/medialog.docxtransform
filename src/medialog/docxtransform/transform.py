# -*- coding: utf-8 -*-
"""
Our transform requires installation of docx2txt 
"""
import mimetypes 
from Products.PortalTransforms.interfaces import ITransform
from zope.interface import implementer
from Products.PortalTransforms.libtransforms.commandtransform import popentransform
from .config import SITE_CHARSET, TRANSFORM_NAME

# Alternative 'manual transform:
from docx import Document 
# These lines should not be needed
from io import BytesIO
 


@implementer(ITransform)
class DocxToText(popentransform):
    __name__ = TRANSFORM_NAME
    name = TRANSFORM_NAME
    inputs = (
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
      'application/vnd.openxmlformats-officedocument.wordprocessingml.template',       
    )    
    output = 'text/plain'
    output_encoding = SITE_CHARSET
    binaryName = "docx2txt"
    binaryArgs = "$infile $outfile"
    binary = "docx2txt"
    
    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.__name__ = name


    # def convert(self, orig, idata, **kwargs):
    #     # doctext.DocFile(doc=path_to_docx_file)
    #     # out = []
    #     # text = docx2txt.process(BytesIO(orig))
    #     # out.extend(self.clean_data(data=text))
    #     # idata.setData(" ".join(out))
    #     return 'idata brannmann'

 

    
def register():
    return DocxToText()

 