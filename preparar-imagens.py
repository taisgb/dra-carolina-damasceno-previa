from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlsplit
from PIL import Image, ImageOps
import re, io, json, hashlib
root=Path(__file__).resolve().parent
file=root/'index.html'; html=file.read_text(encoding='utf-8'); assets=root/'assets'; assets.mkdir(exist_ok=True)
manifest={}; path=root/'chicote'/'imagens.json'
if path.exists(): manifest=json.loads(path.read_text(encoding='utf-8'))
urls=set(re.findall(r'src="(https://dracarolinadamasceno\.com/wp-content/uploads/[^\"]+)"',html))
for url in sorted(urls):
    name=Path(urlsplit(url).path).stem; target=assets/(name+'-'+hashlib.sha256(url.encode()).hexdigest()[:8]+'.webp')
    try:
        req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urlopen(req,timeout=20) as response: raw=response.read()
        with Image.open(io.BytesIO(raw)) as source:
            img=ImageOps.exif_transpose(source);img.thumbnail((1200,1600));img.save(target,'WEBP',quality=83,method=6)
        relative=target.relative_to(root).as_posix();html=html.replace('src="'+url+'"','src="'+relative+'"');manifest[url]={'local':relative,'bytes':target.stat().st_size}; print('OK',relative)
    except Exception as exc: manifest[url]={'erro':str(exc)};print('Falhou',url,exc)
file.write_text(html,encoding='utf-8');path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
