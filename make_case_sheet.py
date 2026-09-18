from pathlib import Path
import subprocess, json, math
from PIL import Image, ImageDraw, ImageFont

base=Path('/Users/laina/.hermes/profiles/sales/workspace/liuyun-technology')
rows=json.loads((base/'cases.json').read_text())
outdir=base/'qa_frames'; outdir.mkdir(exist_ok=True)
thumbs=[]
for row in rows:
    src=base/row['src']
    frame=outdir/(row['id']+'.png')
    if row['kind']=='video':
        subprocess.run(['/opt/homebrew/bin/ffmpeg','-y','-loglevel','error','-ss','0.7','-i',str(src),'-frames:v','1','-vf','scale=420:-1',str(frame)],check=False)
    else:
        try:
            im=Image.open(src).convert('RGB'); im.thumbnail((420,260)); im.save(frame)
        except Exception:
            continue
    if frame.exists():
        im=Image.open(frame).convert('RGB'); im.thumbnail((420,260)); thumbs.append((row,im.copy()))
cell_w,cell_h=460,330
cols=3; rows_n=math.ceil(len(thumbs)/cols)
sheet=Image.new('RGB',(cols*cell_w,rows_n*cell_h),'#eef4f4'); draw=ImageDraw.Draw(sheet)
for i,(row,im) in enumerate(thumbs):
    x=(i%cols)*cell_w+20; y=(i//cols)*cell_h+12
    sheet.paste(im,(x,y))
    draw.text((x,y+270),f"{row['id']} | {row['displayTitle']}",fill='#07152d')
sheet.save(base/'case-contact-sheet.png')
print({'thumbs':len(thumbs),'sheet':str(base/'case-contact-sheet.png')})
