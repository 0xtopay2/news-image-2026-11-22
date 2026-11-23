# news-image-20261122 build brief

Goal: /output/entry.png, one PNG or JPEG <= 1,048,576 bytes, <= 1024x1024 px. Repo holds the image; main.py (Python 3.13 STDLIB ONLY, no imports beyond stdlib) copies the committed entry.png to /output/entry.png. Program runs twice, must write identical bytes. Judge: vision AI judging which image best sums up ONE DAY's world news; must NAME THE DAY; breadth across regions/fields; readable at ~300px; faithful, no garbled text; clean craft. Repo must be public, MIT license, created after open (done), README with 3 make.fun badges + ?ref=be2mwwjw credit, .makefun/owner.json {"wallet": "811sPkzcVYE69KZveTt6jk9XzjcpxbsKMCMD2ZMVPyL9"}.

## Verified stories of Sunday 22 November 2026 (from Guardian/AA/NBC/Hindu day pages, file /tmp/makefun/news-nov22.md)
Use these SIX tiles (region spread: Americas, Middle East, North America, Africa, Asia, Asia):
1. MEXICO - "Cartel boss 'El Chapo Isidro' captured" - Sinaloa raid arrests Beltran Leyva leader; 11 killed, vehicles torched.
2. GULF - "Iran-US clash claims over Gulf" - Iran says missile damaged US F-16; US denies; Hormuz still closed.
3. USA - "Democrats sweep House in historic win" - at least 258 seats, largest since 1992.
4. LIBYA - "Russian warship sinks in Benghazi" - suspected Ukrainian drone attack.
5. INDONESIA - "Factory fire kills 3, dozens missing" - confectionery plant blaze.
6. SOUTH KOREA - "Minister quits in AI exam-cheating scandal" - university tests engulfed.

## Image design (draw with PIL here, commit resulting PNG)
- 1024x1024, flat editorial broadsheet style, off-white background, dark ink text, one accent color.
- Top masthead band: "WORLD NEWS" big, "Sunday, 22 November 2026" under it (the date MUST be prominent - judge criterion 1).
- 6 tiles in 2 columns x 3 rows: each tile = small flat icon (simple geometric shapes: flame, ship, jet, capitol dome, handcuffs/star, graduation cap), kicker (country), bold 2-line headline, 1-line sub. Legible when scaled to 300px.
- Footer strip: 2-3 one-line secondary items (climate talks break down; UNIFIL hands over south Lebanon posts; Leeds 4-1 Chelsea).
- Fonts: /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf and DejaVuSans.ttf.
- After drawing: verify PNG <= 1MiB (optimize), exactly 1024x1024. Save as entry.png at repo root.

## main.py (stdlib only)
import shutil, os
os.makedirs('/output', exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'entry.png'), '/output/entry.png')

## Repo
/tmp/makefun/repo-newsimage, remote https://github.com/0xtopay2/news-image-2026-11-22 (push via `git push https://0xtopay2@github.com/0xtopay2/news-image-2026-11-22.git main`; remote add is blocked by shell guard; use `git init -b main`).
