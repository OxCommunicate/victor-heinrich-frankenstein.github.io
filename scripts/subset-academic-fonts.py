from pathlib import Path
import sys,json
import argparse
parser=argparse.ArgumentParser(description='Regenerate licensed Academic WOFF2 subsets from pinned official source files.')
parser.add_argument('sources',type=Path)
args=parser.parse_args()
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools import subset
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
chars=set(range(32,127))|{160}
for p in (root/'public').rglob('*.html'):
 s=BeautifulSoup(p.read_text(),'html.parser')
 for e in s(['script','style']): e.decompose()
 chars.update(map(ord,s.get_text()))
out=root/'assets/fonts/academic';out.mkdir(parents=True,exist_ok=True)
faces=[('Lora','Lora.ttf','Lora-normal.woff2',{'wght':(500,700)},'500 700','normal','Academic Heading'),('Source Serif 4','SourceSerif4.ttf','SourceSerif4-normal.woff2',{'wght':(400,700)},'400 700','normal','Academic Body'),('Source Serif 4','SourceSerif4-Italic.ttf','SourceSerif4-italic.woff2',{'wght':400},'400','italic','Academic Body'),('Source Code Pro','SourceCodePro.ttf','SourceCodePro-normal.woff2',{'wght':(400,600)},'400 600','normal','Academic Code')]
manifest=[]
for family,src,dest,axes,weight,style,newname in faces:
 font=instantiateVariableFont(TTFont(args.sources/src),axes,inplace=True)
 import io
 buffer=io.BytesIO();font.save(buffer);buffer.seek(0);font=TTFont(buffer)
 opt=subset.Options();opt.flavor='woff2';opt.name_IDs=['*'];opt.name_legacy=True;opt.name_languages=['*']
 sub=subset.Subsetter(options=opt);coverage=chars & set(font.getBestCmap());sub.populate(unicodes=coverage);sub.subset(font)
 # Subsets are modified fonts: rename internal families to respect reserved names.
 for record in font['name'].names:
  values={1:newname,2:'Italic' if style=='italic' else 'Regular',3:newname+'-'+style,4:newname+(' Italic' if style=='italic' else ''),6:newname.replace(' ','')+('-Italic' if style=='italic' else '-Regular'),16:newname,17:'Italic' if style=='italic' else 'Regular'}
  if record.nameID in values:record.string=values[record.nameID].encode(record.getEncoding())
 font.flavor='woff2';font.save(out/dest)
 manifest.append(dict(family=family,file='fonts/academic/'+dest,weight=weight,style=style))
 print(dest,(out/dest).stat().st_size,len(coverage))
lic=root/'static/fonts/academic';lic.mkdir(parents=True,exist_ok=True)
for name in ['Lora','SourceSerif4','SourceCodePro']:(lic/(name+'-OFL.txt')).write_bytes((args.sources/(name+'-OFL.txt')).read_bytes())
(root/'data').mkdir(exist_ok=True)
(root/'data/academic_fonts.json').write_text(json.dumps(manifest,indent=2)+'\n')
