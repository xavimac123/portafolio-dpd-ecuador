/* MSCDoc: exportación de informes a Word (.docx) y a PDF (impresión), sin dependencias.
   Fuente única: scripts/exportar.js. La incrustan app-pd/build_pwa.py (app) y scripts/barra_contexto.py (herramientas).
   - MSCDoc.firma(html): deja espacio para firma y sello (ALTO_FIRMA_CM) sobre cada línea de firma.
   - MSCDoc.docx(html, nombre): descarga un .docx real (WordprocessingML) con títulos, párrafos, listas y tablas.
   - MSCDoc.pdf(html, titulo): abre el diálogo de impresión con formato A4; allí se elige «Guardar como PDF».
   - MSCDoc.usd(n): formato de moneda «USD $ 1.234,56». */
(function(W){
"use strict";
var ALTO_FIRMA_CM=6; /* tres a cuatro dedos para firma y sello físicos */
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function usd(n,sinCero){n=Number(n);if(!isFinite(n))return '';if(sinCero&&!n)return '';var neg=n<0;n=Math.abs(n);var p=n.toFixed(2).split('.');return (neg?'−':'')+'USD $ '+p[0].replace(/\B(?=(\d{3})+(?!\d))/g,'.')+','+p[1]}

/* ---------- firma y sello ---------- */
var RE_LINEA=/^\s*Firma(?:\s+y\s+sello)?\s*:?\s*_{4,}\s*$/i;
function firma(html){var d=new DOMParser().parseFromString('<div id="r">'+html+'</div>','text/html'),r=d.getElementById('r');
 [].slice.call(r.querySelectorAll('td,th')).forEach(function(c){if(RE_LINEA.test(c.textContent)){c.setAttribute('data-firma','1');c.setAttribute('style','height:'+ALTO_FIRMA_CM+'cm;vertical-align:bottom');c.textContent='Firma y sello: ______________________'}});
 [].slice.call(r.querySelectorAll('tr')).forEach(function(t){if(t.querySelector('[data-firma]'))t.setAttribute('data-firma','1')});
 return r.innerHTML}
/* bloque de firma estándar: una o dos columnas [nombre, línea 2, línea 3] */
function bloqueFirma(cols,fecha){cols=cols.filter(Boolean);var w=Math.floor(100/cols.length);
 return '<p><b>FIRMA DE RESPONSABILIDAD</b></p><table border="1" cellpadding="5" style="border-collapse:collapse;width:100%;font-size:10pt"><tr>'+cols.map(function(c){return '<th style="width:'+w+'%;text-align:left;background:#EFEBDD">'+esc(c.rol)+'</th>'}).join('')+'</tr><tr data-firma="1">'+cols.map(function(){return '<td data-firma="1" style="height:'+ALTO_FIRMA_CM+'cm;vertical-align:bottom">Firma y sello: ______________________</td>'}).join('')+'</tr>'+
 [0,1,2].map(function(i){return cols.some(function(c){return c.l[i]})?'<tr>'+cols.map(function(c){return '<td>'+esc(c.l[i]||'')+'</td>'}).join('')+'</tr>':''}).join('')+'</table>'+(fecha?'<p>Fecha: '+esc(fecha)+'</p>':'')}

/* ---------- ZIP sin compresión ---------- */
var CRC=(function(){var t=[],c,n,k;for(n=0;n<256;n++){c=n;for(k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0}return t})();
function crc32(u){var c=0xFFFFFFFF;for(var i=0;i<u.length;i++)c=CRC[(c^u[i])&255]^(c>>>8);return (c^0xFFFFFFFF)>>>0}
function zip(files){var TE=new TextEncoder(),parts=[],cen=[],off=0;
 function hdr(n){return new DataView(new ArrayBuffer(n))}
 files.forEach(function(f){var nm=TE.encode(f[0]),dat=typeof f[1]==='string'?TE.encode(f[1]):f[1],crc=crc32(dat);
  var h=hdr(30);h.setUint32(0,0x04034b50,true);h.setUint16(4,20,true);h.setUint16(6,0x0800,true);h.setUint16(8,0,true);h.setUint16(10,0,true);h.setUint16(12,0x21,true);h.setUint32(14,crc,true);h.setUint32(18,dat.length,true);h.setUint32(22,dat.length,true);h.setUint16(26,nm.length,true);h.setUint16(28,0,true);
  parts.push(new Uint8Array(h.buffer),nm,dat);
  var c=hdr(46);c.setUint32(0,0x02014b50,true);c.setUint16(4,20,true);c.setUint16(6,20,true);c.setUint16(8,0x0800,true);c.setUint16(10,0,true);c.setUint16(12,0,true);c.setUint16(14,0x21,true);c.setUint32(16,crc,true);c.setUint32(20,dat.length,true);c.setUint32(24,dat.length,true);c.setUint16(28,nm.length,true);c.setUint32(42,off,true);
  cen.push(new Uint8Array(c.buffer),nm);off+=30+nm.length+dat.length});
 var cs=cen.reduce(function(s,x){return s+x.length},0),e=hdr(22);e.setUint32(0,0x06054b50,true);e.setUint16(8,files.length,true);e.setUint16(10,files.length,true);e.setUint32(12,cs,true);e.setUint32(16,off,true);
 return new Blob(parts.concat(cen,[new Uint8Array(e.buffer)]),{type:'application/vnd.openxmlformats-officedocument.wordprocessingml.document'})}

/* ---------- HTML (subconjunto) a WordprocessingML ---------- */
function x(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function run(t,f){if(t==='\n')return '<w:r><w:br/></w:r>';var p='';if(f.b)p+='<w:b/>';if(f.i)p+='<w:i/>';if(f.u)p+='<w:u w:val="single"/>';if(f.c)p+='<w:color w:val="'+f.c+'"/>';if(f.sz)p+='<w:sz w:val="'+f.sz+'"/><w:szCs w:val="'+f.sz+'"/>';
 return '<w:r>'+(p?'<w:rPr>'+p+'</w:rPr>':'')+'<w:t xml:space="preserve">'+x(t)+'</w:t></w:r>'}
function inl(n,f,out){for(var c=n.firstChild;c;c=c.nextSibling){
  if(c.nodeType===3){var t=c.nodeValue.replace(/\s+/g,' ');if(t)out.push(run(t,f))}
  else if(c.nodeType===1){var g=c.tagName.toLowerCase(),h={b:f.b,i:f.i,u:f.u,c:f.c,sz:f.sz};
   if(g==='br'){out.push(run('\n',f));continue}if(g==='style'||g==='script'||g==='button'||g==='input'||g==='select'||g==='textarea')continue;
   if(g==='b'||g==='strong'||g==='th')h.b=1;if(g==='i'||g==='em')h.i=1;if(g==='u')h.u=1;if(g==='small')h.sz=17;
   inl(c,h,out)}}return out}
function par(runs,o){o=o||{};var p='';if(o.sp!=null||o.sb!=null)p+='<w:spacing w:before="'+(o.sb||0)+'" w:after="'+(o.sp==null?120:o.sp)+'"/>';if(o.ind)p+='<w:ind w:left="'+o.ind+'" w:hanging="'+(o.hang||0)+'"/>';if(o.keep)p+='<w:keepNext/>';if(o.al)p+='<w:jc w:val="'+o.al+'"/>';
 return '<w:p>'+(p?'<w:pPr>'+p+'</w:pPr>':'')+(runs.join('')||'')+'</w:p>'}
var BLQ={p:1,div:1,h1:1,h2:1,h3:1,h4:1,ul:1,ol:1,table:1,section:1,blockquote:1,hr:1,li:1};
function tieneBloques(n){for(var c=n.firstChild;c;c=c.nextSibling)if(c.nodeType===1&&BLQ[c.tagName.toLowerCase()])return true;return false}
function bloques(n,f,out,ctx){var pend=[];function vacia(){if(pend.length){out.push(par(pend,ctx));pend=[]}}
 for(var c=n.firstChild;c;c=c.nextSibling){
  if(c.nodeType===3){var t=c.nodeValue.replace(/\s+/g,' ');if(t.trim())pend.push(run(t,f));continue}
  if(c.nodeType!==1)continue;var g=c.tagName.toLowerCase();
  if(g==='style'||g==='script'||g==='button'||g==='input'||g==='select'||g==='textarea')continue;
  if(!BLQ[g]){if(g==='br')pend.push(run('\n',f));else{var h={b:f.b||g==='b'||g==='strong',i:f.i||g==='i'||g==='em',u:f.u||g==='u',c:f.c,sz:g==='small'?17:f.sz};inl(c,h,pend)}continue}
  vacia();
  if(g==='h1')out.push(par(inl(c,{b:1,sz:32,c:'14181E'},[]),{sb:0,sp:160,keep:1}));
  else if(g==='h2')out.push(par(inl(c,{b:1,sz:25,c:'6E6230'},[]),{sb:280,sp:120,keep:1}));
  else if(g==='h3'||g==='h4')out.push(par(inl(c,{b:1,sz:22},[]),{sb:200,sp:100,keep:1}));
  else if(g==='ul'||g==='ol'){var k=0;[].slice.call(c.children).forEach(function(li){if(li.tagName.toLowerCase()!=='li')return;k++;var r=[run((g==='ol'?k+'.':'•')+'\t',f)];inl(li,f,r);out.push('<w:p><w:pPr><w:tabs><w:tab w:val="left" w:pos="'+((ctx&&ctx.ind||0)+360)+'"/></w:tabs><w:spacing w:before="0" w:after="60"/><w:ind w:left="'+((ctx&&ctx.ind||0)+360)+'" w:hanging="360"/></w:pPr>'+r.join('')+'</w:p>')})}
  else if(g==='table')out.push(tabla(c,f));
  else if(g==='hr')out.push('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="C9BC82"/></w:pBdr></w:pPr></w:p>');
  else if(tieneBloques(c))bloques(c,f,out,ctx);
  else out.push(par(inl(c,f,[]),ctx))}
 vacia();return out}
var ANCHO=9070; /* A4 con márgenes de 2,5 cm, en vigésimos de punto */
function tabla(t,f){var rows=[].slice.call(t.querySelectorAll('tr')).filter(function(r){return r.closest('table')===t});if(!rows.length)return '';
 var nc=0;rows.forEach(function(r){var n=0;[].slice.call(r.children).forEach(function(c){n+=+c.getAttribute('colspan')||1});if(n>nc)nc=n});if(!nc)return '';
 var wc=Math.floor(ANCHO/nc),B='<w:top w:val="single" w:sz="4" w:color="8C8775"/><w:left w:val="single" w:sz="4" w:color="8C8775"/><w:bottom w:val="single" w:sz="4" w:color="8C8775"/><w:right w:val="single" w:sz="4" w:color="8C8775"/><w:insideH w:val="single" w:sz="4" w:color="8C8775"/><w:insideV w:val="single" w:sz="4" w:color="8C8775"/>';
 var s='<w:tbl><w:tblPr><w:tblW w:w="'+ANCHO+'" w:type="dxa"/><w:tblBorders>'+B+'</w:tblBorders><w:tblLayout w:type="fixed"/><w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tblGrid>';
 for(var i=0;i<nc;i++)s+='<w:gridCol w:w="'+wc+'"/>';s+='</w:tblGrid>';
 rows.forEach(function(r){var fir=r.hasAttribute('data-firma')||!!r.querySelector('[data-firma]');
  s+='<w:tr><w:trPr><w:cantSplit/>'+(fir?'<w:trHeight w:val="'+Math.round(ALTO_FIRMA_CM*567)+'" w:hRule="atLeast"/>':'')+'</w:trPr>';var usados=0;
  [].slice.call(r.children).forEach(function(c){var sp=+c.getAttribute('colspan')||1,th=c.tagName.toLowerCase()==='th',g={b:f.b||th,i:f.i,u:f.u,c:f.c,sz:19},o=[];usados+=sp;
   bloques(c,g,o,{sp:40});if(!o.length)o.push('<w:p/>');if(/<\/w:tbl>$/.test(o[o.length-1]))o.push('<w:p/>');
   s+='<w:tc><w:tcPr><w:tcW w:w="'+wc*sp+'" w:type="dxa"/>'+(sp>1?'<w:gridSpan w:val="'+sp+'"/>':'')+(th?'<w:shd w:val="clear" w:color="auto" w:fill="EFEBDD"/>':'')+(fir?'<w:vAlign w:val="bottom"/>':'')+'</w:tcPr>'+o.join('')+'</w:tc>'});
  for(;usados<nc;usados++)s+='<w:tc><w:tcPr><w:tcW w:w="'+wc+'" w:type="dxa"/></w:tcPr><w:p/></w:tc>';
  s+='</w:tr>'});
 return s+'</w:tbl><w:p><w:pPr><w:spacing w:before="0" w:after="60"/></w:pPr></w:p>'}
function aDocx(html,pie){var d=new DOMParser().parseFromString('<div id="r">'+firma(html)+'</div>','text/html'),o=[];bloques(d.getElementById('r'),{},o,null);
 var NS='xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"';
 var doc='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document '+NS+'><w:body>'+o.join('')+'<w:sectPr><w:footerReference w:type="default" r:id="rId2"/><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1418" w:header="709" w:footer="567" w:gutter="0"/></w:sectPr></w:body></w:document>';
 var sty='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles '+NS+'><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial"/><w:sz w:val="21"/><w:szCs w:val="21"/><w:lang w:val="es-EC"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style></w:styles>';
 var foot='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr '+NS+'><w:p><w:pPr><w:pBdr><w:top w:val="single" w:sz="4" w:space="4" w:color="C9BC82"/></w:pBdr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:color w:val="6E6230"/><w:sz w:val="15"/></w:rPr><w:t xml:space="preserve">'+x(pie||'Macías Sánchez Consultores · Protección de datos personales')+' · Página </w:t></w:r><w:r><w:rPr><w:color w:val="6E6230"/><w:sz w:val="15"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:rPr><w:color w:val="6E6230"/><w:sz w:val="15"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r><w:r><w:rPr><w:color w:val="6E6230"/><w:sz w:val="15"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>';
 return zip([
  ['[Content_Types].xml','<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>'],
  ['_rels/.rels','<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'],
  ['word/document.xml',doc],['word/styles.xml',sty],['word/footer1.xml',foot],
  ['word/_rels/document.xml.rels','<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>']])}

/* ---------- entrega ---------- */
function limpio(s){return String(s||'documento').normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^A-Za-z0-9 _.-]+/g,' ').trim().replace(/\s+/g,'-').slice(0,70)||'documento'}
function bajar(blob,fn){var u=URL.createObjectURL(blob),a=document.createElement('a');a.href=u;a.download=fn;document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(u)},8000)}
function docx(html,nombre,pie){var b=aDocx(html,pie),fn=limpio(nombre)+'.docx';bajar(b,fn);return fn}
var CSS='@page{size:A4;margin:2.2cm 2.2cm 2.4cm}*{box-sizing:border-box}body{font-family:Arial,Helvetica,sans-serif;font-size:10.5pt;line-height:1.4;color:#14181E;margin:0}h1{font-size:16pt;margin:0 0 8pt}h2{font-size:12.5pt;color:#6E6230;margin:16pt 0 6pt;break-after:avoid}h3,h4{font-size:11pt;margin:12pt 0 5pt;break-after:avoid}p{margin:0 0 6pt}table{border-collapse:collapse;width:100%;margin:0 0 8pt;font-size:9.5pt}th,td{border:.6pt solid #8C8775;padding:4pt 5pt;text-align:left;vertical-align:top}th{background:#EFEBDD}tr{break-inside:avoid}td[data-firma]{height:'+ALTO_FIRMA_CM+'cm;vertical-align:bottom}ul,ol{margin:0 0 6pt;padding-left:18pt}.pie{margin-top:14pt;border-top:.6pt solid #C9BC82;padding-top:5pt;font-size:8pt;color:#6E6230;text-align:center}';
function pagina(html,titulo,pie){return '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>'+esc(titulo||'Documento')+'</title><style>'+CSS+'</style></head><body>'+firma(html)+'<div class="pie">'+esc(pie||'Macías Sánchez Consultores · Protección de datos personales')+'</div></body></html>'}
function pdf(html,titulo,pie){var doc=pagina(html,limpio(titulo),pie),f=document.createElement('iframe');f.setAttribute('aria-hidden','true');f.style.cssText='position:fixed;right:0;bottom:0;width:0;height:0;border:0;visibility:hidden';
 var listo=false,imprime=function(){if(listo)return;listo=true;try{f.contentWindow.focus();f.contentWindow.print()}catch(e){var w=window.open('','_blank');if(w){w.document.write(doc);w.document.close();setTimeout(function(){try{w.print()}catch(_){}},400)}}setTimeout(function(){f.remove()},60000)};
 f.onload=function(){setTimeout(imprime,150)};f.srcdoc=doc;document.body.appendChild(f);return true}
W.MSCDoc={firma:firma,bloqueFirma:bloqueFirma,docx:docx,pdf:pdf,usd:usd,aDocx:aDocx,pagina:pagina,ALTO_FIRMA_CM:ALTO_FIRMA_CM};
})(window);
