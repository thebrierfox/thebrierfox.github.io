#!/usr/bin/env python3
"""Generate SEO-optimized city pages for COAP."""
import os

CITIES = [
    {
        "slug": "doniphan-mo",
        "name": "Doniphan, MO",
        "full": "Doniphan, Missouri",
        "pop": "1,200",
        "county": "Butler County",
        "anchor": "Rural Butler County corridor",
        "sector": "Auto Repair & Vehicle Service",
        "sector_short": "Auto Repair",
        "gap": "2 shops for 1,200 residents — zero public transit, rural geography",
        "signal": "600:1 resident-to-shop ratio (underserved)",
        "y1_low": "$260,000",
        "y1_high": "$335,000",
        "startup_low": "$60,000",
        "startup_high": "$110,000",
        "headline_stat": "2 shops for all of Butler County",
        "roi_note": "Textbook rural demand: independent vehicle dependency + no competition",
        "data_1": ("Auto Repair Shops (10km)", "2"),
        "data_2": ("Population / Shop Ratio", "600:1"),
        "data_3": ("State Unemployment", "3.4%"),
    },
    {
        "slug": "cape-girardeau-mo",
        "name": "Cape Girardeau, MO",
        "full": "Cape Girardeau, Missouri",
        "pop": "40,344",
        "county": "Cape Girardeau County",
        "anchor": "SEMO university town + regional medical hub",
        "sector": "Hair Salon / Barbershop",
        "sector_short": "Hair Salon",
        "gap": "1 salon in OSM for 40,344 residents — industry norm is 1 per 1,000–2,000",
        "signal": "40x undersupply relative to benchmark",
        "y1_low": "$241,000",
        "y1_high": "$283,000",
        "startup_low": "$28,000",
        "startup_high": "$45,000",
        "headline_stat": "1 salon for 40,344 people",
        "roi_note": "536% ROI at 6-chair booth-rental model · 11,000 SEMO students",
        "data_1": ("Median Household Income", "$55,658"),
        "data_2": ("Median Age", "34 (peak personal-care demographic)"),
        "data_3": ("Hair Salons (10km)", "1 — for 40,344 residents"),
    },
    {
        "slug": "columbia-mo",
        "name": "Columbia, MO",
        "full": "Columbia, Missouri",
        "pop": "130,913",
        "county": "Boone County",
        "anchor": "University of Missouri (30K students) + regional healthcare",
        "sector": "Modern Coin Laundry / Laundromat",
        "sector_short": "Coin Laundromat",
        "gap": "2 laundromats for 130,913 residents — national benchmark: 1 per 2,000–5,000",
        "signal": "13x–33x undersaturation",
        "y1_low": "$80,000",
        "y1_high": "$120,000",
        "startup_low": "$40,000",
        "startup_high": "$80,000",
        "headline_stat": "2 laundromats for 130,000+ residents",
        "roi_note": "30K college students without in-unit laundry = guaranteed demand",
        "data_1": ("Population", "130,913"),
        "data_2": ("Laundromats (10km)", "2 — for 130,913 residents"),
        "data_3": ("Mizzou Enrollment", "~30,000 students"),
    },
    {
        "slug": "fayetteville-ar",
        "name": "Fayetteville, AR",
        "full": "Fayetteville, Arkansas",
        "pop": "103,124",
        "county": "Washington County",
        "anchor": "University of Arkansas (28K) + NW Arkansas growth corridor",
        "sector": "Express Car Wash (subscription model)",
        "sector_short": "Express Car Wash",
        "gap": "6 car washes for 103K residents in a fast-growing Sunbelt-adjacent market",
        "signal": "High-income, high-vehicle-ownership market with thin car wash coverage",
        "y1_low": "$320,000",
        "y1_high": "$535,000",
        "startup_low": "$1,400,000",
        "startup_high": "$1,800,000",
        "headline_stat": "6 car washes for 103K high-income residents",
        "roi_note": "Year 2: $785K–$1.05M at full subscription ramp · SBA 504 eligible",
        "data_1": ("Median Household Income", "$66,237"),
        "data_2": ("Median Home Value", "$376,400"),
        "data_3": ("Population Growth 2020–2024", "+7,000 residents"),
    },
    {
        "slug": "jefferson-city-mo",
        "name": "Jefferson City, MO",
        "full": "Jefferson City, Missouri",
        "pop": "42,488",
        "county": "Cole County",
        "anchor": "Missouri state capital + state fleet + government employment",
        "sector": "Auto Repair & Vehicle Service Center",
        "sector_short": "Auto Repair",
        "gap": "1 auto repair shop for 42,488 residents — national benchmark: 17 shops expected",
        "signal": "State fleet anchor + government-stable employment base",
        "y1_low": "$40,000",
        "y1_high": "$100,000",
        "startup_low": "$35,000",
        "startup_high": "$80,000",
        "headline_stat": "1 shop vs 17 expected for a city this size",
        "roi_note": "Government employment = stable income + high vehicle ownership",
        "data_1": ("Population", "42,488"),
        "data_2": ("Auto Repair Shops (OSM)", "1 listed"),
        "data_3": ("Benchmark Expected", "17 shops"),
    },
    {
        "slug": "jonesboro-ar",
        "name": "Jonesboro, AR",
        "full": "Jonesboro, Arkansas",
        "pop": "82,386",
        "county": "Craighead County",
        "anchor": "Arkansas State University (14K) + regional medical center",
        "sector": "Modern Coin Laundry / Laundromat",
        "sector_short": "Coin Laundromat",
        "gap": "Severe laundry undersupply relative to student and renter population",
        "signal": "High renter fraction + university enrollment = structural demand",
        "y1_low": "$261,000",
        "y1_high": "$362,000",
        "startup_low": "$40,000",
        "startup_high": "$60,000",
        "headline_stat": "Highest-ROI opportunity in Jonesboro per census + OSM data",
        "roi_note": "54–98% ROI Year 2 · low startup capital, no licensed operator required",
        "data_1": ("Population", "82,386"),
        "data_2": ("Arkansas State Enrollment", "~14,000 students"),
        "data_3": ("Year 1 Revenue (base)", "$261,000–$362,000"),
    },
    {
        "slug": "joplin-mo",
        "name": "Joplin, MO",
        "full": "Joplin, Missouri",
        "pop": "52,593",
        "county": "Jasper/Newton County",
        "anchor": "4-state regional hub (MO/KS/OK/AR) + Missouri Southern State University",
        "sector": "Bar / Taproom (Multi-Revenue Model)",
        "sector_short": "Bar / Taproom",
        "gap": "Extreme bar undersupply: 10–17x below national per-capita benchmark",
        "signal": "Regional hub status + student population + I-44 highway traffic",
        "y1_low": "$480,000",
        "y1_high": "$635,000",
        "startup_low": "$275,000",
        "startup_high": "$325,000",
        "headline_stat": "10–17x below benchmark — one of Missouri's largest supply gaps",
        "roi_note": "Multi-stream: bar + food + events + live music · 4-state draw",
        "data_1": ("Population", "52,593"),
        "data_2": ("Bar Supply Gap", "10–17× below benchmark"),
        "data_3": ("Year 1 Revenue (base)", "$480,000–$635,000"),
    },
    {
        "slug": "lexington-ky",
        "name": "Lexington, KY",
        "full": "Lexington, Kentucky",
        "pop": "329,437",
        "county": "Fayette County",
        "anchor": "University of Kentucky (30K) + horse racing economy + UK HealthCare",
        "sector": "Boutique Fitness Studio",
        "sector_short": "Boutique Fitness",
        "gap": "13 gyms for 329,437 people — benchmark: 22–33 facilities expected",
        "signal": "Median age 35 + $70K HHI = peak fitness demographic with income",
        "y1_low": "$198,000",
        "y1_high": "$378,000",
        "startup_low": "$145,000",
        "startup_high": "$385,000",
        "headline_stat": "9–20 missing fitness facilities in a high-income, university market",
        "roi_note": "37–62% cash-on-cash ROI Year 3 · student + young-professional demand",
        "data_1": ("Median Household Income", "$69,989"),
        "data_2": ("Gyms (10km)", "13 — for 329,437 residents"),
        "data_3": ("UK Enrollment", "~30,000 students"),
    },
    {
        "slug": "murfreesboro-tn",
        "name": "Murfreesboro, TN",
        "full": "Murfreesboro, Tennessee",
        "pop": "157,600",
        "county": "Rutherford County",
        "anchor": "MTSU (22K students) + Amazon/logistics hub + Vanderbilt health system",
        "sector": "Modern Coin Laundry / Laundromat",
        "sector_short": "Coin Laundromat",
        "gap": "7 laundromats for 157,600 residents — 5×–7× below national benchmark",
        "signal": "Fastest-growing mid-size city in US + shift-worker employment base",
        "y1_low": "$280,000",
        "y1_high": "$375,000",
        "startup_low": "$150,000",
        "startup_high": "$300,000",
        "headline_stat": "46% population growth since 2010 — infrastructure can't keep up",
        "roi_note": "35–50% EBITDA margin stabilized · MTSU students + logistics workers",
        "data_1": ("Population", "157,600"),
        "data_2": ("Laundromats (10km)", "7 — for 157,600 residents"),
        "data_3": ("MTSU Enrollment", "~22,000 students"),
    },
    {
        "slug": "poplar-bluff-mo",
        "name": "Poplar Bluff, MO",
        "full": "Poplar Bluff, Missouri",
        "pop": "16,254",
        "county": "Butler County",
        "anchor": "Regional trade hub for SE Missouri (40K–60K trade area)",
        "sector": "Card-Operated Laundromat",
        "sector_short": "Laundromat",
        "gap": "0 laundromats in a city of 16,254 with a 20.8% poverty rate",
        "signal": "First operator captures 40,000–60,000 person regional trade area",
        "y1_low": "$220,000",
        "y1_high": "$220,000",
        "startup_low": "$157,000",
        "startup_high": "$370,000",
        "headline_stat": "Zero laundromats — essential-service gap in a regional hub",
        "roi_note": "51–64% EBITDA margin · 14–22 month payback · no competition",
        "data_1": ("Poverty Rate", "20.8% — 3,246 residents below poverty line"),
        "data_2": ("Existing Laundromats", "0"),
        "data_3": ("Regional Trade Area", "40,000–60,000 (SE Missouri)"),
    },
    {
        "slug": "rolla-mo",
        "name": "Rolla, MO",
        "full": "Rolla, Missouri",
        "pop": "20,287",
        "county": "Phelps County",
        "anchor": "Missouri S&T (7,500 students) + I-44 highway corridor",
        "sector": "Taproom / Bar",
        "sector_short": "Taproom",
        "gap": "1 bar for 20,287 residents including 7,500 university students",
        "signal": "Median age 28 — the highest-spending nightlife cohort",
        "y1_low": "$286,000",
        "y1_high": "$608,000",
        "startup_low": "$150,000",
        "startup_high": "$280,000",
        "headline_stat": "1 bar for a college town of 20,000",
        "roi_note": "Zero entrenched competition · S&T students + I-44 travelers",
        "data_1": ("Median Age", "28 (university-driven)"),
        "data_2": ("Existing Bars (10km)", "1"),
        "data_3": ("Missouri S&T Enrollment", "~7,500 students"),
    },
    {
        "slug": "springfield-mo",
        "name": "Springfield, MO",
        "full": "Springfield, Missouri",
        "pop": "170,000",
        "county": "Greene County",
        "anchor": "MSU (25K students) + CoxHealth/Mercy (20K+ medical employees) + Bass Pro HQ",
        "sector": "Boutique Dog Grooming & Pet Daycare Studio",
        "sector_short": "Dog Grooming / Pet Daycare",
        "gap": "Zero boutique pet care coverage despite high pet ownership density",
        "signal": "Student + professional population with captive pet-owning demographic",
        "y1_low": "$265,000",
        "y1_high": "$301,000",
        "startup_low": "$55,000",
        "startup_high": "$90,000",
        "headline_stat": "Zero boutique pet care in a metro of 470,000",
        "roi_note": "2×–3× underserved per capita · low startup, high repeat customer rate",
        "data_1": ("Population", "170,000 city / 470,000 metro"),
        "data_2": ("MSU Enrollment", "~25,000 students"),
        "data_3": ("Medical Employment", "20,000+ (CoxHealth + Mercy)"),
    },
    {
        "slug": "jackson-ms",
        "name": "Jackson, MS",
        "full": "Jackson, Mississippi",
        "pop": "141,376",
        "county": "Hinds County",
        "anchor": "Mississippi state capital + Hope Credit Union HQ + state employment base",
        "sector": "Modern Coin Laundry (3-site rollout)",
        "sector_short": "Coin Laundromat",
        "gap": "1 laundromat for 141,376 residents — 30–70× below national equilibrium",
        "signal": "26.3% poverty rate + $1,101 median rent = structural, inelastic demand",
        "y1_low": "$387,000",
        "y1_high": "$397,000",
        "startup_low": "$240,000",
        "startup_high": "$340,000",
        "headline_stat": "1 laundromat for 141,376 residents",
        "roi_note": "38–54% EBITDA margin · 13–23 month payback · first operator owns the market",
        "data_1": ("Poverty Rate", "26.3% — structural laundry demand floor"),
        "data_2": ("Laundromats (10km)", "1 — for 141,376 residents"),
        "data_3": ("Composite Opportunity Score", "45/50 — highest in pipeline"),
    },
]

PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} Business Opportunity Analysis | COAP</title>
<meta name="description" content="{meta_desc}">
<meta property="og:title" content="{name}: {sector_short} — {y1_low} Year 1 Projection">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://thebrierfox.github.io/coap/cities/{slug}/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="https://thebrierfox.github.io/coap/cities/{slug}/">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ font-size: 18px; }}
  body {{
    font-family: Georgia, 'Times New Roman', serif;
    background: #fff;
    color: #1a1a1a;
    line-height: 1.75;
    padding: 60px 24px 80px;
  }}
  .wrap {{ max-width: 600px; margin: 0 auto; }}
  .breadcrumb {{
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 32px;
  }}
  .breadcrumb a {{ color: #888; text-decoration: none; }}
  .breadcrumb a:hover {{ color: #333; }}
  h1 {{
    font-size: 2rem;
    font-weight: normal;
    line-height: 1.25;
    margin-bottom: 16px;
  }}
  .sector-badge {{
    display: inline-block;
    background: #f0f0f0;
    color: #333;
    font-family: 'Courier New', monospace;
    font-size: 0.78rem;
    padding: 4px 10px;
    border-radius: 3px;
    margin-bottom: 20px;
  }}
  .sub {{
    font-size: 1rem;
    color: #555;
    margin-bottom: 40px;
    border-left: 2px solid #e0e0e0;
    padding-left: 18px;
  }}
  .finding-box {{
    background: #f8f8f8;
    border-left: 3px solid #1a1a1a;
    padding: 20px 24px;
    margin: 32px 0;
  }}
  .finding-box .label {{
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 8px;
  }}
  .finding-box .headline {{
    font-size: 1.1rem;
    font-weight: bold;
    color: #1a1a1a;
    margin-bottom: 8px;
  }}
  .finding-box p {{ font-size: 0.92rem; color: #444; }}
  .data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 28px 0;
    font-size: 0.88rem;
  }}
  .data-table th {{
    text-align: left;
    font-size: 0.7rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #aaa;
    padding-bottom: 8px;
    border-bottom: 1px solid #e8e8e8;
  }}
  .data-table td {{
    padding: 8px 0;
    border-bottom: 1px solid #f4f4f4;
    color: #333;
  }}
  .data-table td:last-child {{
    text-align: right;
    font-weight: 500;
    color: #1a1a1a;
  }}
  .revenue-block {{
    margin: 32px 0;
    padding: 20px 0;
    border-top: 1px solid #e8e8e8;
    border-bottom: 1px solid #e8e8e8;
  }}
  .revenue-label {{
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 12px;
  }}
  .revenue-range {{
    font-size: 1.8rem;
    font-weight: bold;
    color: #1a1a1a;
    margin-bottom: 6px;
  }}
  .revenue-note {{
    font-size: 0.85rem;
    color: #666;
  }}
  .cta-section {{
    margin-top: 48px;
    padding: 28px;
    border: 1px solid #1a1a1a;
    background: #fafafa;
  }}
  .cta-label {{
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 12px;
  }}
  .cta-section h2 {{
    font-size: 1.2rem;
    font-weight: normal;
    margin-bottom: 12px;
  }}
  .cta-section p {{
    font-size: 0.88rem;
    color: #555;
    margin-bottom: 20px;
  }}
  .cta-btn {{
    display: inline-block;
    background: #1a1a1a;
    color: #fff;
    font-family: Georgia, serif;
    font-size: 0.9rem;
    padding: 14px 28px;
    text-decoration: none;
    letter-spacing: 0.02em;
  }}
  .cta-btn:hover {{ background: #333; }}
  .back-link {{
    margin-top: 40px;
    font-size: 0.85rem;
  }}
  .back-link a {{ color: #888; text-decoration: none; }}
  .back-link a:hover {{ color: #333; }}
  footer {{
    margin-top: 60px;
    padding-top: 24px;
    border-top: 1px solid #e8e8e8;
    font-size: 0.75rem;
    color: #aaa;
  }}
</style>
</head>
<body>
<div class="wrap">

  <p class="breadcrumb">
    <a href="/coap/">COAP</a> &rsaquo; {name}
  </p>

  <h1>{full}: Market Opportunity Analysis</h1>
  <div class="sector-badge">Top Sector: {sector_short}</div>

  <p class="sub">
    {pop} residents · {county} · {anchor}
  </p>

  <div class="finding-box">
    <p class="label">Pipeline Finding</p>
    <p class="headline">{headline_stat}</p>
    <p>{gap}</p>
  </div>

  <table class="data-table">
    <tr><th>Market Signal</th><th>Value</th></tr>
    <tr><td>{data_1_label}</td><td>{data_1_val}</td></tr>
    <tr><td>{data_2_label}</td><td>{data_2_val}</td></tr>
    <tr><td>{data_3_label}</td><td>{data_3_val}</td></tr>
  </table>

  <div class="revenue-block">
    <p class="revenue-label">Year 1 Revenue Projection</p>
    <p class="revenue-range">{y1_low} – {y1_high}</p>
    <p class="revenue-note">{roi_note}</p>
  </div>

  <div class="cta-section">
    <p class="cta-label">Get Your City's Report</p>
    <h2>This is a sample. Your city, your sector, your numbers.</h2>
    <p>
      The pipeline ran on {name} and found the {sector_short} opportunity above.
      It can run on any U.S. city. Enter your city, get a full report:
      Census demographics, BLS labor data, OSM business density,
      ranked sectors, Year 1 revenue projection, startup capital estimate,
      and a 90-day action plan. Delivered to your inbox.
    </p>
    <a href="/coap/#order" class="cta-btn">Order Your City Analysis — $49</a>
  </div>

  <p class="back-link">
    &larr; <a href="/coap/">Back to all sample cities</a>
  </p>

  <footer>
    Data sources: U.S. Census Bureau ACS, Bureau of Labor Statistics, OpenStreetMap.
    Analysis by Aegis / IntuiTek¹. Sample report — illustrative of full COAP deliverable.
  </footer>

</div>
</body>
</html>
"""

def make_page(city):
    meta_desc = (
        f"{city['full']} business opportunity analysis. "
        f"Top sector: {city['sector_short']} — {city['y1_low']}–{city['y1_high']} Year 1 projection. "
        f"{city['headline_stat']}. Full market report from $49."
    )
    html = PAGE_TEMPLATE.format(
        slug=city["slug"],
        name=city["name"],
        full=city["full"],
        pop=city["pop"],
        county=city["county"],
        anchor=city["anchor"],
        sector=city["sector"],
        sector_short=city["sector_short"],
        gap=city["gap"],
        signal=city["signal"],
        y1_low=city["y1_low"],
        y1_high=city["y1_high"],
        startup_low=city["startup_low"],
        startup_high=city["startup_high"],
        headline_stat=city["headline_stat"],
        roi_note=city["roi_note"],
        data_1_label=city["data_1"][0],
        data_1_val=city["data_1"][1],
        data_2_label=city["data_2"][0],
        data_2_val=city["data_2"][1],
        data_3_label=city["data_3"][0],
        data_3_val=city["data_3"][1],
        meta_desc=meta_desc,
    )
    return html


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    for city in CITIES:
        city_dir = os.path.join(out_dir, city["slug"])
        os.makedirs(city_dir, exist_ok=True)
        page_path = os.path.join(city_dir, "index.html")
        with open(page_path, "w") as f:
            f.write(make_page(city))
        print(f"  ✓ {city['name']} → cities/{city['slug']}/index.html")
    print(f"\nGenerated {len(CITIES)} city pages.")
