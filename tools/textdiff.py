#!/usr/bin/env python3
"""SGP v2 — content regression: visible text of every built page at a git ref vs the current build (stdlib only).

  python3 tools/textdiff.py                 compare with HEAD
  python3 tools/textdiff.py --ref 1fea9f1   compare with another commit
  python3 tools/textdiff.py --json out.json also write the full list

Lost fragments are sorted into DROPPED (decorative microcopy removed by the plan: relative „po N d.“ statuses,
split-flap tiles, rail/stop counters, lane chart, switchboard/copy button, checklist UI, map legends now inside
assets/img/marsrutai.svg …) and REVIEW (everything else — read them; service conditions, rules, contacts and
schedule dates must never be here).
HEAD text  = text nodes of <body> outside <script>/<style>/<svg>/<noscript>/aria-hidden subtrees, split into
             block-level fragments, then into sentences.
Current    = every text node (aria-hidden included) + aria-label/alt/title/placeholder/value attributes.
A HEAD sentence is "kept" when its normalised form occurs in the normalised current page text.
"""
import json, re, subprocess, sys, os
from html.parser import HTMLParser

REF = sys.argv[sys.argv.index('--ref') + 1] if '--ref' in sys.argv else 'HEAD'
PAGES = subprocess.run(['git', 'ls-tree', '-r', '--name-only', REF], capture_output=True, text=True).stdout.split()
PAGES = [p for p in PAGES if p.endswith('.html')]
PAGES = [p for p in PAGES if not p.startswith(('v1/', 'docs/', 'src/', '_kit/'))]
BLOCK = {'p', 'div', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'td', 'th', 'dt', 'dd', 'section', 'article', 'header', 'footer',
         'nav', 'ul', 'ol', 'tr', 'table', 'figcaption', 'blockquote', 'br', 'label', 'button', 'option', 'summary', 'main', 'aside', 'a', 'span'}
SKIP = {'script', 'style', 'svg', 'noscript', 'template'}
VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'source', 'wbr', 'area', 'base', 'col', 'embed', 'param', 'track'}


class Txt(HTMLParser):
    def __init__(self, strict):
        super().__init__(convert_charrefs=True)
        self.strict, self.stack, self.parts, self.attrs = strict, [], [''], []

    def hidden(self):
        return any(t in SKIP or h for t, h in self.stack)

    def handle_starttag(self, tag, a):
        a = dict(a)
        if not self.strict:
            for k in ('aria-label', 'alt', 'title', 'placeholder', 'content', 'value', 'data-title'):
                if a.get(k):
                    self.attrs.append(a[k])
        if tag in VOID:
            if tag == 'br':
                self.parts.append('')
            return
        h = self.strict and (a.get('aria-hidden') == 'true' or 'hidden' in a and tag not in ('input',))
        self.stack.append((tag, h))
        if tag in BLOCK:
            self.parts.append('')

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
        if tag in BLOCK:
            self.parts.append('')

    def handle_data(self, d):
        if not self.hidden():
            self.parts[-1] += d


def norm(s):
    """letters and digits only, lower case: spacing, dashes, quotes and separators never count as a loss"""
    return re.sub(r'[^0-9a-ząčęėįšųūž]+', '', s.lower())


def frags(html):
    p = Txt(True)
    p.feed(html)
    out = []
    for part in p.parts:
        part = re.sub(r'\s+', ' ', part.replace(' ', ' ')).strip()
        if not part:
            continue
        for s in re.split(r'(?<=[.!?…])\s+(?=[A-ZĄČĘĖĮŠŲŪŽ„"(0-9])', part):
            s = s.strip(' ·|–—-→')
            if len(s) > 1 and re.search(r'[A-Za-zĄČĘĖĮŠŲŪŽąčęėįšųūž0-9]', s):
                out.append(s)
    return out


def flat(html):
    p = Txt(False)
    p.feed(html)
    return norm(' '.join(p.parts) + ' ' + ' '.join(p.attrs))


DROPPED = [re.compile(p, re.I) for p in (
    r'\bpo \d+ d\.', r'^\d{2} / \d{2}$', r'^/ \d+$', r'^\d{2}$', r'^\d{2}–\d{2}$', r'Kita stotelė', r'^Kitas išvykimas$', r'^Artimiausias išvykimas$',
    r'Kopijuoti', r'Pažymėti kaip paruoštą', r'^Pasiruošta$', r'^0 / 5$', r'Laiko juosta|juost', r'Kiekviena stotelė', r'^Nuo šiandien$',
    r'Maršrutų schema · ne mastelis', r'(išvykimas|atvykimas)$', r'^\d{2} · (PL|DE|BE|FR)$', r'^LT ⇄ (IE|ES)', r'^\d+ (principai|priežastys|taisyklės|žingsniai|kryptys|skyriai)$',
    r'^Pauzė$', r'^Kita$', r'^Salone$', r'^Nuotrauka$', r'Praleisti paslaugų juostą', r'^(Turinys|Dokumentas|Rezultatas|Paslauga|Informacija|Atvykimas|Pasitikėjimas)$',
    r'^Apie 3–4 paros$', r'^↑ Į pradžią$', r'Ankstesnė demo versija|Demo · nuotraukos', r'^Į (Airiją|Ispaniją)\+', r'^El\. paštas$',
    r'rugsėjo \d+ d\. · po', r'^(Ispanija|Airija|Lietuva) → (Lietuva|Airija|Ispanija) (rugsėjo|spalio|lapkričio)',
    # GS-Arrival (form + sentence) → GS-Kvietimas on pages that do not end with GS-Užklausa (plan G23/G24): the form
    # stays on /kontaktai/, the home page and the 11 service pages; the sentence stays on /kontaktai/
    r'Susisiekite su mumis ir mes pasiūlysime', r'^Gauti pasiūlymą$', r'^Jūsų vardas$', r'^Įrašykite (vardą|telefono numerį)$',
    r'^Telefono numeris$', r'^El\. pašto adresas$', r'^Patikrinkite el\. pašto adresą$', r'^Kas Jus domina\?$', r'^Pasirinkite paslaugą$',
    r'^Žinutė', r'^Formoje pateikti duomenys', r'Jūsų žinutė sėkmingai išsiųsta',
    # GS-Board (schedule list) dropped from /apie-imone/, /taisykles/, 404 (plan A11/L7/E4) — dates stay in GS-Išvykimai + GS-Artimiausi
    r'^Artimiausi pervežimai$', r'^Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu\.$',
    # table headers / labels merged into element titles; sr-only keyword sentence (kept in <title>)
    r'^Slapuko pavadinimas$', r'^Sutartis su siuntėju · PDF · 72 KB$', r'^Taisyklių 4\.2 · 4\.5 p\.$',
    r'^Tarptautiniai pervežimai: Lietuva – Airija, Lietuva – Ispanija ir atgal$')]


def main():
    res, total_lost, total = {}, 0, 0
    for page in PAGES:
        try:
            old = subprocess.run(['git', 'show', f'{REF}:{page}'], capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            continue
        if not os.path.exists(page):
            res[page] = {'missing': True}
            continue
        cur = flat(open(page, encoding='utf-8').read())
        seen, lost = set(), []
        for s in frags(old):
            n = norm(s)
            if n in seen:
                continue
            seen.add(n)
            total += 1
            if n not in cur:
                lost.append(s)
        total_lost += len(lost)
        res[page] = {'sentences': len(seen), 'lost': lost}
    if '--json' in sys.argv:
        json.dump(res, open(sys.argv[sys.argv.index('--json') + 1], 'w'), ensure_ascii=False, indent=1)
    for page, r in res.items():
        if r.get('missing'):
            print(f'!! {page}: missing in the current build')
            continue
        drop = [s for s in r['lost'] if any(p.search(s) for p in DROPPED)]
        review = [s for s in r['lost'] if s not in drop]
        print(f'{page}: {r["sentences"]} {REF} fragments · {len(drop)} dropped by plan · {len(review)} to review')
        for s in review:
            print(f'    ? {s[:150]}')
    print(f'TOTAL {total} fragments, {total_lost} not found in the current build (see DROPPED patterns + REVIEW above)')


main()
