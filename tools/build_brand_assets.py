from pathlib import Path
import math,random
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parents[1]; A=root/'assets'; A.mkdir(exist_ok=True)
logo_defs='''<defs>
  <linearGradient id="ribbonA" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox"><stop stop-color="#A8E9FC"/><stop offset=".38" stop-color="#4188BB"/><stop offset="1" stop-color="#092E58"/></linearGradient>
  <linearGradient id="ribbonB" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#19558F"/><stop offset=".52" stop-color="#65CADF"/><stop offset="1" stop-color="#B3F6FF"/></linearGradient>
  <linearGradient id="orbitLine" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#58B0D1"/><stop offset=".52" stop-color="#C9F8FF"/><stop offset="1" stop-color="#4789D4"/></linearGradient>
  <radialGradient id="node"><stop stop-color="#F5FCFF"/><stop offset=".6" stop-color="#C3F3FF"/><stop offset="1" stop-color="#6CC3E8"/></radialGradient>
</defs>'''
logo_content='''<!-- One canonical Kplay orbital-ribbon mark: edit here and regenerate all size variants. -->
<path d="M 28 121 C 24 78, 50 39, 91 34 C 117 31, 143 45, 156 65 L 136 86 C 110 54, 87 59, 72 72 C 56 86, 51 113, 58 144 C 64 168, 78 180, 89 183 C 53 179, 30 158, 28 121 Z" fill="url(#ribbonA)"/>
<path d="M 66 111 C 94 115, 117 154, 149 160 C 162 163, 174 158, 184 147 C 174 174, 160 187, 141 188 C 111 183, 91 138, 66 111 Z" fill="url(#ribbonB)"/>
<path d="M 36 180 L 173 35" fill="none" stroke="url(#orbitLine)" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="172" cy="36" r="11" fill="url(#node)"/>
<circle cx="63" cy="151" r="6.3" fill="url(#node)"/>'''
# Logo viewBox, no duplicate text baked in (brand wordmark is HTML / OG artwork)
def svg_logo(bg=False):
    bgstr='<rect width="220" height="220" rx="40" fill="#071624"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220" viewBox="0 0 220 220" role="img" aria-label="Kplay orbital ribbon mark">{logo_defs}{bgstr}{logo_content}</svg>'
(A/'logo-mark.svg').write_text(svg_logo(False),encoding='utf-8')
(A/'favicon.svg').write_text(svg_logo(True),encoding='utf-8')
# Illustration: an intentionally synthetic diagram, NOT trading or performance data.
random.seed(3410)
paths=[]
for j in range(22):
    points=[]
    for i in range(0,1201,18):
        x=i
        baseline = 500-0.135*x
        y=baseline + 44*math.sin(x/122+j*.16)+j*7.2 + (5*math.cos(x/41+j*.34))
        points.append((x, y))
    d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in points)
    paths.append(f'<path d="{d}" fill="none" stroke="url(#wave)" stroke-width="{1.35 if j%3==0 else .72}" opacity="{max(.09,.55-j*.015):.3f}"/>')
nodes=[]
for row in range(17):
 for col in range(46):
    x=col*26.8+4
    y=360+row*18-0.12*x + 28*math.sin(x/104+row*.15)
    radius=0.85 if (row+col)%7 else 1.85
    opacity=.10+(col/46)*.23
    nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" fill="#77CCED" opacity="{opacity:.2f}"/>')
art=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 700" fill="none" aria-hidden="true">
<defs><linearGradient id="wave" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#0A4B82" stop-opacity=".15"/><stop offset=".5" stop-color="#2B83B9"/><stop offset="1" stop-color="#9FEBEF"/></linearGradient>
<radialGradient id="shine"><stop stop-color="#2B96BF" stop-opacity=".33"/><stop offset="1" stop-color="#081725" stop-opacity="0"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="19"/></filter></defs>
<ellipse cx="838" cy="389" rx="391" ry="235" fill="url(#shine)"/>
<path d="M0 622 L1200 450" stroke="#83BADA" stroke-opacity=".11" stroke-dasharray="3 7"/>
{''.join(paths)}
{''.join(nodes)}
<line x1="790" y1="325" x2="790" y2="500" stroke="#A1E8F2" opacity=".65"/>
<circle cx="790" cy="325" r="24" fill="#5AD6F2" opacity=".21" filter="url(#blur)"/>
<circle cx="790" cy="325" r="6" fill="#C3FBFF"/>
<circle cx="790" cy="500" r="3" fill="#75C9E5"/>
</svg>'''
(A/'data-field.svg').write_text(art,encoding='utf-8')
# compact OG 1200x630 PNG: all brand assets derive from the same vector mark
og=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#081321"/>
<circle cx="1050" cy="150" r="400" fill="#102D47" opacity=".60"/>
<g transform="translate(77 64) scale(.65)">{logo_defs}{logo_content}</g>
<text x="222" y="174" fill="#EAF6FE" font-family="Arial, sans-serif" font-size="65" letter-spacing="11" font-weight="600">KPLAY</text>
<text x="571" y="173" fill="#91AFC2" font-family="Arial, sans-serif" font-size="22" letter-spacing="8">LLC</text>
<path d="M82 235 H1115" stroke="#3C6D8F" stroke-opacity=".5"/>
<text x="82" y="340" fill="#EFF8FF" font-family="Arial, sans-serif" font-size="57" font-weight="500">Quantitative research.</text>
<text x="82" y="416" fill="#EFF8FF" font-family="Arial, sans-serif" font-size="57" font-weight="500">Proprietary trading.</text>
<text x="84" y="505" fill="#84CDE8" font-family="Arial, sans-serif" font-size="20" letter-spacing="5">INDEPENDENT · SYSTEMATIC · PRIVATE CAPITAL</text>
</svg>'''
(A/'og-image.svg').write_text(og,encoding='utf-8')
try:
 import cairosvg
 cairosvg.svg2png(bytestring=og.encode(),write_to=str(A/'og-image.png'),output_width=1200,output_height=630)
 cairosvg.svg2png(bytestring=svg_logo(True).encode(),write_to=str(A/'favicon-192.png'),output_width=192,output_height=192)
except Exception as e: print('png failed',e)
print('SVGs and PNGs created')
