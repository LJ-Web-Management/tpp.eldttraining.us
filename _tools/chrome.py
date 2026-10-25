"""Shared page chrome (head, header, footer) for generated pages."""
import html
import json

SITE = "https://tpp.eldttraining.us"
OG_IMAGE = SITE + "/images/hero-bg.jpg"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-6QLCMH62E5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-6QLCMH62E5');
</script>"""

ORG = {
    "@type": "Organization",
    "@id": SITE + "/#organization",
    "name": "HAZWOPER OSHA Training",
    "url": SITE + "/",
    "logo": SITE + "/images/logo.webp",
    "email": "sales@hazwoper-osha.com",
    "telephone": "+1-866-429-6742",
    "sameAs": ["https://hazwoper-osha.com/"],
    "description": "HAZWOPER OSHA Training is listed on the FMCSA Training Provider Registry and delivers accredited, bilingual ELDT theory training online nationwide.",
}

CHEV = '<svg class="chev" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 4.5 6 7.5 9 4.5"/></svg>'

NAV_ITEMS = [
    ("home", "/", "Home"),
    ("program", "/partner-program.html", "ELDT Partner Program"),
    ("audience", None, "Who It&rsquo;s For"),
    ("guides", "/guides/", "Guides"),
    ("about", "/about.html", "About"),
    ("contact", "/contact.html", "Contact"),
]

AUDIENCE_LINKS = [
    ("/school-districts.html", "School Districts"),
    ("/government-agencies.html", "Government Agencies"),
    ("/guides/cdl-schools-outsource-eldt-theory.html", "CDL &amp; Driving Schools"),
    ("/guides/eldt-for-trucking-companies.html", "Trucking Companies &amp; Fleets"),
    ("/guides/eldt-for-staffing-agencies.html", "Staffing &amp; Workforce Agencies"),
    ("/guides/add-eldt-training-revenue-associations-consultants.html", "Associations &amp; Consultants"),
]


def esc(s):
    return html.escape(s, quote=True)


def nav_html(active, prefix=""):
    """prefix is "" for root-absolute links (generated pages) and keeps hrefs absolute."""
    out = []
    for key, href, label in NAV_ITEMS:
        cls = ' class="active"' if key == active else ""
        if key == "audience":
            items = "\n".join(
                f'            <li><a href="{h}">{t}</a></li>' for h, t in AUDIENCE_LINKS
            )
            cls = ' class="has-dropdown active"' if active == "audience" else ' class="has-dropdown"'
            out.append(
                f'        <li{cls}><a href="/#who-its-for">{label} {CHEV}</a>\n'
                f'          <ul class="dropdown">\n{items}\n          </ul>\n        </li>'
            )
        else:
            out.append(f'        <li{cls}><a href="{href}">{label}</a></li>')
    return "\n".join(out)


def header(active):
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a href="/" class="logo"><img src="/images/logo.webp" alt="HAZWOPER OSHA Training" class="logo-img" width="154" height="28"></a>
    <nav class="main-nav" id="mainNav">
      <ul>
{nav_html(active)}
      </ul>
    </nav>
    <div class="header-actions">
      <a href="/apply.html" class="btn btn-primary btn-sm">Become a Partner</a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>"""


FOOTER = """<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-brand">
      <a href="/" class="logo footer-logo"><img src="/images/logo.webp" alt="HAZWOPER OSHA Training" class="logo-img" width="143" height="26"></a>
      <p>ELDT theory training for CDL drivers, listed on the FMCSA Training Provider Registry. Online, bilingual, and available nationwide through our ELDT Partner Program.</p>
    </div>
    <div class="footer-col">
      <h4>Program</h4>
      <ul>
        <li><a href="/partner-program.html">ELDT Partner Program</a></li>
        <li><a href="/school-districts.html">School Districts</a></li>
        <li><a href="/government-agencies.html">Government Agencies</a></li>
        <li><a href="/guides/">ELDT Guides &amp; Articles</a></li>
        <li><a href="/about.html">About Us</a></li>
        <li><a href="/apply.html">Apply to Become a Partner</a></li>
        <li><a href="/contact.html">Contact Us</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Get in Touch</h4>
      <ul class="footer-contact">
        <li><a href="mailto:sales@hazwoper-osha.com">sales@hazwoper-osha.com</a></li>
        <li><a href="tel:+18664296742">1-866-429-6742</a></li>
        <li>Nationwide &middot; Online Training</li>
      </ul>
      <a href="/apply.html" class="btn btn-primary btn-sm">Become a Partner</a>
    </div>
  </div>
  <div class="footer-bottom container">
    <p>&copy; 2026 HAZWOPER OSHA Training. All rights reserved.</p>
    <p class="footer-disclaimer">HAZWOPER OSHA Training is the accredited provider and seller of record for all courses sold through ELDT Partner Program landing pages, and shares 50% of course revenue with its Training Partners.</p>
  </div>
</footer>

<script src="/js/main.js"></script>"""


def head(title, description, path, graph, og_type="website", extra_meta=""):
    url = SITE + path
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="HAZWOPER OSHA Training">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{OG_IMAGE}">
{extra_meta}<link rel="icon" type="image/png" href="/images/favicon-32.png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
"""
