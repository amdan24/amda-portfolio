# Lupen-Kopfbereich: derselbe Gartenplan zweimal gezeichnet.
#   außen = Plan (Tinte auf Weiß, lateinische Pflanzennamen)
#   innen = Praxis (gleiche Geometrie, ausgemalt, deutsche Namen)
# Wird von inhalt.py eingebunden; erzeugt festes SVG ohne JavaScript.
import math, random

W, H = 1200, 800
TINTE = "#161816"
GRUEN = ["#1D6B37", "#2E6B39", "#3E8A4F", "#6BAF88", "#8FC395"]

# (x, y, Radius, Latein, Deutsch, Grünton)
BAEUME = [
    (150, 215, 78, "Quercus robur", "Stieleiche", 1),
    (345, 165, 54, "Tilia cordata", "Winterlinde", 2),
    (545, 235, 40, "Acer campestre", "Feldahorn", 3),
    (88, 445, 40, "Corylus avellana", "Hasel", 4),
    (640, 105, 32, "Crataegus monogyna", "Weißdorn", 2),
    (1010, 555, 62, "Cornus mas", "Kornelkirsche", 3),
    (1110, 400, 36, "Sambucus nigra", "Schwarzer Holunder", 4),
]
HAUS = (800, 145, 250, 150)           # x, y, Breite, Höhe
TERRASSE = (770, 295, 310, 62)
BEETE = [(515, 345, 118, 54), (515, 415, 118, 54), (665, 380, 96, 54)]
TEICH = (300, 355, 92, 50)            # cx, cy, rx, ry
WEG = "M925 357 C 930 450, 800 500, 790 590 S 830 700, 860 760"
HOEHEN = ["M0 320 C 200 270, 400 350, 620 300 S 1000 210, 1200 270",
          "M0 400 C 220 350, 430 430, 640 380 S 1010 300, 1200 360",
          "M0 480 C 240 440, 450 510, 660 460 S 1020 390, 1200 450"]


def _krone(cx, cy, r, zufall, lappen=11):
    """Weiche, gelappte Baumkrone als Pfad."""
    pts = []
    for k in range(lappen * 2):
        a = k / (lappen * 2) * math.tau
        rr = r * (1.0 if k % 2 == 0 else 0.86) * (0.94 + zufall.random() * 0.12)
        pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(0, len(pts), 2):
        c = pts[(i + 1) % len(pts)]
        n = pts[(i + 2) % len(pts)]
        d += f" Q{c[0]:.1f} {c[1]:.1f} {n[0]:.1f} {n[1]:.1f}"
    return d + "Z"


def _rahmen():
    return "M60 95 L1140 72 L1162 690 L42 722 Z"


def plan_svg():
    s = [f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>']
    for d in HOEHEN:
        s.append(f'<path d="{d}" fill="none" stroke="{TINTE}" stroke-opacity=".16" stroke-width="1.4"/>')
    s.append(f'<path d="{_rahmen()}" fill="none" stroke="{TINTE}" stroke-width="1.6" stroke-dasharray="14 5 2 5"/>')
    # Weg
    s.append(f'<path d="{WEG}" fill="none" stroke="{TINTE}" stroke-width="30" stroke-linecap="round" stroke-opacity=".0"/>')
    s.append(f'<path d="{WEG}" fill="none" stroke="{TINTE}" stroke-width="1.6" stroke-dasharray="3 7" transform="translate(-16 0)"/>')
    s.append(f'<path d="{WEG}" fill="none" stroke="{TINTE}" stroke-width="1.6" stroke-dasharray="3 7" transform="translate(16 0)"/>')
    # Haus und Terrasse
    x, y, w, h = HAUS
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#F3F5F3" stroke="{TINTE}" stroke-width="3"/>')
    x, y, w, h = TERRASSE
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{TINTE}" stroke-width="1.6"/>')
    s.append(f'<line x1="{x}" y1="{y + h + 22}" x2="{x + w}" y2="{y + h + 22}" stroke="{TINTE}" stroke-width="1.2"/>'
             f'<line x1="{x}" y1="{y + h + 14}" x2="{x}" y2="{y + h + 30}" stroke="{TINTE}" stroke-width="1.2"/>'
             f'<line x1="{x + w}" y1="{y + h + 14}" x2="{x + w}" y2="{y + h + 30}" stroke="{TINTE}" stroke-width="1.2"/>'
             f'<text x="{x + w / 2}" y="{y + h + 18}" text-anchor="middle" font-family="Patrick Hand,cursive" font-size="19" fill="{TINTE}" stroke="#fff" stroke-width="5" paint-order="stroke">12,40 m</text>')
    # Hochbeete
    for (bx, by, bw, bh) in BEETE:
        s.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#fff" stroke="{TINTE}" stroke-width="2"/>')
    # Teich
    cx, cy, rx, ry = TEICH
    s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fff" stroke="{TINTE}" stroke-width="2"/>')
    # Bäume: Kreis mit Stammkreuz, gestrichelter Kronenrand
    for (bx, by, r, lat, _de, _f) in BAEUME:
        s.append(f'<circle cx="{bx}" cy="{by}" r="{r}" fill="#fff" fill-opacity=".92" stroke="{TINTE}" stroke-width="1.8"/>'
                 f'<circle cx="{bx}" cy="{by}" r="{r * 0.62:.1f}" fill="none" stroke="{TINTE}" stroke-width="1" stroke-dasharray="4 5"/>'
                 f'<path d="M{bx - 7} {by} H{bx + 7} M{bx} {by - 7} V{by + 7}" stroke="{TINTE}" stroke-width="1.8"/>'
                 f'<text x="{bx}" y="{by + r + 22}" text-anchor="middle" font-family="Patrick Hand,cursive" font-size="20" font-style="italic" fill="{TINTE}" stroke="#fff" stroke-width="5" paint-order="stroke">{lat}</text>')
    # Nordpfeil und Maßstab
    s.append(f'<g transform="translate(1120 640)" fill="none" stroke="{TINTE}" stroke-width="2"><circle r="26"/><path d="M0 -26 L9 14 L0 7 L-9 14Z" fill="{TINTE}"/></g>'
             f'<text x="1120" y="612" text-anchor="middle" font-family="Patrick Hand,cursive" font-size="22" fill="{TINTE}" stroke="#fff" stroke-width="5" paint-order="stroke">N</text>')
    s.append(f'<g transform="translate(930 705)" stroke="{TINTE}" stroke-width="2" fill="none"><path d="M0 0 H120 M0 -8 V8 M60 -5 V5 M120 -8 V8"/></g>'
             f'<text x="990" y="690" text-anchor="middle" font-family="Patrick Hand,cursive" font-size="19" fill="{TINTE}" stroke="#fff" stroke-width="5" paint-order="stroke">M 1:200</text>')
    s.append("</svg>")
    return "".join(s)


def praxis_svg():
    z = random.Random(7)
    s = [f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">',
         '<rect width="1200" height="800" fill="#2E6B39"/>']
    # Rasen innerhalb der Grenze
    s.append(f'<path d="{_rahmen()}" fill="#3E8A4F"/>')
    for d in HOEHEN:
        s.append(f'<path d="{d}" fill="none" stroke="#8FC395" stroke-opacity=".28" stroke-width="3"/>')
    # Ziegelweg
    s.append(f'<path d="{WEG}" fill="none" stroke="#B5573C" stroke-width="34" stroke-linecap="round"/>'
             f'<path d="{WEG}" fill="none" stroke="#D98A5F" stroke-width="30" stroke-linecap="round" stroke-dasharray="14 4"/>')
    # Terrasse und Haus
    x, y, w, h = TERRASSE
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#D98A5F"/>')
    for i in range(1, 11):
        s.append(f'<line x1="{x + i * w / 11:.1f}" y1="{y}" x2="{x + i * w / 11:.1f}" y2="{y + h}" stroke="#B5573C" stroke-width="2"/>')
    x, y, w, h = HAUS
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#F6EFE3"/>'
             f'<path d="M{x} {y} L{x + w / 2} {y + h / 2} L{x + w} {y} M{x} {y + h} L{x + w / 2} {y + h / 2} L{x + w} {y + h}" stroke="#B5573C" stroke-width="3" fill="none"/>'
             f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#B5573C" stroke-width="10"/>')
    # Hochbeete mit Pflanzen
    for (bx, by, bw, bh) in BEETE:
        s.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="3" fill="#6B4A32" stroke="#B5573C" stroke-width="8"/>')
        for i in range(5):
            px = bx + 14 + i * (bw - 28) / 4
            py = by + bh / 2 + (6 if i % 2 else -6)
            s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{10 + z.random() * 4:.1f}" fill="{GRUEN[3 + i % 2]}"/>')
        s.append(f'<circle cx="{bx + bw * 0.5:.1f}" cy="{by + bh * 0.5:.1f}" r="5" fill="#F6D44A"/>')
    # Teich
    cx, cy, rx, ry = TEICH
    s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx + 8}" ry="{ry + 8}" fill="#8FC395"/>'
             f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#6FB4C6"/>'
             f'<ellipse cx="{cx - 20}" cy="{cy - 10}" rx="26" ry="8" fill="#fff" fill-opacity=".35"/>'
             f'<circle cx="{cx + 40}" cy="{cy + 14}" r="12" fill="#3E8A4F"/><circle cx="{cx + 62}" cy="{cy + 2}" r="8" fill="#3E8A4F"/>')
    # Bäume
    for (bx, by, r, _lat, de, ton) in BAEUME:
        s.append(f'<ellipse cx="{bx + r * 0.18:.1f}" cy="{by + r * 0.26:.1f}" rx="{r:.1f}" ry="{r * 0.9:.1f}" fill="#0F3A1E" fill-opacity=".38"/>'
                 f'<path d="{_krone(bx, by, r, z)}" fill="{GRUEN[ton]}"/>'
                 f'<path d="{_krone(bx - r * 0.12, by - r * 0.14, r * 0.62, z, 8)}" fill="#fff" fill-opacity=".16"/>'
                 f'<circle cx="{bx}" cy="{by}" r="5" fill="#6B4A32"/>'
                 f'<text x="{bx}" y="{by + r + 24}" text-anchor="middle" font-family="Patrick Hand,cursive" font-size="22" fill="#fff" stroke="#0F3A1E" stroke-width="4" paint-order="stroke">{de}</text>')
    # Blumen im Rasen (kleine gelbe Tupfer)
    for (fx, fy) in [(230, 560), (260, 600), (210, 615), (380, 640), (410, 610), (330, 690), (150, 650), (610, 620), (690, 560)]:
        s.append(f'<circle cx="{fx}" cy="{fy}" r="6" fill="#F6D44A"/><circle cx="{fx}" cy="{fy}" r="2.4" fill="#fff"/>')
    # Sonne statt Nordpfeil
    s.append('<g transform="translate(1120 640)"><circle r="40" fill="#F6D44A" fill-opacity=".35"/><path transform="translate(-24 -24) scale(2)" d="M12 0C12.9 7.6 15.6 11 24 12 15.6 13 12.9 16.4 12 24 11.1 16.4 8.4 13 0 12 8.4 11 11.1 7.6 12 0Z" fill="#F6D44A"/></g>')
    s.append("</svg>")
    return "".join(s)


def hero_html():
    return f'''<section class="lupe" id="lupe" tabindex="0" aria-label="Kopfbild: derselbe Gartenplan als Zeichnung und als gelebter Garten. Mit der Maus, dem Finger oder den Pfeiltasten lässt sich eine Lupe bewegen.">
  <div class="lupe-ebene lupe-a">{plan_svg()}</div>
  <div class="lupe-ebene lupe-b" aria-hidden="true">{praxis_svg()}</div>
  <div class="lupe-ring" aria-hidden="true"></div>
  <p class="lupe-hinweis nur-js" aria-hidden="true">Fahre mit der Lupe über den Plan.<br>Gedrückt halten: große Linse.</p>
  <p class="lupe-legende" aria-hidden="true">Außen: der Plan<br>Innen: die Praxis</p>
  <div class="lupe-text">
    <p class="lupe-titel">Landschaft planen.<br>Freiräume gestalten.</p>
    <p class="lupe-titel lupe-titel-b" aria-hidden="true">Zwanzig Jahre Praxis.<br>Hände in der Erde.</p>
  </div>
  <a class="knopf lupe-weiter" href="#oben">Zum Lebenslauf <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 2v11M3 9l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
</section>
'''
