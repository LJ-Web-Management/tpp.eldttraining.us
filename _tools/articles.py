"""Guide/article content. Each body uses <h2 id="..."> sections; the table of contents is built from them.

audience tags (used by the guides hub filter): employers, schools, districts, government, staffing, partners
cta: which landing page the article funnels to — "partner", "districts", or "government"
"""

PUBLISHED = "2026-10-25"

ARTICLES = [
# ---------------------------------------------------------------------------
{
"slug": "what-is-eldt",
"title": "What Is ELDT? FMCSA Entry-Level Driver Training Requirements Explained",
"seo_title": "What Is ELDT? FMCSA Entry-Level Driver Training Rules (2026 Guide)",
"description": "A plain-English guide to the FMCSA Entry-Level Driver Training (ELDT) rule: who needs it, what theory and behind-the-wheel training cover, the Training Provider Registry, and common exemptions.",
"category": "ELDT Basics",
"audience": ["employers", "schools", "districts", "government", "staffing", "partners"],
"cta": "partner",
"featured": True,
"lead": "Since February 7, 2022, almost every new commercial driver in the United States has had to complete federally standardized training before testing for a CDL. Here's what the ELDT rule requires, who it applies to, and what it means for the organizations that hire, train, and support CDL drivers.",
"takeaways": [
    "ELDT applies to drivers getting a Class A or Class B CDL for the first time, upgrading from Class B to Class A, or getting a Passenger (P), School Bus (S), or Hazardous Materials (H) endorsement for the first time.",
    "Training has two parts: <strong>theory</strong> (classroom or online knowledge instruction) and <strong>behind-the-wheel</strong> (range and public road). Hazmat requires theory only.",
    "Training must come from a provider listed on the FMCSA Training Provider Registry (TPR), which reports completion directly to FMCSA.",
    "Theory and behind-the-wheel can be completed with different providers, which is why many organizations outsource theory online.",
],
"body": """
<h2 id="what-eldt-is">What ELDT is</h2>
<p>ELDT stands for <strong>Entry-Level Driver Training</strong>. It is a set of federal minimum training standards created by the Federal Motor Carrier Safety Administration (FMCSA) and codified in 49 CFR Part 380, Subparts F and G. The rule took effect on <strong>February 7, 2022</strong>.</p>
<p>Before ELDT, there was no national standard for how a new commercial driver had to be trained. Some drivers attended months-long programs; others studied a state manual and took the test. ELDT closed that gap by requiring a consistent curriculum, delivered by a registered training provider, before a driver can sit for certain CDL tests.</p>

<h2 id="who-needs-eldt">Who needs ELDT training</h2>
<p>ELDT applies when a driver is obtaining one of the following for the <em>first time</em>:</p>
<ul>
<li>A <strong>Class A</strong> commercial driver's license</li>
<li>A <strong>Class B</strong> commercial driver's license</li>
<li>An <strong>upgrade from Class B to Class A</strong></li>
<li>A <strong>Passenger (P)</strong> endorsement</li>
<li>A <strong>School Bus (S)</strong> endorsement</li>
<li>A <strong>Hazardous Materials (H)</strong> endorsement (which is also part of the combined Hazmat &amp; Tank Vehicle (X) endorsement)</li>
</ul>
<p>The requirement is tied to the test, not the job. The state driver licensing agency checks the Training Provider Registry for a completed ELDT record before administering the CDL <strong>skills test</strong> (for Class A, Class B, the B-to-A upgrade, P, and S) or the <strong>knowledge test</strong> for the H endorsement.</p>

<div class="callout"><p><strong>Tanker (N) note:</strong> The federal ELDT rule does not include a separate tanker curriculum, but tank vehicle operation is part of hazmat and Class A/B knowledge, and many employers still require structured tanker training for new drivers.</p></div>

<h2 id="who-is-exempt">Who is not required to complete ELDT</h2>
<p>Several groups fall outside the requirement. Always confirm specifics with your state driver licensing agency, but in general ELDT does not apply to:</p>
<ul>
<li>Drivers who were issued a commercial learner's permit (CLP) <strong>before February 7, 2022</strong> and obtain their CDL before that CLP expires.</li>
<li>Drivers who already hold the CDL class or endorsement, including those reinstating a CDL or endorsement they previously held.</li>
<li>Drivers who are exempt from CDL requirements altogether under 49 CFR 383.3, such as certain military operators, farmers, and firefighters or emergency equipment operators in states that use that exemption.</li>
<li>Veterans who qualify for a skills test waiver under the military operator program.</li>
</ul>

<h2 id="theory-training">Part one: theory training</h2>
<p>Theory instruction is the knowledge portion of ELDT. It can be delivered in a classroom, online, or as a mix, and it covers the topics listed in the curriculum appendices of Part 380:</p>
<ul>
<li><strong>Appendix A</strong> &mdash; Class A CDL theory (basic operation, safe operating procedures, advanced operating practices, vehicle systems and reporting malfunctions, and non-driving activities like hours of service and cargo handling)</li>
<li><strong>Appendix B</strong> &mdash; Class B CDL theory</li>
<li><strong>Appendix C</strong> &mdash; Passenger (P) endorsement</li>
<li><strong>Appendix D</strong> &mdash; School Bus (S) endorsement</li>
<li><strong>Appendix E</strong> &mdash; Hazardous Materials (H) endorsement</li>
</ul>
<p>There is <strong>no minimum number of hours</strong> for theory instruction. Instead, the driver must cover every required topic and score at least <strong>80% on a written or electronic assessment</strong>. That proficiency-based structure is why well-designed online courses have become the most common way drivers complete theory.</p>

<h2 id="behind-the-wheel">Part two: behind-the-wheel training</h2>
<p>Behind-the-wheel (BTW) training is hands-on instruction on a <strong>range</strong> (a closed area away from public traffic) and on a <strong>public road</strong>. Like theory, there is no federal minimum number of hours; the instructor determines when the driver has demonstrated proficiency in every required skill.</p>
<p>The Hazardous Materials (H) endorsement has <strong>no behind-the-wheel component</strong>. It is theory only.</p>
<p>For a deeper comparison, see our guide to <a href="/guides/eldt-theory-vs-behind-the-wheel.html">ELDT theory vs. behind-the-wheel training</a>.</p>

<h2 id="training-provider-registry">The Training Provider Registry</h2>
<p>Only providers listed on the <strong>FMCSA Training Provider Registry (TPR)</strong> can deliver ELDT. Each provider self-certifies that it meets the curriculum, instructor, facility, and vehicle requirements, and FMCSA can audit and remove providers that don't.</p>
<p>When a driver completes training, the provider must submit the completion record to the TPR by midnight of the second business day. That electronic record is what the state checks before testing, so a paper certificate alone is not enough. Learn more in our <a href="/guides/fmcsa-training-provider-registry-guide.html">Training Provider Registry guide</a>.</p>

<h2 id="what-it-means-for-employers">What ELDT means for employers and training organizations</h2>
<p>For anyone who recruits, employs, or supports new CDL drivers, ELDT added a required step to every new driver's path. That creates three practical questions:</p>
<ol>
<li><strong>Who delivers theory?</strong> You can become a registered provider yourself, or use a provider that's already on the TPR.</li>
<li><strong>Who delivers behind-the-wheel?</strong> This usually requires vehicles, ranges, and qualified instructors, so it often stays with a CDL school or an in-house trainer.</li>
<li><strong>How do drivers pay, and who benefits?</strong> Theory training is a recurring purchase for every new driver, every upgrade, and every new endorsement.</li>
</ol>
<p>That last point is why organizations like CDL schools, staffing agencies, associations, and fleets are adding ELDT theory to what they offer, either to reduce their own costs or to create a new revenue stream.</p>

<div class="inline-cta"><p><strong>Offer ELDT theory without building a course.</strong> Get a hosted, TPR-listed ELDT theory landing page with no setup cost and a 50/50 revenue split.</p><a href="/partner-program.html" class="btn btn-primary btn-sm">See the Partner Program</a></div>

<h2 id="eldt-courses-available">ELDT theory courses at a glance</h2>
<div class="table-wrap"><table class="compare">
<thead><tr><th>Course</th><th>Who takes it</th><th>BTW also required?</th></tr></thead>
<tbody>
<tr><td>Class A CDL theory</td><td>First-time Class A drivers (tractor-trailers, combination vehicles)</td><td>Yes</td></tr>
<tr><td>Class B CDL theory</td><td>First-time Class B drivers (straight trucks, buses, dump trucks)</td><td>Yes</td></tr>
<tr><td>Class B to Class A upgrade</td><td>Current Class B holders moving to Class A</td><td>Yes</td></tr>
<tr><td>Passenger (P)</td><td>Bus, motorcoach, and transit drivers</td><td>Yes</td></tr>
<tr><td>School Bus (S)</td><td>School bus drivers</td><td>Yes</td></tr>
<tr><td>Hazardous Materials (H)</td><td>Drivers hauling placarded hazmat</td><td>No (theory only)</td></tr>
</tbody></table></div>
""",
"faqs": [
    ("When did the ELDT rule take effect?", "The FMCSA Entry-Level Driver Training rule took effect on February 7, 2022."),
    ("Is there a minimum number of hours for ELDT theory training?", "No. ELDT theory is proficiency-based. Drivers must cover every required topic and score at least 80% on the theory assessment, but there is no minimum number of classroom or online hours."),
    ("Can ELDT theory training be completed online?", "Yes. FMCSA allows theory instruction to be delivered online, as long as the provider is listed on the Training Provider Registry and the course covers the required curriculum and assessment."),
    ("Do drivers who already have a CDL need ELDT?", "Generally no. ELDT applies to first-time Class A or B CDLs, Class B to A upgrades, and first-time P, S, or H endorsements. Drivers who already hold the class or endorsement are not required to retake it."),
    ("Can theory and behind-the-wheel be done with different providers?", "Yes. A driver can complete theory with one registered provider and behind-the-wheel with another. Each provider reports its own portion to the Training Provider Registry."),
],
"related": ["eldt-theory-vs-behind-the-wheel", "fmcsa-training-provider-registry-guide", "how-to-become-eldt-theory-training-provider"],
},

# ---------------------------------------------------------------------------
{
"slug": "how-to-become-eldt-theory-training-provider",
"title": "How to Become an ELDT Theory Training Provider (and a Faster Alternative)",
"seo_title": "How to Become an ELDT Theory Training Provider | Steps, Costs & Alternatives",
"description": "What it takes to register as an FMCSA ELDT theory training provider: curriculum, instructors, assessments, TPR registration, and recordkeeping, plus how to offer ELDT theory without building your own program.",
"category": "Business Guides",
"audience": ["schools", "staffing", "partners", "employers"],
"cta": "partner",
"featured": False,
"lead": "Every new CDL driver needs ELDT theory, and that steady demand makes it tempting to become a registered provider. Before you commit, here's an honest look at what FMCSA requires, what it really costs to run a compliant program, and the shortcut many organizations take instead.",
"takeaways": [
    "To deliver ELDT theory you must meet the Part 380 curriculum, instructor, and assessment requirements and register each location on the FMCSA Training Provider Registry.",
    "The ongoing work, including course updates, assessments, TPR submissions within two business days, three years of records, and audit readiness, is where most of the real cost lives.",
    "Partnering with a provider that's already registered lets you offer ELDT theory through a dedicated landing page and share the revenue, without carrying the compliance burden.",
],
"body": """
<h2 id="why-organizations-consider-it">Why organizations consider becoming a provider</h2>
<p>ELDT theory is a required purchase for every first-time Class A or Class B driver, every Class B to Class A upgrade, and every first-time Passenger, School Bus, or Hazmat endorsement. If you already have a pipeline of those drivers (as a CDL school, staffing agency, carrier, association, or workforce program), capturing the theory step feels like an obvious move.</p>
<p>There are two ways to do it: register as a training provider yourself, or partner with one that is already registered. Let's look at the first path in detail.</p>

<h2 id="requirements">What FMCSA requires of a theory provider</h2>
<p>Training providers self-certify on the Training Provider Registry that they meet the standards in 49 CFR Part 380, Subpart G. For theory instruction, that means:</p>
<h3>1. A complete, compliant curriculum</h3>
<p>Your course must cover every topic in the applicable appendix: Appendix A for Class A, B for Class B, C for Passenger, D for School Bus, and E for Hazmat. That includes vehicle systems, safe operating procedures, hours of service, cargo handling, whistleblower protections, drug and alcohol rules, and more. When regulations change, your content has to change with them.</p>
<h3>2. A proficiency assessment</h3>
<p>Drivers must score at least 80% on a written or electronic theory assessment. You need a question bank that covers the full curriculum and a delivery method that protects test integrity.</p>
<h3>3. Qualified instructors</h3>
<p>Theory instructors generally must hold a CDL of the same or higher class with the applicable endorsements and have at least two years of experience driving a CMV requiring that CDL, or two years of experience as a behind-the-wheel instructor, subject to the limited exceptions in the rule. Even fully online courses need qualified instructors behind the content and available to learners.</p>
<h3>4. TPR registration and reporting</h3>
<p>Each training location registers on the TPR, attests that it meets every requirement, and keeps that registration current, including the required biennial update. After a driver completes training, the provider must submit the completion to the TPR by <strong>midnight of the second business day</strong>.</p>
<h3>5. Recordkeeping and audits</h3>
<p>Providers must retain training records for at least <strong>three years</strong> and make them available to FMCSA on request. FMCSA can audit providers and remove them from the registry for non-compliance, and it has stepped up removals of providers that can't back up their certifications.</p>

<h2 id="real-costs">The real cost of running a compliant program</h2>
<p>Registration itself doesn't carry a federal fee. The cost is everything around it:</p>
<ul>
<li><strong>Curriculum development</strong> for each course you offer, often five separate courses to cover A, B, P, S, and H.</li>
<li><strong>A learning platform</strong> that handles enrollment, progress tracking, assessments, certificates, and mobile access.</li>
<li><strong>Translation</strong> if you serve Spanish-speaking drivers, which most fleets and schools do.</li>
<li><strong>Payments, refunds, and customer support</strong> for drivers who get stuck at 9 p.m. on a Sunday.</li>
<li><strong>Staff time</strong> for TPR submissions, records retention, and audit preparation.</li>
<li><strong>Ongoing updates</strong> when FMCSA guidance or regulations change.</li>
</ul>
<p>For an organization that trains hundreds of drivers a year and wants full control, that investment can make sense. For most organizations, the math is much harder to justify.</p>

<h2 id="the-partner-alternative">The faster alternative: partner with a registered provider</h2>
<p>A partnership model lets you offer ELDT theory to your audience without becoming the provider of record. With the <a href="/partner-program.html">ELDTTraining.us ELDT Partner Program</a>, for example:</p>
<ul>
<li>You get a <strong>dedicated, hosted landing page</strong> with the full ELDT theory library: Class A, Class B, B-to-A upgrade, Hazmat, Hazmat &amp; Tank Vehicle, Tanker, Passenger, and School Bus.</li>
<li>There is <strong>no setup fee and no cost to join</strong>.</li>
<li>ELDTTraining.us stays the <strong>seller and training provider of record</strong>, handling checkout, certificates, TPR reporting, recordkeeping, and support.</li>
<li>Every course sold through your page is split <strong>50/50</strong> with you.</li>
<li>Every course includes an <strong>English/Spanish toggle</strong>.</li>
</ul>

<h2 id="side-by-side">Side-by-side comparison</h2>
<div class="table-wrap"><table class="compare">
<thead><tr><th></th><th>Become a provider</th><th>Partner Program</th></tr></thead>
<tbody>
<tr><td>Upfront cost</td><td>Curriculum, platform, translation, staff</td><td>$0</td></tr>
<tr><td>Time to launch</td><td>Months</td><td>Typically days after approval</td></tr>
<tr><td>TPR registration &amp; reporting</td><td>Your responsibility</td><td>Handled for you</td></tr>
<tr><td>Records &amp; audits</td><td>Your responsibility</td><td>Handled for you</td></tr>
<tr><td>Course updates</td><td>Your responsibility</td><td>Handled for you</td></tr>
<tr><td>Revenue</td><td>100% of sales, minus all costs</td><td>50% of every sale, no costs</td></tr>
<tr><td>Spanish version</td><td>Build it yourself</td><td>Included on every course</td></tr>
</tbody></table></div>

<h2 id="which-is-right">Which path is right for you?</h2>
<p>Becoming a provider can make sense if training is your core business, you have instructional design and compliance staff, and you want to own every detail. Partnering makes sense if your strength is your audience (drivers, members, students, or clients) and you'd rather earn on theory training than operate it.</p>
<p>Many CDL schools use both: they register as a provider for behind-the-wheel training, and partner for theory. See <a href="/guides/cdl-schools-outsource-eldt-theory.html">how CDL schools outsource ELDT theory</a>.</p>
""",
"faqs": [
    ("Does it cost money to register on the FMCSA Training Provider Registry?", "There is no federal registration fee. The costs of becoming a provider come from building and maintaining a compliant curriculum, assessments, platform, instructors, reporting, and records."),
    ("How long do ELDT training providers have to report completions?", "Providers must submit a driver's completion to the Training Provider Registry by midnight of the second business day after the driver completes training."),
    ("How long must ELDT training records be kept?", "Training providers must retain ELDT records for at least three years."),
    ("Can I sell ELDT theory training without becoming a registered provider?", "Yes, by partnering with a registered provider. In the ELDTTraining.us ELDT Partner Program, ELDTTraining.us (operated by registered provider HAZWOPER OSHA Training) remains the provider and seller of record while partners get a dedicated landing page and a 50/50 revenue split."),
],
"related": ["what-is-eldt", "fmcsa-training-provider-registry-guide", "add-eldt-training-revenue-associations-consultants"],
},

# ---------------------------------------------------------------------------
{
"slug": "eldt-requirements-school-bus-drivers",
"title": "ELDT Requirements for School Bus Drivers: A Guide for School Districts",
"seo_title": "ELDT Requirements for School Bus Drivers | Guide for School Districts",
"description": "What FMCSA ELDT means for school districts hiring bus drivers: Class B, Passenger, and School Bus endorsement training, theory vs. behind-the-wheel, in-house options, and how to cut per-driver costs.",
"category": "School Districts",
"audience": ["districts", "government"],
"cta": "districts",
"featured": False,
"lead": "Driver shortages have made every new school bus hire precious, and ELDT added a federal training step between hiring and testing. Here's what your district needs to know to keep new drivers moving from application to route as quickly as possible.",
"takeaways": [
    "Most new school bus drivers need ELDT for a Class B CDL plus the Passenger (P) and School Bus (S) endorsements, unless they already hold some of them.",
    "Each of those has a theory portion and a behind-the-wheel portion, and the theory portion can be completed online.",
    "Districts can run behind-the-wheel training in-house and use a registered online provider for theory, reducing cost and time per hire.",
],
"body": """
<h2 id="what-new-drivers-need">What new school bus drivers need</h2>
<p>A driver operating a school bus designed to carry 16 or more people (including the driver) needs a commercial driver's license, typically a <strong>Class B</strong>, along with the <strong>Passenger (P)</strong> and <strong>School Bus (S)</strong> endorsements. Under the FMCSA Entry-Level Driver Training rule, a driver getting any of those for the first time must complete ELDT for each one before taking the corresponding skills test.</p>
<p>That means a brand-new hire with only a regular driver's license typically needs:</p>
<ul>
<li><strong>Class B CDL</strong> theory and behind-the-wheel training</li>
<li><strong>Passenger (P)</strong> endorsement theory and behind-the-wheel training</li>
<li><strong>School Bus (S)</strong> endorsement theory and behind-the-wheel training</li>
</ul>
<p>A driver who already holds a Class B CDL with a P endorsement, for example a former transit driver, would only need the School Bus (S) training.</p>

<div class="callout"><p><strong>Check your state's rules too.</strong> States add their own school bus requirements on top of federal ELDT, such as pre-service hours, annual in-service training, background checks, and physical exams. ELDT is the federal floor, not the whole picture.</p></div>

<h2 id="school-bus-curriculum">What the School Bus (S) theory curriculum covers</h2>
<p>The School Bus endorsement curriculum (Appendix D of 49 CFR Part 380) focuses on the risks unique to transporting children, including:</p>
<ul>
<li>Danger zones around the bus and use of mirrors</li>
<li>Loading and unloading procedures</li>
<li>Emergency exits and evacuation procedures</li>
<li>Railroad-highway grade crossings</li>
<li>Managing student behavior</li>
<li>Antilock braking systems and special safety considerations</li>
<li>Pre- and post-trip inspections</li>
</ul>
<p>Like all ELDT theory, there's no minimum hour requirement. Drivers must complete the full curriculum and score at least 80% on the assessment.</p>

<h2 id="in-house-model">The in-house model most districts use</h2>
<p>Many districts already employ experienced trainers and own the buses needed for behind-the-wheel instruction. The challenge is usually theory: building a compliant classroom curriculum, keeping it current, scheduling sessions around new-hire start dates, and reporting completions to the Training Provider Registry.</p>
<p>A common solution is to split the work:</p>
<ol>
<li><strong>Theory online</strong> through a provider listed on the TPR. New hires can start the day they're hired, on any device, at their own pace.</li>
<li><strong>Behind-the-wheel in-house</strong> with the district's own trainers and buses, registered on the TPR for BTW.</li>
<li><strong>Skills test</strong> once both portions are reported to the TPR.</li>
</ol>
<p>Because theory and behind-the-wheel can be completed with different registered providers, this split is fully compliant and often the fastest route from hire to route.</p>

<h2 id="reducing-cost-per-driver">Reducing cost and time per driver</h2>
<p>When districts look at the true cost of a new driver, theory classroom time often stands out. Paying a trainer to deliver classroom instruction, plus paying the trainee to sit through it, adds up quickly. Online theory shifts that time to a self-paced format and frees trainers for behind-the-wheel work.</p>
<p>Other cost levers to consider:</p>
<ul>
<li><strong>Volume pricing.</strong> Buying seats in bulk across the school year usually beats buying one at a time.</li>
<li><strong>SCORM packages.</strong> If your district already runs a learning management system, a SCORM version of the course keeps completions and records in your own system.</li>
<li><strong>Bilingual courses.</strong> An English/Spanish toggle helps you recruit from a wider pool of applicants.</li>
</ul>

<div class="inline-cta"><p><strong>Built for districts:</strong> Class B, Passenger, and School Bus theory from $50 per seat, down to $30 at volume, with SCORM available.</p><a href="/school-districts.html" class="btn btn-primary btn-sm">See District Pricing</a></div>

<h2 id="choosing-a-provider">Questions to ask an online theory provider</h2>
<ul>
<li>Is the provider listed on the FMCSA Training Provider Registry, and will it report completions within two business days?</li>
<li>Does it cover every course your new hires need: Class B, Passenger, and School Bus?</li>
<li>Can drivers switch between English and Spanish?</li>
<li>Does it work on phones and tablets?</li>
<li>Can it provide a SCORM package or bulk seats for your district?</li>
<li>Who handles support when a driver gets stuck?</li>
</ul>
<p>For a broader look at verifying providers, see our <a href="/guides/fmcsa-training-provider-registry-guide.html">Training Provider Registry guide</a>.</p>
""",
"faqs": [
    ("Do school bus drivers need ELDT?", "Yes, in most cases. Drivers getting a Class B CDL, Passenger (P) endorsement, or School Bus (S) endorsement for the first time must complete ELDT for each before taking the skills test."),
    ("Can school bus drivers complete ELDT theory online?", "Yes. Theory instruction for the Class B CDL, Passenger, and School Bus endorsements can be completed online with a provider listed on the FMCSA Training Provider Registry."),
    ("Can a school district provide its own behind-the-wheel training?", "Yes. Districts with qualified trainers and vehicles can register on the Training Provider Registry to deliver behind-the-wheel training and use a separate registered provider for theory."),
    ("Does ELDT replace state school bus training requirements?", "No. ELDT is a federal minimum. States often add their own pre-service and in-service school bus driver training requirements."),
],
"related": ["what-is-eldt", "eldt-for-government-fleets", "eldt-theory-vs-behind-the-wheel"],
},

# ---------------------------------------------------------------------------
{
"slug": "eldt-for-government-fleets",
"title": "ELDT for Government Fleets: A Guide for Cities, Counties, and State Agencies",
"seo_title": "ELDT for Government Fleets | Public Works, Transit & Municipal CDL Training",
"description": "How federal, state, and local government agencies can meet FMCSA ELDT requirements for public works, transit, utility, and fleet drivers, including in-house training, exemptions, and procurement tips.",
"category": "Government",
"audience": ["government"],
"cta": "government",
"featured": False,
"lead": "Public works crews, snowplow operators, transit drivers, sanitation teams, and utility departments all depend on CDL holders. ELDT applies to public employers too, and agencies that plan for it can promote from within faster and spend less per driver.",
"takeaways": [
    "Government employees getting a first-time Class A or B CDL, a B-to-A upgrade, or a first-time P, S, or H endorsement need ELDT, the same as private-sector drivers.",
    "Some government roles fall under CDL exemptions (such as certain military and firefighting operations), so confirm which positions actually require a CDL.",
    "Agencies commonly pair online theory from a registered provider with in-house behind-the-wheel training using their own vehicles and trainers.",
],
"body": """
<h2 id="does-eldt-apply">Does ELDT apply to government employees?</h2>
<p>Yes. The FMCSA ELDT rule is tied to obtaining a CDL or endorsement, not to the type of employer. A city maintenance worker getting a Class B CDL to drive a dump truck must complete ELDT just like a driver at a private carrier.</p>
<p>Government agencies commonly need ELDT for roles like:</p>
<ul>
<li>Public works and street maintenance (dump trucks, plows, sweepers)</li>
<li>Sanitation and solid waste collection</li>
<li>Water, wastewater, and utility departments</li>
<li>Parks and recreation equipment haulers</li>
<li>Public transit and paratransit (Passenger endorsement)</li>
<li>Pupil transportation (School Bus endorsement)</li>
<li>Hazmat response and fuel delivery (Hazmat endorsement)</li>
</ul>

<h2 id="exemptions">Exemptions that may apply</h2>
<p>Some government drivers don't need a CDL at all, which means ELDT doesn't apply. Under 49 CFR 383.3, exemptions include certain <strong>military vehicle operators</strong> and, at a state's option, <strong>firefighters and operators of emergency equipment</strong>. Some states have also created limited exemptions for specific municipal operations.</p>
<p>Because exemptions vary by state and by role, confirm each position's CDL requirement with your state driver licensing agency before you budget for training.</p>

<h2 id="promote-from-within">Using ELDT to promote from within</h2>
<p>Many agencies struggle to hire experienced CDL holders at public-sector pay rates. A more reliable strategy is to train current employees, such as laborers, groundskeepers, and equipment operators, into CDL roles. ELDT makes that path more structured:</p>
<ol>
<li>The employee obtains a commercial learner's permit.</li>
<li>They complete ELDT theory online, often during slower seasons or between assignments.</li>
<li>Your in-house trainer delivers behind-the-wheel instruction on agency equipment.</li>
<li>Once both portions are on the Training Provider Registry, they take the skills test.</li>
</ol>
<p>The result is a CDL pipeline built from people who already know your agency, your equipment, and your community.</p>

<h2 id="in-house-vs-outsourced">In-house vs. outsourced theory</h2>
<p>An agency can register on the TPR and deliver its own theory instruction, but that means building and maintaining a compliant curriculum, assessments, instructor qualifications, reporting, and three years of records. Most agencies prefer to keep behind-the-wheel training in-house, where their equipment and trainers add the most value, and buy theory from a registered provider.</p>
<p>If your agency already uses a learning management system, look for a provider that offers a <strong>SCORM package</strong> so completions and records stay in your system.</p>

<div class="inline-cta"><p><strong>For agencies:</strong> the full ELDT theory library from $50 per seat, down to $30 at volume, with SCORM packages available.</p><a href="/government-agencies.html" class="btn btn-primary btn-sm">See Agency Pricing</a></div>

<h2 id="procurement-tips">Procurement tips for ELDT theory</h2>
<ul>
<li><strong>Verify TPR listing.</strong> Ask for the provider's registry listing and confirm it covers theory for each course you need.</li>
<li><strong>Cover every class and endorsement.</strong> A single contract covering Class A, Class B, B-to-A upgrade, P, S, and H avoids juggling vendors.</li>
<li><strong>Ask about per-seat volume tiers.</strong> Annual seat volume across departments can unlock lower rates.</li>
<li><strong>Require bilingual access.</strong> An English/Spanish toggle supports a broader workforce.</li>
<li><strong>Confirm reporting and support.</strong> Who reports completions, and who answers driver questions?</li>
</ul>
""",
"faqs": [
    ("Do municipal employees need ELDT to get a CDL?", "Yes. Government employees getting a first-time Class A or B CDL, a Class B to A upgrade, or a first-time Passenger, School Bus, or Hazmat endorsement must complete ELDT, unless their role is exempt from CDL requirements."),
    ("Are firefighters exempt from ELDT?", "Under 49 CFR 383.3, states may exempt firefighters and emergency equipment operators from CDL requirements. If a state uses that exemption, those drivers don't need a CDL and therefore don't need ELDT. Check your state's rules."),
    ("Can a government agency deliver its own ELDT training?", "Yes. Agencies can register on the FMCSA Training Provider Registry. Many deliver behind-the-wheel training in-house and use a registered online provider for theory."),
],
"related": ["eldt-requirements-school-bus-drivers", "what-is-eldt", "fmcsa-training-provider-registry-guide"],
},

# ---------------------------------------------------------------------------
{
"slug": "eldt-theory-vs-behind-the-wheel",
"title": "ELDT Theory vs. Behind-the-Wheel Training: What's the Difference?",
"seo_title": "ELDT Theory vs. Behind-the-Wheel Training: Key Differences Explained",
"description": "Compare the two parts of FMCSA Entry-Level Driver Training: what theory and behind-the-wheel cover, who can deliver each, how they're assessed, and why many programs split them between providers.",
"category": "ELDT Basics",
"audience": ["employers", "schools", "districts", "government", "staffing"],
"cta": "partner",
"featured": False,
"lead": "Every ELDT program has two halves: theory and behind-the-wheel. They have different requirements, different costs, and often different providers. Understanding the difference is the first step to designing a faster, cheaper training path for new drivers.",
"takeaways": [
    "Theory is knowledge instruction that can be delivered online. Behind-the-wheel is hands-on range and public road training in a real vehicle.",
    "Theory requires an 80% assessment score; behind-the-wheel proficiency is judged by the instructor. Neither has a federal minimum hour requirement.",
    "A driver can complete each portion with a different registered provider, and Hazmat (H) is theory only.",
],
"body": """
<h2 id="quick-comparison">Quick comparison</h2>
<div class="table-wrap"><table class="compare">
<thead><tr><th></th><th>Theory</th><th>Behind-the-wheel</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>Knowledge instruction on regulations, safety, and vehicle operation</td><td>Hands-on driving on a range and on public roads</td></tr>
<tr><td>Delivery</td><td>Classroom, online, or blended</td><td>In a CMV of the class being trained</td></tr>
<tr><td>Minimum hours</td><td>None</td><td>None</td></tr>
<tr><td>How proficiency is measured</td><td>80% minimum score on a written or electronic assessment</td><td>Instructor determines proficiency in every required skill</td></tr>
<tr><td>Required for</td><td>Class A, Class B, B-to-A, P, S, and H</td><td>Class A, Class B, B-to-A, P, and S (not H)</td></tr>
<tr><td>Typical cost drivers</td><td>Curriculum, platform, support</td><td>Vehicles, fuel, insurance, ranges, instructor time</td></tr>
</tbody></table></div>

<h2 id="theory-explained">Theory training explained</h2>
<p>Theory instruction covers everything a new driver needs to <em>know</em>. For a Class A CDL, that includes basic operation, safe operating procedures, advanced operating practices like hazard perception and skid control, vehicle systems and malfunction reporting, and non-driving activities such as hours of service, trip planning, cargo handling, and drug and alcohol rules.</p>
<p>Because it's knowledge-based, theory adapts well to online delivery. Drivers can work through modules at their own pace, review material before the assessment, and finish on a phone or tablet. To complete theory, a driver must score at least <strong>80%</strong> on the assessment.</p>

<h2 id="btw-explained">Behind-the-wheel training explained</h2>
<p>Behind-the-wheel training covers what a new driver needs to <em>do</em>. It has two parts:</p>
<ul>
<li><strong>Range training</strong> on a closed course: vehicle inspections, straight-line backing, offset and alley-dock backing, parallel parking, and coupling and uncoupling (for Class A).</li>
<li><strong>Public road training</strong> in real traffic: turns, lane changes, intersections, railroad crossings, curves, and highway driving.</li>
</ul>
<p>There's no minimum hour requirement. The instructor decides when the driver has demonstrated proficiency in every required element. BTW requires qualified instructors, a vehicle representative of the class being trained, and a suitable range, which is why it's typically the most expensive part of CDL training.</p>

<h2 id="why-split">Why many programs split theory and BTW</h2>
<p>FMCSA allows a driver to complete theory with one registered provider and behind-the-wheel with another. Each provider reports its own portion to the Training Provider Registry. That flexibility has led to a common model:</p>
<ul>
<li><strong>Online theory</strong> from a provider that specializes in curriculum, platform, and compliance reporting.</li>
<li><strong>Behind-the-wheel</strong> from a CDL school, carrier, district, or agency that already has trucks, buses, ranges, and instructors.</li>
</ul>
<p>The benefits are practical: drivers can start theory immediately instead of waiting for a classroom cohort, instructors spend their time in the vehicle instead of at a whiteboard, and theory costs become predictable per driver.</p>

<div class="inline-cta"><p><strong>Run behind-the-wheel? Add theory without building it.</strong> Offer the full ELDT theory library from your own dedicated page and earn 50% of every sale.</p><a href="/partner-program.html" class="btn btn-primary btn-sm">Explore the Program</a></div>

<h2 id="hazmat-exception">The Hazmat exception</h2>
<p>The Hazardous Materials (H) endorsement is the only ELDT category with <strong>no behind-the-wheel requirement</strong>. Drivers complete hazmat theory, and the state checks the TPR before administering the H knowledge test. That makes hazmat one of the simplest courses to deliver entirely online. See our <a href="/guides/hazmat-endorsement-eldt-requirements.html">Hazmat endorsement ELDT guide</a>.</p>
""",
"faqs": [
    ("Is ELDT theory training required before behind-the-wheel?", "Federal rules do not require a specific order, but both must be completed and reported to the Training Provider Registry before the CDL skills test. Many programs complete theory first so drivers arrive at behind-the-wheel training with the knowledge base in place."),
    ("Does the Hazmat endorsement require behind-the-wheel training?", "No. The Hazmat (H) endorsement requires ELDT theory only."),
    ("How many hours is ELDT behind-the-wheel training?", "There is no federal minimum. The instructor determines when the driver is proficient in each required range and public road skill."),
],
"related": ["what-is-eldt", "cdl-schools-outsource-eldt-theory", "hazmat-endorsement-eldt-requirements"],
},

# ---------------------------------------------------------------------------
{
"slug": "fmcsa-training-provider-registry-guide",
"title": "The FMCSA Training Provider Registry: How It Works and How to Verify a Provider",
"seo_title": "FMCSA Training Provider Registry (TPR) Guide: How It Works & How to Verify",
"description": "How the FMCSA Training Provider Registry works, what providers must certify, how completion records reach the state, and how employers and drivers can verify an ELDT provider before buying training.",
"category": "ELDT Basics",
"audience": ["employers", "schools", "districts", "government", "staffing", "partners"],
"cta": "partner",
"featured": False,
"lead": "If a driver's training isn't on the Training Provider Registry, as far as the state is concerned, it didn't happen. Here's how the TPR works and how to make sure the training you buy, recommend, or resell will actually count.",
"takeaways": [
    "The TPR is FMCSA's database of providers allowed to deliver ELDT, and the system that records each driver's completed training.",
    "Providers must report completions by midnight of the second business day; states check the TPR before CDL skills tests and the Hazmat knowledge test.",
    "Before buying or reselling training, confirm the provider is listed for the specific course and training type (theory or BTW).",
],
"body": """
<h2 id="what-is-the-tpr">What the Training Provider Registry is</h2>
<p>The Training Provider Registry (TPR) is an FMCSA system that does two jobs:</p>
<ol>
<li>It lists every <strong>training provider</strong> that has certified it meets the ELDT requirements in 49 CFR Part 380, Subpart G.</li>
<li>It stores <strong>driver training records</strong> submitted by those providers when a driver completes theory or behind-the-wheel training.</li>
</ol>
<p>State driver licensing agencies use those records to confirm a driver has completed ELDT before testing.</p>

<h2 id="who-registers">Who registers</h2>
<p>Any organization delivering ELDT must register, including CDL schools, community colleges, motor carriers that train their own drivers, school districts, government agencies, labor organizations, and online providers. Registration is per training location, and each listing shows which courses it offers and whether it provides theory, behind-the-wheel, or both.</p>
<p>Providers self-certify that they meet curriculum, instructor, facility, vehicle, and recordkeeping standards. FMCSA can audit providers, and it can remove providers from the registry when they can't demonstrate compliance.</p>

<h2 id="how-records-flow">How a driver's record gets to the state</h2>
<ol>
<li>The driver creates a TPR account and shares their information with the provider (or the provider enters it).</li>
<li>The driver completes training and, for theory, passes the assessment with at least 80%.</li>
<li>The provider submits the completion record to the TPR by <strong>midnight of the second business day</strong>.</li>
<li>FMCSA transmits the record to the driver's state licensing agency.</li>
<li>The state confirms the record before administering the skills test (Class A, Class B, B-to-A, P, S) or the Hazmat knowledge test.</li>
</ol>
<p>If any step breaks down, such as a provider forgetting to submit or entering the wrong license number, the driver can be turned away at the testing site.</p>

<h2 id="how-to-verify">How to verify a provider</h2>
<p>Whether you're a driver, employer, school, or reseller, take these steps before you buy:</p>
<ul>
<li><strong>Search the TPR</strong> on FMCSA's website by provider name or location.</li>
<li><strong>Check the training type.</strong> A provider listed only for behind-the-wheel can't report theory, and vice versa.</li>
<li><strong>Check the specific courses.</strong> Make sure the listing includes each class or endorsement you need.</li>
<li><strong>Ask about reporting.</strong> Confirm the provider submits completions to the TPR for you and how quickly.</li>
<li><strong>Ask who answers questions.</strong> Drivers inevitably need help with logins, assessments, or TPR records.</li>
</ul>

<div class="callout"><p><strong>Red flags:</strong> a provider that can't give you its TPR listing, offers a certificate without reporting to the TPR, guarantees a pass, or offers training that's dramatically shorter than the full curriculum.</p></div>

<h2 id="for-resellers">If you resell or recommend training</h2>
<p>Organizations that send drivers to a provider (staffing agencies, associations, consultants, or fleets) put their reputation on the line with every recommendation. A partner model where the TPR-listed provider remains the provider of record means the compliance, reporting, and recordkeeping obligations stay with the provider, while you still offer the training to your audience.</p>
<p>ELDTTraining.us is operated by HAZWOPER OSHA Training, which is listed on the FMCSA Training Provider Registry for ELDT theory (search the registry for &ldquo;HAZWOPER OSHA Training&rdquo;), and stays the provider and seller of record for every course sold through an <a href="/partner-program.html">ELDT Partner Program</a> page.</p>
""",
"faqs": [
    ("How do I check if an ELDT provider is registered?", "Search FMCSA's Training Provider Registry by provider name or location, and confirm the listing includes the training type (theory or behind-the-wheel) and the specific courses you need."),
    ("How quickly do providers report ELDT completion?", "Providers must submit completion records to the Training Provider Registry by midnight of the second business day after the driver completes training."),
    ("What happens if my training isn't in the TPR?", "The state licensing agency will not administer the CDL skills test (or the Hazmat knowledge test) until a completed ELDT record appears in the registry. Contact the provider to submit or correct the record."),
],
"related": ["what-is-eldt", "how-to-become-eldt-theory-training-provider", "eldt-for-staffing-agencies"],
},

# ---------------------------------------------------------------------------
{
"slug": "eldt-for-trucking-companies",
"title": "ELDT for Trucking Companies: Onboarding New CDL Drivers Faster",
"seo_title": "ELDT for Trucking Companies & Fleets | Faster New Driver Onboarding",
"description": "How motor carriers and private fleets can use ELDT theory training to recruit, upskill, and onboard new CDL drivers faster, including company-sponsored training, B-to-A upgrades, and endorsement add-ons.",
"category": "Employers",
"audience": ["employers"],
"cta": "partner",
"featured": False,
"lead": "For carriers and private fleets, ELDT is more than a compliance box. It's a lever for recruiting new drivers, upgrading the ones you already have, and getting everyone on the road sooner. Here's how fleets are using it.",
"takeaways": [
    "Company-sponsored CDL programs, B-to-A upgrades, and new hazmat or passenger endorsements all trigger ELDT.",
    "Moving theory online lets recruits start training the day they accept an offer, shrinking the gap between hire and first load.",
    "Fleets can offer ELDT theory to their own drivers and to their broader network, and earn revenue doing it.",
],
"body": """
<h2 id="where-eldt-shows-up">Where ELDT shows up in a fleet</h2>
<p>Even if you only hire experienced drivers, ELDT probably touches your operation more than you think:</p>
<ul>
<li><strong>Company-sponsored CDL programs</strong> that train new drivers from scratch need Class A or Class B ELDT.</li>
<li><strong>Upgrades</strong> from Class B to Class A, for example moving local straight-truck drivers into tractor-trailers, require B-to-A ELDT.</li>
<li><strong>New endorsements</strong>, such as adding hazmat to win a fuel or chemical contract, require Hazmat (H) ELDT theory.</li>
<li><strong>Yard and warehouse employees</strong> moving into driving roles need full ELDT for their first CDL.</li>
</ul>

<h2 id="speed-to-seat">Shrinking time from offer to first load</h2>
<p>Every day between a recruit accepting an offer and driving revenue miles is a day they might take another offer. Classroom theory is often a bottleneck: recruits wait for the next cohort, travel to a terminal, and sit through days of instruction.</p>
<p>Online theory changes the sequence. A recruit can start ELDT theory on their phone the evening they accept your offer, finish at their own pace, and arrive at behind-the-wheel training ready to drive. Your trainers spend their time in the truck, which is where they add the most value.</p>

<h2 id="upskilling">Upskilling your existing drivers</h2>
<p>Your best future Class A and hazmat drivers may already be on your payroll. A structured upskilling path might look like this:</p>
<ol>
<li>Identify Class B drivers or yard staff with clean records who want to move up.</li>
<li>Have them complete B-to-A or Class A theory online during downtime.</li>
<li>Pair them with an in-house trainer or CDL school for behind-the-wheel training.</li>
<li>Add the Hazmat theory course for drivers on hazmat lanes.</li>
</ol>
<p>Promoting from within improves retention and lowers recruiting costs, and drivers notice when a company invests in their careers.</p>

<h2 id="bilingual">Supporting a bilingual workforce</h2>
<p>Many fleets employ drivers and warehouse staff whose first language is Spanish. A course with an English/Spanish toggle helps them learn complex material, like hours of service and cargo securement, in the language they understand best, while still preparing for English-language road signs, inspections, and communication. See our guide to <a href="/guides/spanish-eldt-training.html">Spanish-language ELDT training</a>.</p>

<h2 id="fleet-as-partner">Turning your network into revenue</h2>
<p>Large fleets often sit at the center of a network: owner-operators, lease-purchase drivers, local partner carriers, and job applicants who don't yet qualify. All of them may need ELDT theory at some point.</p>
<p>With the <a href="/partner-program.html">ELDT Partner Program</a>, a fleet can launch a dedicated landing page offering the full ELDT theory library to its network at no setup cost. ELDTTraining.us handles checkout, certificates, TPR reporting, and support, and splits every sale 50/50 with the fleet. You can also purchase training on your drivers' behalf through the same page.</p>

<div class="inline-cta"><p><strong>Give your recruits and drivers a place to start training today.</strong> No setup cost. 50/50 revenue split.</p><a href="/apply.html" class="btn btn-primary btn-sm">Apply Now</a></div>
""",
"faqs": [
    ("Do company-sponsored CDL training programs need to follow ELDT?", "Yes. Any driver obtaining a first-time Class A or B CDL must complete ELDT from a provider on the FMCSA Training Provider Registry, whether the training is paid for by the driver or the company."),
    ("Does upgrading from a Class B to a Class A CDL require ELDT?", "Yes. The Class B to Class A upgrade has its own ELDT theory and behind-the-wheel requirements."),
    ("Can a trucking company buy ELDT theory training for its drivers?", "Yes. Through an ELDT Partner Program page, a company can let drivers purchase training themselves or purchase it on their behalf."),
],
"related": ["eldt-for-staffing-agencies", "spanish-eldt-training", "hazmat-endorsement-eldt-requirements"],
},

# ---------------------------------------------------------------------------
{
"slug": "eldt-for-staffing-agencies",
"title": "ELDT for Staffing Agencies: Build a CDL Driver Pipeline and New Revenue",
"seo_title": "ELDT Training for Staffing Agencies & Workforce Programs | CDL Pipeline",
"description": "How driver staffing agencies, workforce development boards, and reentry programs can use ELDT theory training to build CDL candidate pipelines and add a new revenue stream.",
"category": "Business Guides",
"audience": ["staffing", "partners"],
"cta": "partner",
"featured": False,
"lead": "Staffing agencies and workforce programs are often the first stop for people who want to become CDL drivers. ELDT theory is the natural first training step for those candidates, and offering it can turn your candidate pool into a qualified driver pipeline.",
"takeaways": [
    "Candidates without a CDL need ELDT before they can test, so theory is the first training step you can offer them.",
    "Offering ELDT theory through your own partner landing page keeps candidates engaged with your agency instead of drifting to a school or competitor.",
    "In a partner model you earn 50% of every course sold while the registered provider handles compliance, reporting, and support.",
],
"body": """
<h2 id="the-pipeline-problem">The driver pipeline problem</h2>
<p>Driver staffing agencies have plenty of people who <em>want</em> to drive and plenty of clients who need drivers. The gap is qualification: a candidate without a CDL can't be placed in a CDL role, and getting that CDL now requires ELDT.</p>
<p>If your agency simply tells candidates to "go get a CDL," many never return. If you guide them through the first training step yourself, they stay connected to you as they progress.</p>

<h2 id="theory-as-first-step">ELDT theory as the first step</h2>
<p>A typical path for a new candidate looks like this:</p>
<ol>
<li><strong>Commercial learner's permit (CLP).</strong> The candidate passes the state knowledge tests.</li>
<li><strong>ELDT theory.</strong> Completed online at the candidate's own pace, often in a week or two around their current job.</li>
<li><strong>Behind-the-wheel training</strong> with a CDL school or a client carrier's training program.</li>
<li><strong>Skills test</strong> and CDL issuance.</li>
<li><strong>Placement</strong> with your client.</li>
</ol>
<p>Steps 2 and 5 are where your agency can add the most value. By offering theory directly, you keep the candidate in your ecosystem from day one.</p>

<h2 id="workforce-programs">For workforce boards and reentry programs</h2>
<p>Workforce development boards, community organizations, and reentry programs often fund CDL training as a path to stable, well-paying work. Online theory with a bilingual toggle is a cost-effective way to start participants on that path, and lets case managers track progress before committing funds to behind-the-wheel training. Confirm funding eligibility rules with your program administrator.</p>

<h2 id="revenue-model">How the revenue works</h2>
<p>With the <a href="/partner-program.html">ELDT Partner Program</a>, your agency gets a dedicated landing page offering the full ELDT theory library: Class A, Class B, B-to-A upgrade, Hazmat, Hazmat &amp; Tank Vehicle, Tanker, Passenger, and School Bus.</p>
<ul>
<li><strong>No setup fee</strong> and no platform cost.</li>
<li>Candidates <strong>buy directly</strong>, or your agency <strong>buys on their behalf</strong>, for example as a hiring incentive.</li>
<li>ELDTTraining.us is the <strong>provider and seller of record</strong>, handling checkout, certificates, TPR reporting, recordkeeping, and support.</li>
<li>Every sale is split <strong>50/50</strong> with your agency.</li>
</ul>
<p>Because you never become the training provider of record, you take on no curriculum, reporting, or audit obligations.</p>

<div class="inline-cta"><p><strong>Turn candidates into CDL-ready drivers.</strong> Launch your agency's ELDT theory page at no cost.</p><a href="/apply.html" class="btn btn-primary btn-sm">Become a Partner</a></div>

<h2 id="marketing-ideas">Ideas for promoting your training page</h2>
<ul>
<li>Add the link to job postings that require a CDL: "Don't have your CDL yet? Start here."</li>
<li>Include it in candidate onboarding emails and texts.</li>
<li>Share it at job fairs and community events.</li>
<li>Offer to cover the cost of theory for candidates who commit to a placement.</li>
<li>Promote the Spanish option to reach bilingual candidates.</li>
</ul>
""",
"faqs": [
    ("Can a staffing agency offer ELDT training without being a registered provider?", "Yes. Through the ELDT Partner Program, ELDTTraining.us, operated by registered provider HAZWOPER OSHA Training, remains the provider and seller of record, while the agency offers training through its own dedicated landing page."),
    ("How much does a staffing agency earn from ELDT courses?", "Partners earn 50% of the revenue from every course sold through their ELDT Partner Program landing page."),
    ("Can our agency purchase training for candidates?", "Yes. Partners can let candidates buy courses directly or purchase training on their behalf."),
],
"related": ["eldt-for-trucking-companies", "add-eldt-training-revenue-associations-consultants", "how-to-become-eldt-theory-training-provider"],
},

# ---------------------------------------------------------------------------
{
"slug": "cdl-schools-outsource-eldt-theory",
"title": "How CDL Schools Can Outsource ELDT Theory and Focus on Behind-the-Wheel",
"seo_title": "CDL Schools: Outsource ELDT Theory Training Online | Partner Program",
"description": "Why CDL and truck driving schools are moving ELDT theory online with a registered partner: lower instructor costs, faster student starts, Spanish-language access, and a share of theory revenue.",
"category": "CDL Schools",
"audience": ["schools", "partners"],
"cta": "partner",
"featured": False,
"lead": "Your trucks, ranges, and instructors are your competitive advantage. Classroom theory isn't. Here's why more CDL schools are moving ELDT theory online with a registered partner, and how to do it without losing revenue.",
"takeaways": [
    "Theory and behind-the-wheel can be delivered by different registered providers, so a school can keep BTW and outsource theory.",
    "Online theory frees instructors for in-truck time, lets students start immediately, and removes curriculum maintenance from your plate.",
    "A partner page lets you keep offering theory to your students while earning 50% of every theory sale.",
],
"body": """
<h2 id="the-classroom-squeeze">The classroom squeeze</h2>
<p>For most CDL schools, the constraint is behind-the-wheel capacity: trucks, range time, and qualified instructors. Every hour an instructor spends teaching theory in a classroom is an hour they're not in a truck generating BTW completions.</p>
<p>Meanwhile, maintaining an ELDT-compliant theory curriculum for Class A, Class B, the B-to-A upgrade, Passenger, School Bus, and Hazmat is a full-time job of its own, and one that doesn't differentiate your school.</p>

<h2 id="split-model">The split model</h2>
<p>Under the ELDT rule, a student can complete theory with one registered provider and behind-the-wheel with another. Each reports its own portion to the Training Provider Registry. That makes a clean division of labor possible:</p>
<ul>
<li><strong>Your school</strong> stays registered for behind-the-wheel and does what it does best.</li>
<li><strong>A theory partner</strong> delivers online theory, assessments, certificates, and TPR reporting for theory.</li>
</ul>
<p>Students arrive at their first range day having already passed theory, so instructors can get straight to driving.</p>

<h2 id="benefits">Benefits for your school</h2>
<ul>
<li><strong>More BTW throughput</strong> from the same instructors and trucks.</li>
<li><strong>Faster starts.</strong> Students begin theory the day they enroll instead of waiting for the next classroom cohort.</li>
<li><strong>No curriculum maintenance</strong> or theory assessment management.</li>
<li><strong>Spanish-language access</strong> with an English/Spanish toggle on every course.</li>
<li><strong>Endorsement add-ons</strong> like Hazmat, Passenger, and School Bus without building new courses.</li>
<li><strong>Continuing revenue</strong> on theory through a revenue share.</li>
</ul>

<h2 id="keeping-revenue">Keeping theory revenue</h2>
<p>The biggest worry schools have about outsourcing theory is losing that revenue. A partner model solves it. With the <a href="/partner-program.html">ELDT Partner Program</a>, your school gets a dedicated landing page offering the full theory library. Students buy through your page (or you buy on their behalf as part of tuition), ELDTTraining.us handles delivery and compliance, and every sale is split 50/50 with you.</p>
<p>You can also send graduates back to your page later when they need an upgrade or a new endorsement, which turns one-time students into long-term customers.</p>

<div class="inline-cta"><p><strong>Put your instructors back in the truck.</strong> Add online ELDT theory to your school at no cost.</p><a href="/apply.html" class="btn btn-primary btn-sm">Apply as a School</a></div>

<h2 id="getting-started">Getting started</h2>
<ol>
<li><a href="/apply.html">Apply to the Partner Program</a> with your school's details.</li>
<li>We build your landing page with the full ELDT theory catalog.</li>
<li>Add the link to enrollment, orientation, and your website.</li>
<li>Students complete theory online; you run behind-the-wheel.</li>
</ol>
""",
"faqs": [
    ("Can a CDL school outsource ELDT theory training?", "Yes. FMCSA allows theory and behind-the-wheel training to be completed with different registered providers, so a school can deliver behind-the-wheel training and use a partner for theory."),
    ("Do students need to finish theory before behind-the-wheel?", "Federal rules don't mandate an order, but both must be completed and reported before the skills test. Many schools have students complete theory first."),
    ("Can my school include theory in its tuition package?", "Yes. Partners can purchase courses on their students' behalf through their landing page, so theory can be bundled into tuition."),
],
"related": ["eldt-theory-vs-behind-the-wheel", "how-to-become-eldt-theory-training-provider", "spanish-eldt-training"],
},

# ---------------------------------------------------------------------------
{
"slug": "hazmat-endorsement-eldt-requirements",
"title": "Hazmat Endorsement ELDT Requirements: What Drivers and Employers Need to Know",
"seo_title": "Hazmat (H) Endorsement ELDT Requirements | Theory-Only Training Guide",
"description": "ELDT requirements for the Hazardous Materials (H) and Hazmat & Tank Vehicle (X) endorsements: theory-only training, curriculum topics, TSA security threat assessment, and how employers can speed up the process.",
"category": "Endorsements",
"audience": ["employers", "government", "staffing", "schools"],
"cta": "partner",
"featured": False,
"lead": "Hazmat-endorsed drivers command higher pay and open doors to fuel, chemical, and specialized freight. The good news for employers: hazmat is the one ELDT category that's theory only, which means it can be completed entirely online.",
"takeaways": [
    "Drivers getting the Hazardous Materials (H) endorsement for the first time must complete ELDT hazmat theory before the H knowledge test.",
    "There is no behind-the-wheel requirement for hazmat, so the ELDT portion can be completed fully online.",
    "Drivers also need a TSA security threat assessment, so start both processes early.",
],
"body": """
<h2 id="who-needs-it">Who needs hazmat ELDT</h2>
<p>Any driver getting the Hazardous Materials (H) endorsement for the first time must complete hazmat ELDT theory, and the state checks the Training Provider Registry before administering the hazmat knowledge test. The combined <strong>Hazmat &amp; Tank Vehicle (X)</strong> endorsement includes the H endorsement, so first-time X applicants need hazmat theory too.</p>
<p>Drivers who already hold an H endorsement and are simply renewing it don't need to repeat ELDT, though they still must meet renewal and security threat assessment requirements.</p>

<h2 id="curriculum">What the hazmat theory curriculum covers</h2>
<p>Appendix E of 49 CFR Part 380 lays out the hazmat theory curriculum, including:</p>
<ul>
<li>Basic introductory hazmat requirements and definitions</li>
<li>Reading and using shipping papers</li>
<li>Marking, labeling, and placarding requirements</li>
<li>Loading, unloading, segregation, and securement</li>
<li>Bulk packaging and tank marking</li>
<li>Hazmat routing and driving and parking rules</li>
<li>Emergency response procedures and incident reporting</li>
<li>Security awareness and hazmat security plans</li>
<li>Special requirements for specific hazard classes</li>
</ul>
<p>Drivers must complete the full curriculum and score at least 80% on the theory assessment.</p>

<h2 id="tsa">Don't forget the TSA security threat assessment</h2>
<p>Separate from ELDT, every hazmat endorsement applicant must pass a Transportation Security Administration (TSA) security threat assessment, which includes fingerprinting and a background check. It can take several weeks, so employers often have drivers start the TSA application and ELDT theory at the same time.</p>

<h2 id="employer-strategy">An employer's hazmat upskilling strategy</h2>
<p>Because hazmat ELDT is theory only, it's one of the easiest credentials to add to an existing driver workforce:</p>
<ol>
<li>Identify drivers with clean records who want hazmat lanes.</li>
<li>Have them start the TSA threat assessment.</li>
<li>Assign hazmat ELDT theory online, completed between loads or during downtime.</li>
<li>Once the TPR record and TSA clearance are in place, the driver takes the H knowledge test.</li>
</ol>
<p>Remember that ELDT is entry-level training. Employers also have ongoing hazmat employee training obligations under 49 CFR Part 172, Subpart H, which is a separate requirement.</p>

<div class="inline-cta"><p><strong>Offer Hazmat, Hazmat &amp; Tank Vehicle, and Tanker theory from your own page</strong>, with no setup cost and a 50/50 revenue split.</p><a href="/partner-program.html" class="btn btn-primary btn-sm">See the Program</a></div>
""",
"faqs": [
    ("Does the hazmat endorsement require behind-the-wheel training under ELDT?", "No. The Hazardous Materials (H) endorsement requires ELDT theory only, with no behind-the-wheel component."),
    ("Do I need ELDT to renew my hazmat endorsement?", "No. ELDT applies when obtaining the H endorsement for the first time. Renewals have their own requirements, including the TSA security threat assessment."),
    ("Does the X endorsement require hazmat ELDT?", "Yes. The combined Hazmat & Tank Vehicle (X) endorsement includes the H endorsement, so first-time applicants need ELDT hazmat theory."),
],
"related": ["eldt-theory-vs-behind-the-wheel", "eldt-for-trucking-companies", "what-is-eldt"],
},

# ---------------------------------------------------------------------------
{
"slug": "spanish-eldt-training",
"title": "Spanish-Language ELDT Training: Options for Bilingual Drivers and Employers",
"seo_title": "Spanish ELDT Theory Training | Bilingual CDL Training for Drivers & Fleets",
"description": "Can ELDT theory be taken in Spanish? What employers, schools, and agencies should know about bilingual ELDT courses, English language proficiency rules, and reaching Spanish-speaking CDL candidates.",
"category": "Employers",
"audience": ["employers", "schools", "staffing", "districts", "government"],
"cta": "partner",
"featured": False,
"lead": "Spanish-speaking workers are a large and growing share of the transportation workforce. Bilingual ELDT theory helps those drivers master complex safety material, as long as employers also plan for federal English language proficiency requirements.",
"takeaways": [
    "The ELDT rule doesn't restrict the language theory is taught in, and bilingual courses help drivers understand complex safety and regulatory material.",
    "Separately, commercial drivers must meet FMCSA English language proficiency requirements, which are actively enforced at roadside inspections.",
    "The strongest approach pairs bilingual theory with English proficiency support, so drivers get both comprehension and compliance.",
],
"body": """
<h2 id="can-eldt-be-in-spanish">Can ELDT theory be taken in Spanish?</h2>
<p>The FMCSA ELDT rule sets curriculum and assessment requirements but doesn't restrict the language of instruction. Many registered providers offer Spanish versions of theory courses, and some, like ELDTTraining.us, include an <strong>English/Spanish toggle</strong> on every course so drivers can switch languages at any time.</p>
<p>A toggle is particularly useful for bilingual learners. A driver can read a hours-of-service module in Spanish to understand the concept, then switch to English to learn the exact terms they'll see on logs, signs, and inspection reports.</p>

<h2 id="english-proficiency">English language proficiency still applies</h2>
<p>Federal regulations at 49 CFR 391.11(b)(2) require commercial drivers to read and speak English well enough to converse with the public, understand highway traffic signs and signals, respond to official inquiries, and make entries on reports and records. Enforcement of that requirement has been strengthened, and drivers who can't demonstrate proficiency can be placed out of service at roadside inspections.</p>
<p>States also set their own rules for which languages CDL knowledge tests are offered in. Check your state driver licensing agency's current policy.</p>
<div class="callout"><p><strong>Bottom line:</strong> Spanish-language training is a comprehension tool, not a substitute for English proficiency. Use it to help drivers truly understand safety material while they build the English skills the job requires.</p></div>

<h2 id="why-it-matters">Why bilingual training matters to employers</h2>
<ul>
<li><strong>Deeper understanding.</strong> Drivers retain complex safety concepts better when they can learn them in their strongest language.</li>
<li><strong>Bigger candidate pool.</strong> Bilingual training opens your recruiting to more applicants.</li>
<li><strong>Fewer failed assessments.</strong> Comprehension issues are a common reason drivers struggle with the 80% theory assessment.</li>
<li><strong>Better retention.</strong> Drivers who feel supported in training are more likely to stay.</li>
</ul>

<h2 id="best-practices">Best practices for a bilingual training program</h2>
<ol>
<li>Offer theory with an English/Spanish toggle so drivers can move between languages.</li>
<li>Encourage drivers to review key terms and road signs in English.</li>
<li>Pair theory with English-language practice for inspection and roadside scenarios.</li>
<li>Use bilingual trainers for behind-the-wheel where possible.</li>
<li>Confirm your state's knowledge test language options before scheduling.</li>
</ol>

<div class="inline-cta"><p><strong>Every course includes an English/Spanish toggle.</strong> Offer bilingual ELDT theory to your audience from your own page.</p><a href="/partner-program.html" class="btn btn-primary btn-sm">Learn More</a></div>
""",
"faqs": [
    ("Can I take ELDT theory training in Spanish?", "Yes. The ELDT rule does not restrict the language of instruction, and many registered providers offer Spanish theory courses. ELDTTraining.us includes an English/Spanish toggle on every course."),
    ("Do CDL drivers need to speak English?", "Yes. Under 49 CFR 391.11(b)(2), commercial drivers must read and speak English sufficiently to communicate with the public, understand traffic signs, respond to official inquiries, and complete reports."),
    ("Can the CDL knowledge test be taken in Spanish?", "It depends on the state. Each state licensing agency sets its own policy on knowledge test languages, so check with yours."),
],
"related": ["eldt-for-trucking-companies", "cdl-schools-outsource-eldt-theory", "what-is-eldt"],
},

# ---------------------------------------------------------------------------
{
"slug": "add-eldt-training-revenue-associations-consultants",
"title": "Adding ELDT Training to Your Business: A Revenue Guide for Associations, Consultants, and Industry Suppliers",
"seo_title": "Earn Revenue Selling ELDT Training | Guide for Associations & Consultants",
"description": "How trucking associations, safety consultants, insurance agencies, equipment dealers, and industry suppliers can add ELDT theory training to their offerings with no setup cost and a 50/50 revenue split.",
"category": "Business Guides",
"audience": ["partners", "staffing", "employers"],
"cta": "partner",
"featured": False,
"lead": "If drivers, carriers, or fleet managers already trust you, you're in a strong position to offer them ELDT training. Here's how associations, consultants, and suppliers are adding a training revenue stream without becoming training companies.",
"takeaways": [
    "ELDT theory is a recurring need: every new CDL, upgrade, and first-time P, S, or H endorsement requires it.",
    "Organizations with an engaged audience can offer it through your own partner landing page with no setup cost.",
    "The registered provider handles delivery, compliance, and support; you earn 50% of every sale.",
],
"body": """
<h2 id="who-this-is-for">Who this is for</h2>
<p>This model fits any organization that regularly talks to CDL drivers or the companies that employ them, such as:</p>
<ul>
<li><strong>Trucking and transportation associations</strong> looking for member benefits and non-dues revenue</li>
<li><strong>Safety and compliance consultants</strong> who advise carriers on DOT requirements</li>
<li><strong>Insurance agencies</strong> that work with commercial auto and fleet clients</li>
<li><strong>Truck, bus, and equipment dealers</strong> whose customers hire drivers</li>
<li><strong>Driver qualification and drug testing providers</strong></li>
<li><strong>Industry publications and online communities</strong> for drivers</li>
<li><strong>Community colleges and adult education programs</strong> without a full CDL program</li>
</ul>

<h2 id="why-eldt">Why ELDT is a good fit</h2>
<ul>
<li><strong>It's required.</strong> You're not convincing anyone they need it; you're making it easy to get.</li>
<li><strong>It recurs.</strong> Every new hire, every upgrade, and every new endorsement creates another purchase.</li>
<li><strong>It's relevant.</strong> Offering compliant, registered training reinforces your role as a trusted resource.</li>
<li><strong>It's online.</strong> Nothing to schedule, ship, or staff.</li>
</ul>

<h2 id="how-it-works">How the partner model works</h2>
<ol>
<li><strong>Apply.</strong> Tell us about your organization and audience.</li>
<li><strong>Launch.</strong> We build a dedicated landing page with the full ELDT theory library. There's no setup fee.</li>
<li><strong>Share.</strong> Promote the page to your members, clients, or customers.</li>
<li><strong>Earn.</strong> ELDTTraining.us handles checkout, certificates, TPR reporting, and support, and splits every sale 50/50 with you.</li>
</ol>
<p>See full details on the <a href="/partner-program.html">ELDT Partner Program page</a>, including <a href="/partner-program.html#program-terms">program terms</a>.</p>

<h2 id="promotion-playbook">A simple promotion playbook</h2>
<h3>For associations</h3>
<p>Add ELDT training to your member benefits page, mention it in your newsletter, and feature it at conferences. Consider buying training on behalf of members' new hires as a sponsorship.</p>
<h3>For consultants</h3>
<p>Include the link in compliance audits and onboarding checklists. When a client hires a new driver or adds hazmat lanes, point them to your page.</p>
<h3>For suppliers and dealers</h3>
<p>Share the page with fleet customers when they add vehicles. New trucks often mean new drivers or upgrades.</p>
<h3>For publications and communities</h3>
<p>Publish helpful content about ELDT (like the guides on this site) and link to your training page as the next step.</p>

<div class="inline-cta"><p><strong>Already have the audience?</strong> Launch your ELDT training page with no setup cost and earn 50% of every sale.</p><a href="/apply.html" class="btn btn-primary btn-sm">Become a Partner</a></div>

<h2 id="faq-liability">What about liability and compliance?</h2>
<p>Because ELDTTraining.us remains the merchant and training provider of record, partners take on no payment processing, course content, or TPR reporting responsibility. Your landing page is your audience's doorway into registered ELDT theory training.</p>
""",
"faqs": [
    ("Who can join the ELDT Partner Program?", "Any business or organization with an audience that needs ELDT training, including associations, consultants, staffing agencies, schools, fleets, suppliers, school districts, and government agencies."),
    ("Is there a cost to become a partner?", "No. There is no setup fee and no cost to join."),
    ("Who handles customer support for partner sales?", "ELDTTraining.us handles checkout, certificates, Training Provider Registry reporting, recordkeeping, and learner support for every purchase made through a partner page."),
],
"related": ["how-to-become-eldt-theory-training-provider", "eldt-for-staffing-agencies", "fmcsa-training-provider-registry-guide"],
},
]
