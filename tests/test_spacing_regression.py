import importlib.util,tempfile,unittest,zipfile
from pathlib import Path
from xml.dom import minidom
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('spacing_builder',ROOT/'skills/bto-cv/scripts/build_docx.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
class ExperienceSpacingTests(unittest.TestCase):
 def test_same_style_spacing_is_explicitly_enabled(self):
  data={'initials':'T.E.','experience':[{'dates':'2026','role':'Test','employer':'Example','bullets':['First','Last']}],'education':['Education']}
  with tempfile.TemporaryDirectory() as tmp:
   output=Path(tmp)/'test.docx';builder.build(data,output)
   with zipfile.ZipFile(output) as z:doc=minidom.parseString(z.read('word/document.xml'))
   ps={builder.text(p):p for p in doc.getElementsByTagNameNS(builder.W,'p')}
   for text,after in [('First','100'),('Last','0')]:
    self.assertEqual(ps[text].getElementsByTagNameNS(builder.W,'spacing')[0].getAttributeNS(builder.W,'after'),after)
    self.assertEqual(ps[text].getElementsByTagNameNS(builder.W,'contextualSpacing')[0].getAttributeNS(builder.W,'val'),'0')
   self.assertFalse(ps['Education'].getElementsByTagNameNS(builder.W,'contextualSpacing'))
