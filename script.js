'use strict';
document.documentElement.classList.add('js');
const menu=document.querySelector('.menu'), nav=document.querySelector('#navlinks');
function setMenu(open){nav.classList.toggle('open',open);menu.setAttribute('aria-expanded',String(open));}
menu.addEventListener('click',()=>setMenu(menu.getAttribute('aria-expanded')!=='true'));
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){setMenu(false);menu.focus();}});
const fields=[...document.querySelectorAll('input[name="assunto"]')],status=document.querySelector('#status');
fields.forEach(el=>el.addEventListener('change',()=>{const count=fields.filter(x=>x.checked).length;status.textContent=count?`${count} ${count===1?'assunto selecionado':'assuntos selecionados'}. As escolhas não serão enviadas.`:'Nenhum assunto selecionado.';}));
