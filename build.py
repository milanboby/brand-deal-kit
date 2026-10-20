import json, html, os, sys
BASE = os.environ.get("BASE_URL", "").rstrip("/")
CHECKOUT = "https://whop.com/checkout/plan_o5zILq0x5yZOP"
PRODUCT = "https://whop.com/milan-boby/first-brand-deal-kit-milan/"
OGIMG = "https://assets-2-prod.whop.com/public/uploads/2026-10-18/b811d975-fa6c-459a-a4d0-f513bc11e195/image.png"
TITLE = "Media Kit Template, UGC Rate Card & Brand Pitch Email Templates"
DESC = "Brand Deal Kit for UGC and micro creators: an editable media kit template, UGC rate card and calculator, 24 brand pitch email templates and a deal tracker. Works in Google Sheets, Docs and Canva free. $19."
FAQ = [
 ("Does it work with Google Sheets, Google Docs and Canva's free plan?", "Yes. The spreadsheets are XLSX files that import into Google Sheets (File > Import > Upload > Replace spreadsheet) with formulas and dropdowns intact. The media kit and scripts are DOCX files that open in Google Docs or Word, and a step-by-step guide shows you how to rebuild the media kit layout in Canva's free plan. Excel and LibreOffice work too."),
 ("What file formats are included?", "One ZIP download with 10 files: PDF (Start Here guide, media kit preview, rate card template, pitch scripts), DOCX (media kit template, pitch scripts), XLSX (rate calculator and rate card, deal tracker), a Markdown Canva guide and a README."),
 ("Who is this for?", "UGC creators and micro creators getting ready to pitch their first paid brand deals who want a media kit, a way to work out rates, pitch scripts and a tracker without building them from scratch. If you already have an agency or manager handling deals, you may not need it."),
 ("Does it guarantee brand deals or a certain income?", "No. It gives you templates, scripts and a pricing framework so you can pitch professionally and quickly. Replies, deals and rates depend on your content, niche, audience, outreach and each brand's budget. Nothing in the kit predicts or guarantees income."),
 ("How does the UGC rate card calculator work?", "You enter followers, average views and engagement rate, then choose a deliverable, usage rights, exclusivity and rush. It shows a suggested low–high range. Every rate and multiplier is visible and editable on a Settings tab. The defaults are starting points to adjust, not market data."),
 ("What's the licence?", "Personal use: edit and use the templates for your own creator business as much as you like. Please don't resell or redistribute the kit files."),
 ("What about refunds?", "Checkout and payments are handled by Whop, so refunds follow Whop's buyer terms. If a file won't open or something is missing, contact us through Whop and we'll fix it."),
 ("How do I get the files after buying?", "Right after checkout you get access on Whop to a lesson with the ZIP download and the Start Here PDF. Download it, open 00_Start_Here.pdf, and follow the afternoon plan."),
]
INCLUDED = [
 ("Media kit template", "Editable 2-page DOCX, a PDF layout preview, and a Canva free-plan rebuild guide. Sections for bio, niche, audience demographics, platform stats, past collabs and UGC samples, services and contact."),
 ("UGC rate card + rate calculator", "XLSX that imports into Google Sheets. Enter followers, average views, engagement rate, deliverable, usage rights, exclusivity and rush to get a suggested low–high range. All multipliers editable."),
 ("Printable rate card", "A self-filling sheet tab plus a blank PDF template."),
 ("24 brand pitch email templates & scripts", "DOCX + PDF: cold emails, follow-ups, Instagram & TikTok DMs, UGC pitches, rate-quote replies, negotiation and counter-offers, deal recap, invoice and payment reminders, plus a subject-line bank."),
 ("Brand deal tracker", "XLSX with pipeline stages, dropdowns, automatic follow-up dates, payment tracking and a summary tab."),
 ("Start Here guide", "A 4-hour afternoon plan plus import steps for Google Sheets and Docs."),
]
BENEFITS = ["Send brands a professional media kit instead of starting from a blank page",
 "Quote with a clear UGC rate card and calculator, with every number visible",
 "Pitch faster with fill-in-the-blank brand pitch email and DM templates",
 "Track every brand deal, follow-up and invoice in one place"]
SHOTS = [("media-kit-template","Two-page media kit template preview with bio, platform stats, audience and services sections","Media kit template"),
 ("ugc-rate-card-calculator","UGC rate calculator spreadsheet with example numbers and a printable rate card tab","UGC rate card & calculator"),
 ("brand-pitch-email-templates","Pitch and negotiation scripts document showing cold email templates","Brand pitch email templates"),
 ("brand-deal-tracker","Deal tracker spreadsheet with pipeline stages, follow-up dates and summary tab","Brand deal tracker")]
e = html.escape
product_ld = {"@context":"https://schema.org","@type":"Product","name":"Brand Deal Kit: Media Kit Template, UGC Rate Card & Pitch Email Scripts",
 "description":DESC,"image":[OGIMG],"brand":{"@type":"Brand","name":"Milan Boby"},"category":"Digital templates",
 "offers":{"@type":"Offer","price":"19.00","priceCurrency":"USD","availability":"https://schema.org/InStock","url":CHECKOUT}}
faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
canon = f'<link rel="canonical" href="{BASE}/">\n<meta property="og:url" content="{BASE}/">' if BASE else ""
def pic(k, alt, eager=False):
    return (f'<img src="img/{k}.webp" srcset="img/{k}-640.webp 640w, img/{k}.webp 1280w" sizes="(max-width: 720px) 100vw, 640px" '
            f'width="1280" height="720" alt="{e(alt)}" {"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async">')
cta = f'<a class="btn" href="{CHECKOUT}">Get the kit for $19</a>'
page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
{canon}
<meta property="og:type" content="product">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:image" content="{OGIMG}">
<meta property="og:image:width" content="1920"><meta property="og:image:height" content="1080">
<meta property="og:image:alt" content="Brand Deal Kit cover: media kit, rate calculator, pitch scripts, deal tracker">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(TITLE)}">
<meta name="twitter:description" content="{e(DESC)}">
<meta name="twitter:image" content="{OGIMG}">
<link rel="icon" href="img/favicon.png" type="image/png">
<meta name="theme-color" content="#1F1B2E">
<link rel="preload" href="fonts/inter-latin.woff" as="font" type="font/woff" crossorigin>
<style>
@font-face{{font-family:Inter;src:url(fonts/inter-latin.woff) format("woff");font-weight:100 900;font-display:swap}}
:root{{--ink:#1F1B2E;--acc:#C7381A;--acc2:#FF5A36;--soft:#FFF1EC;--mut:#5C5970}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);line-height:1.6;font-size:17px;background:#fff}}
a{{color:var(--acc)}}img{{max-width:100%;height:auto;display:block;border-radius:12px}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 20px}}
.skip{{position:absolute;left:-999px}}.skip:focus{{left:12px;top:12px;background:#fff;padding:8px;z-index:9}}
.promo{{background:var(--acc2);color:#1F1B2E;text-align:center;padding:10px 16px;font-weight:700;font-size:15px}}
.promo code{{background:#fff;padding:2px 8px;border-radius:6px;font-size:15px}}
header.hero{{background:var(--ink);color:#fff;padding:56px 0 64px}}
.hero .grid{{display:grid;grid-template-columns:1.05fr 1fr;gap:40px;align-items:center}}
.eyebrow{{display:inline-block;background:var(--acc2);color:#1F1B2E;font-weight:800;font-size:13px;letter-spacing:.08em;padding:5px 12px;border-radius:99px}}
h1{{font-size:clamp(30px,4.4vw,46px);line-height:1.12;margin:16px 0 14px;letter-spacing:-.02em}}
.hero p{{color:#E2DFEE;font-size:18px;margin:0 0 24px}}
.btn{{display:inline-block;background:var(--acc2);color:#1F1B2E;font-weight:800;text-decoration:none;padding:14px 24px;border-radius:10px;font-size:17px}}
.btn:hover,.btn:focus-visible{{background:#ff7a5c}}a:focus-visible,.btn:focus-visible{{outline:3px solid #FFD27A;outline-offset:3px}}
.sec-link{{color:#fff;margin-left:16px;font-weight:600}}
.price{{margin-top:14px;color:#CFCBE0;font-size:15px}}
section{{padding:56px 0}}section.alt{{background:#F7F6FA}}
h2{{font-size:clamp(24px,3vw,32px);line-height:1.2;margin:0 0 18px;letter-spacing:-.01em}}
h3{{font-size:19px;margin:0 0 6px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px}}
.card{{background:#fff;border:1px solid #E6E4EE;border-radius:12px;padding:20px}}
.card p{{margin:0;color:var(--mut);font-size:16px}}
ul.ticks{{list-style:none;padding:0;margin:0;display:grid;gap:10px}}
ul.ticks li{{padding-left:30px;position:relative}}ul.ticks li:before{{content:"✓";position:absolute;left:0;top:0;color:var(--acc);font-weight:800}}
.shots{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:22px}}
figure{{margin:0}}figcaption{{font-weight:700;margin-top:8px}}
.plan ol{{padding-left:22px}}.plan li{{margin-bottom:6px}}
details{{border-bottom:1px solid #E6E4EE;padding:14px 0}}summary{{font-weight:700;cursor:pointer;font-size:18px}}
details p{{margin:10px 0 0;color:var(--mut)}}
.final{{background:var(--ink);color:#fff;text-align:center}}.final p{{color:#E2DFEE}}
.note{{font-size:14px;color:var(--mut)}}.final .note{{color:#CFCBE0}}
.mt24{{margin-top:24px}}.mt20{{margin-top:20px}}
footer{{padding:28px 0;font-size:14px;color:var(--mut);text-align:center}}
@media (max-width:820px){{.hero .grid{{grid-template-columns:1fr}}.sec-link{{display:inline-block;margin:14px 0 0}}}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style>
<script type="application/ld+json">{json.dumps(product_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<aside class="promo" id="promo" aria-label="Launch offer" hidden>
Launch offer: use code <code>LAUNCH20</code> at checkout for 20% off (new buyers). Ends Oct 27, 2026, 9:10 AM IST.
</aside>
<header class="hero">
 <div class="wrap grid">
  <div>
   <span class="eyebrow">FOR UGC &amp; MICRO CREATORS</span>
   <h1>Media kit template, UGC rate card &amp; brand pitch email templates in one kit</h1>
   <p>Everything you need to pitch your first paid brand deals, set up in one afternoon with free tools: Google Docs, Google Sheets, Canva free, Excel or LibreOffice.</p>
   {cta}<a class="sec-link" href="{PRODUCT}">See it on Whop</a>
   <p class="price">$19 one-time · instant ZIP download · 10 files</p>
  </div>
  <div>{pic("cover","Brand Deal Kit cover showing media kit, rate calculator, pitch scripts and deal tracker", True)}</div>
 </div>
</header>
<main id="main">
<section>
 <div class="wrap">
  <h2>Why creators use the Brand Deal Kit</h2>
  <ul class="ticks">{"".join(f"<li>{e(b)}</li>" for b in BENEFITS)}</ul>
 </div>
</section>
<section class="alt" id="included">
 <div class="wrap">
  <h2>What's included</h2>
  <div class="cards">{"".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t,d in INCLUDED)}</div>
  <p class="mt24">{pic("inside","Overview of every file in the kit: Start Here guide, media kit, rate calculator, pitch scripts and deal tracker")}</p>
 </div>
</section>
<section>
 <div class="wrap">
  <h2>A look inside the templates</h2>
  <div class="shots">{"".join(f"<figure>{pic(k,a)}<figcaption>{e(c)}</figcaption></figure>" for k,a,c in SHOTS)}</div>
  <p class="note">Screens show example numbers. Every rate and multiplier in the calculator is editable, and they're starting points, not a promise of what you'll be paid.</p>
 </div>
</section>
<section class="alt plan">
 <div class="wrap">
  <h2>Your afternoon plan</h2>
  <ol>
   <li><strong>Hour 1, media kit:</strong> fill in the media kit template with your real stats, then export a PDF.</li>
   <li><strong>Hour 2, rates:</strong> enter your numbers in the UGC rate card calculator and print your rate card.</li>
   <li><strong>Hour 3, pitch list:</strong> add 15–20 brands to the deal tracker.</li>
   <li><strong>Hour 4, pitch:</strong> personalise the brand pitch email templates and send your first pitches.</li>
  </ol>
  {cta}
 </div>
</section>
<section id="faq">
 <div class="wrap">
  <h2>Frequently asked questions</h2>
  {"".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in FAQ)}
 </div>
</section>
<section class="final">
 <div class="wrap">
  <h2>Get the Brand Deal Kit</h2>
  <p>Media kit template, UGC rate card and calculator, 24 brand pitch email templates and a deal tracker. $19, one-time.</p>
  {cta}<a class="sec-link" href="{PRODUCT}">View the product page</a>
  <p class="note mt20">Templates and a pricing framework you adjust to your niche. They don't guarantee replies, deals or income. Checkout is handled securely by Whop.</p>
 </div>
</section>
</main>
<footer><div class="wrap">© 2026 Milan Boby · Brand Deal Kit · Font: Inter (SIL Open Font License) · <a href="{PRODUCT}">Whop product page</a></div></footer>
<script>
(function(){{var end=Date.parse("2026-10-27T03:40:00Z"),b=document.getElementById("promo");if(b&&Date.now()<end)b.hidden=false;}})();
</script>
</body>
</html>
"""
open("index.html","w").write(page)
open("robots.txt","w").write("User-agent: *\nAllow: /\n" + (f"Sitemap: {BASE}/sitemap.xml\n" if BASE else ""))
if BASE:
    open("sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}/</loc><lastmod>{__import__("datetime").date.today().isoformat()}</lastmod></url></urlset>\n')
print(len(page))
