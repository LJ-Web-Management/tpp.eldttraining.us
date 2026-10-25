"""Generate /guides/index.html and one page per article in /guides/.

Run from the repo root:  python3 _tools/build_guides.py
This also rewrites sitemap.xml with every page and guide.
"""
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
from chrome import SITE, ORG, esc, head, header, FOOTER  # noqa: E402
from articles import ARTICLES, PUBLISHED  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "guides")
BY_SLUG = {a["slug"]: a for a in ARTICLES}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
CAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>'
SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'

AUDIENCE_LABELS = [
    ("all", "All Guides"),
    ("employers", "Trucking &amp; Fleets"),
    ("schools", "CDL Schools"),
    ("staffing", "Staffing &amp; Workforce"),
    ("districts", "School Districts"),
    ("government", "Government"),
    ("partners", "Partners &amp; Resellers"),
]

CTAS = {
    "partner": ("Start Selling ELDT Theory Training", "Get a hosted ELDT theory landing page with no setup cost and a 50/50 revenue split on every course sold.", "/apply.html", "Become a Partner"),
    "districts": ("In-House ELDT for Your District", "Class B and School Bus theory from $50 per seat, down to $30 at volume, with SCORM packages available.", "/school-districts.html", "See District Pricing"),
    "government": ("ELDT Theory for Your Agency", "The full ELDT theory library from $50 per seat, down to $30 at volume, with SCORM packages available.", "/government-agencies.html", "See Agency Pricing"),
}


def human_date(iso):
    d = date.fromisoformat(iso)
    return d.strftime("%B %-d, %Y")


def reading_minutes(a):
    words = len(re.sub(r"<[^>]+>", " ", a["body"] + " ".join(a["takeaways"])).split())
    return max(3, round(words / 230))


def toc_items(body):
    return re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def guide_card(a, featured=False):
    cls = "guide-card featured-guide" if featured else "guide-card"
    return f"""      <a href="/guides/{a['slug']}.html" class="{cls}" data-audience="{' '.join(a['audience'])}">
        <div class="guide-card-band"></div>
        <div class="guide-card-body">
          <div class="guide-card-meta"><span class="tag">{esc(a['category'])}</span><span>{reading_minutes(a)} min read</span></div>
          <h3>{esc(a['title'])}</h3>
          <p>{esc(a['description'])}</p>
          <span class="cat-card-link">Read the guide {ARROW}</span>
        </div>
      </a>"""


def article_page(a):
    path = f"/guides/{a['slug']}.html"
    url = SITE + path
    mins = reading_minutes(a)
    toc = toc_items(a["body"])
    faq_graph = {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}}
            for q, ans in a["faqs"]
        ],
    }
    graph = [
        ORG,
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides/"},
                {"@type": "ListItem", "position": 3, "name": a["title"]},
            ],
        },
        {
            "@type": "Article",
            "headline": a["title"],
            "description": a["description"],
            "image": SITE + "/images/hero-bg.jpg",
            "datePublished": PUBLISHED,
            "dateModified": PUBLISHED,
            "author": {"@id": SITE + "/#organization"},
            "publisher": {"@id": SITE + "/#organization"},
            "mainEntityOfPage": url,
            "articleSection": a["category"],
            "inLanguage": "en-US",
        },
        faq_graph,
    ]
    extra = (
        f'<meta property="article:published_time" content="{PUBLISHED}">\n'
        f'<meta property="article:modified_time" content="{PUBLISHED}">\n'
        f'<meta property="article:section" content="{esc(a["category"])}">\n'
    )
    takeaways = "\n".join(f"      <li>{t}</li>" for t in a["takeaways"])
    toc_html = "\n".join(f'          <li><a href="#{i}">{t}</a></li>' for i, t in toc)
    faqs = "\n".join(
        f"""      <details class="faq-item">
        <summary>{esc(q)}<span class="plus"></span></summary>
        <div class="faq-body">{esc(ans)}</div>
      </details>"""
        for q, ans in a["faqs"]
    )
    related = "\n".join(guide_card(BY_SLUG[s]) for s in a["related"])
    cta_h, cta_p, cta_href, cta_btn = CTAS[a["cta"]]

    return head(a["seo_title"], a["description"], path, graph, og_type="article", extra_meta=extra) + f"""
{header("guides")}

<div class="breadcrumb">
  <div class="container">
    <a href="/">Home</a><span class="sep">/</span><a href="/guides/">Guides</a><span class="sep">/</span><span class="current">{esc(a['category'])}</span>
  </div>
</div>

<section class="article-hero">
  <div class="container">
    <span class="eyebrow">{esc(a['category'])}</span>
    <h1>{esc(a['title'])}</h1>
    <p class="lead">{esc(a['lead'])}</p>
    <div class="article-meta">
      <span>{CAL} Updated {human_date(PUBLISHED)}</span>
      <span>{CLOCK} {mins} min read</span>
      <span>{SHIELD} By the ELDTTraining.us team at HAZWOPER OSHA Training, an FMCSA TPR-listed ELDT theory provider</span>
    </div>
  </div>
</section>

<section class="section-sm section-alt" style="padding-top:clamp(36px,5vw,56px);">
  <div class="container article-layout">
    <article class="prose">
      <div class="takeaways">
        <h2>Key Takeaways</h2>
        <ul>
{takeaways}
        </ul>
      </div>
{a['body'].strip()}

      <h2 id="faq">Frequently asked questions</h2>
      <div class="panel" style="margin-top:1em;">
{faqs}
      </div>

      <p class="article-disclaimer">This guide is for general information and reflects FMCSA ELDT requirements as of {human_date(PUBLISHED)}. Regulations and state policies change; confirm current requirements with FMCSA and your state driver licensing agency before making training or compliance decisions.</p>
    </article>
    <aside class="article-aside">
      <nav class="toc" aria-label="Table of contents">
        <h4>In This Guide</h4>
        <ol>
{toc_html}
          <li><a href="#faq">Frequently asked questions</a></li>
        </ol>
      </nav>
      <div class="aside-cta">
        <h4>{cta_h}</h4>
        <p>{cta_p}</p>
        <a href="{cta_href}" class="btn btn-primary btn-sm btn-block">{cta_btn}</a>
      </div>
    </aside>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Keep Reading</span>
      <h2>Related Guides</h2>
    </div>
    <div class="guide-grid">
{related}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-banner cta-banner-yellow">
      <div>
        <h2>{cta_h}</h2>
        <p>{cta_p}</p>
      </div>
      <a href="{cta_href}" class="btn btn-primary">{cta_btn}</a>
    </div>
  </div>
</section>

{FOOTER}
</body>
</html>
"""


def index_page():
    path = "/guides/"
    title = "ELDT Guides & Articles for Employers, Schools & Agencies | ELDTTraining.us"
    desc = "Practical guides to FMCSA Entry-Level Driver Training (ELDT) for trucking companies, CDL schools, staffing agencies, school districts, government fleets, and training partners."
    graph = [
        ORG,
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Guides"},
            ],
        },
        {
            "@type": "CollectionPage",
            "name": "ELDT Guides & Articles",
            "url": SITE + path,
            "description": desc,
            "hasPart": [
                {"@type": "Article", "headline": a["title"], "url": f"{SITE}/guides/{a['slug']}.html"}
                for a in ARTICLES
            ],
        },
    ]
    featured = [a for a in ARTICLES if a.get("featured")]
    rest = [a for a in ARTICLES if not a.get("featured")]
    cards = "\n".join([guide_card(a, featured=True) for a in featured] + [guide_card(a) for a in rest])
    filters = "\n".join(
        f'      <button class="guide-filter{" active" if k == "all" else ""}" data-filter="{k}" type="button">{label}</button>'
        for k, label in AUDIENCE_LABELS
    )
    return head(title, desc, path, graph) + f"""
{header("guides")}

<div class="breadcrumb">
  <div class="container">
    <a href="/">Home</a><span class="sep">/</span><span class="current">Guides</span>
  </div>
</div>

<section class="hero hero-photo" style="--hero-img:url('../images/heroes/hero-eldt.jpg');">
  <div class="container" style="max-width:860px;text-align:center;">
    <span class="eyebrow">ELDT Guides &amp; Articles</span>
    <h1>Everything Your Organization Needs to Know About ELDT</h1>
    <p class="lead" style="margin:0 auto;">Plain-English guides to FMCSA Entry-Level Driver Training, written for the people who hire, train, and support new CDL drivers, from fleets and CDL schools to school districts and government agencies.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>Browse by Audience</h2>
      <p>Pick the guides written for your organization, or start with the ELDT basics.</p>
    </div>
    <div class="guide-filters" role="group" aria-label="Filter guides by audience">
{filters}
    </div>
    <div class="guide-grid">
{cards}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-banner cta-banner-yellow">
      <div>
        <h2>Offer ELDT Theory Training to Your Audience</h2>
        <p>A hosted, TPR-listed ELDT theory landing page. No setup cost, and every sale splits 50/50.</p>
      </div>
      <a href="/apply.html" class="btn btn-primary">Become a Partner</a>
    </div>
  </div>
</section>

{FOOTER}
</body>
</html>
"""


def write_sitemap():
    pages = [
        ("/", "monthly", "1.0"),
        ("/partner-program.html", "monthly", "0.9"),
        ("/school-districts.html", "monthly", "0.9"),
        ("/government-agencies.html", "monthly", "0.9"),
        ("/guides/", "weekly", "0.9"),
        ("/apply.html", "monthly", "0.8"),
    ] + [(f"/guides/{a['slug']}.html", "monthly", "0.8") for a in ARTICLES] + [
        ("/about.html", "yearly", "0.6"),
        ("/contact.html", "yearly", "0.5"),
    ]
    rows = "\n".join(
        f"""  <url>
    <loc>{SITE}{p}</loc>
    <lastmod>{PUBLISHED}</lastmod>
    <changefreq>{f}</changefreq>
    <priority>{pr}</priority>
  </url>"""
        for p, f, pr in pages
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    for a in ARTICLES:
        for s in a["related"]:
            assert s in BY_SLUG, f"{a['slug']}: unknown related slug {s}"
        with open(os.path.join(OUT, a["slug"] + ".html"), "w") as fh:
            fh.write(article_page(a))
    with open(os.path.join(OUT, "index.html"), "w") as fh:
        fh.write(index_page())
    write_sitemap()
    print(f"Wrote {len(ARTICLES)} guides, guides/index.html, and sitemap.xml")


if __name__ == "__main__":
    main()
