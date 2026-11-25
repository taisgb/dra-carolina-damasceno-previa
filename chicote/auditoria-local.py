from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parents[1]
result=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for w,h in [(360,640),(390,844),(1440,900)]:
  page=browser.new_page(viewport={'width':w,'height':h},reduced_motion='reduce')
  # Ambiente sem rede: abortar externos para testar o layout de fallback de forma explícita.
  page.route('https://**/*',lambda route:route.abort())
  errors=[]; page.on('pageerror',lambda e:errors.append(str(e)))
  html=(root/'index.html').read_text().replace('<link rel="stylesheet" href="style.css">','<style>'+ (root/'style.css').read_text() +'</style>').replace('<script src="script.js" defer></script>','')
  page.set_content(html,wait_until='domcontentloaded');page.add_script_tag(content=(root/'script.js').read_text());page.wait_for_timeout(300)
  d=page.evaluate('''()=>{const c=document.querySelector('[data-cta=principal]').getBoundingClientRect();return {width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length,ctaTop:Math.round(c.top),ctaBottom:Math.round(c.bottom),ctaHeight:Math.round(c.height),ctaVisible:c.top>=0&&c.bottom<=innerHeight,brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).length,images:document.images.length,imagesWithAlt:[...document.images].filter(i=>i.hasAttribute('alt')).length}}''')
  if w<681:
   page.locator('.menu').click(); assert page.locator('#navlinks').is_visible();page.keyboard.press('Escape');assert not page.locator('#navlinks').is_visible();d['menu']=True
  page.locator('summary').filter(has_text='Quero organizar minhas dúvidas').click();page.locator('input[name=assunto]').first.check();d['questionario']='1 assunto selecionado' in page.locator('#status').inner_text()
  page.locator('#mapload').click();d['mapaIframe']=page.locator('#mapframe iframe').count()==1
  d['jsErrors']=errors;result.append(d);page.close()
 browser.close()
print(json.dumps(result,indent=2,ensure_ascii=False))
(root/'chicote'/'resultado-local.json').write_text(json.dumps(result,indent=2,ensure_ascii=False))
