# Ministry and public-service use-case catalogue

[Return to government playbook](README.md)

**39 proposed use cases · 13 functional areas · 3 readiness levels.** All examples are fictional planning patterns. No card claims a deployed government AI system. Local mandates, ministry names and risk classifications vary.

Every card inherits the [Caribbean safeguards](caribbean-readiness.md). Use the [pilot template](../templates/government-pilot.md) to set owners, cost caps, thresholds, permissions, incident handling and a stop date before testing. Tools below describe categories, not endorsed products.

## Directory

- [1. Finance, revenue and customs](#area-1)
- [2. Agriculture and food security](#area-2)
- [3. Climate and disaster management](#area-3)
- [4. Health and public health](#area-4)
- [5. Education and training](#area-5)
- [6. Labour and social protection](#area-6)
- [7. Tourism, culture and creative industries](#area-7)
- [8. Transport and public infrastructure](#area-8)
- [9. Energy, water and utilities](#area-9)
- [10. Environment, oceans and fisheries](#area-10)
- [11. Justice and public safety administration](#area-11)
- [12. Foreign affairs, citizen services and local government](#area-12)
- [13. Internal HR, procurement and audit](#area-13)

<a id="area-1"></a>
## 1. Finance, revenue and customs

### GOV-01-1: Tax and customs guidance drafts

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Reduce repeated staff searches for public filing and import procedures.
- **Data:** Current published forms, tariff guidance and official service notices; no taxpayer files.
- **Process:** Retrieve the applicable passage, draft a plain-language answer and send it to a trained officer for review.
- **Tools:** Approved document search with a retrieval-grounded language model.
- **Illustrative sample output:** Draft: the published checklist requests documents A and B; officer must verify the effective date and commodity classification.
- **Risks:** Invented rates or deadlines; accidental individual tax advice.
- **Controls:** Cite each rule and date; abstain on classification disputes; no automated assessments.
- **Metrics:** Citation accuracy, correction rate and officer minutes per verified answer.
- **Implementation dependencies:** Revenue-policy owner and a versioned publication library.

### GOV-01-2: Customs document completeness assistant

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Reduce avoidable resubmission before an officer performs the substantive inspection.
- **Data:** Authorised manifests, invoices and published submission requirements.
- **Process:** Extract fields, compare against a deterministic checklist, flag missing or contradictory entries and queue exceptions.
- **Tools:** OCR, schema validation and a controlled work queue.
- **Illustrative sample output:** Review queue: invoice number missing; two gross-weight values conflict; officer confirmation required.
- **Risks:** Bad scans, unusual trade documents and confidential cargo information.
- **Controls:** Display source crops, retain provenance, restrict access and never infer smuggling from a missing field.
- **Metrics:** Field accuracy, false missing-item flags, resubmission rate and reviewer time.
- **Implementation dependencies:** Approved customs-data access, document samples and integration with existing records.

### GOV-01-3: Aggregate revenue and port demand forecasting

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Improve staffing and fiscal scenario planning under seasonal trade and tourism demand.
- **Data:** Approved historical aggregate receipts, volumes, calendar effects and documented policy changes.
- **Process:** Compare seasonal baselines and statistical models; back-test rolling periods; review scenarios with economists and port operations.
- **Tools:** Time-series forecasting and scenario dashboards; language model only for reviewed narrative.
- **Illustrative sample output:** Planning range: port workload may exceed baseline under scenario B; assumptions and interval shown.
- **Risks:** Policy shocks, sparse history and false precision; forecasts mistaken for revenue commitments.
- **Controls:** Use holdout periods, disclose uncertainty, test hurricane and demand shocks, and prohibit individual enforcement use.
- **Metrics:** Forecast error versus seasonal baseline, interval coverage and staffing-planning usefulness.
- **Implementation dependencies:** Consistent historical series, data dictionary, economist and operations review.


<a id="area-2"></a>
## 2. Agriculture and food security

### GOV-02-1: Extension bulletin adaptation

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help extension officers turn regional climate bulletins into clear farmer-facing draft messages.
- **Data:** Current official agroclimatic bulletins and locally approved crop guidance.
- **Process:** Identify island, crop and season; draft a short explanation; extension officer verifies and chooses delivery channel.
- **Tools:** Approved retrieval and translation tools with printable or low-bandwidth output.
- **Illustrative sample output:** Draft for review: the bulletin indicates increased dry-spell risk; consult the extension officer on locally suitable water planning.
- **Risks:** Invented farm-level forecasts and unsafe pesticide or fertiliser advice.
- **Controls:** Preserve forecast uncertainty and issue date; agronomist approves advice; no chemical dosing generated.
- **Metrics:** Correct geographical scope, native-speaker comprehension and officer preparation time.
- **Implementation dependencies:** Agricultural extension lead and approved bulletin feed such as CariSAM.

### GOV-02-2: Farmer enquiry routing

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Route crop, irrigation and market questions to the correct extension service.
- **Data:** Consent-appropriate enquiries, service directory and approved categories; minimum contact details.
- **Process:** Classify topic and locality, identify urgent plant-health concerns for trained review, and create a draft referral.
- **Tools:** Text classifier or rules plus case-management queue.
- **Illustrative sample output:** Draft referral: irrigation-support team; parish supplied by caller; crop-disease diagnosis not established.
- **Risks:** Misrouting dialect-rich enquiries and exposing farm locations or commercial details.
- **Controls:** Allow self-correction and human intake; never reject help because classification confidence is low.
- **Metrics:** Routing precision, unresolved enquiry time and performance across languages/channels.
- **Implementation dependencies:** Updated regional service directory, case owner and telephone/offline intake.

### GOV-02-3: Crop supply and irrigation planning scenarios

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Support aggregate water and food-supply planning before committing resources.
- **Data:** Authorised crop surveys, weather series, water availability and satellite indicators with documented resolution.
- **Process:** Build regional scenarios, compare with agronomic baselines and validate against observed seasons and ground reports.
- **Tools:** GIS, statistical or ML forecasts and constraint-based planning.
- **Illustrative sample output:** Scenario: district-level irrigation demand range under a dry season; missing sensor areas flagged.
- **Risks:** Sparse sensors, smallholder exclusion and estimates treated as individual farm facts.
- **Controls:** Publish coverage limits, include field verification and avoid automatic subsidy or allocation decisions.
- **Metrics:** Forecast error, geographic coverage, uncertainty calibration and planner usefulness.
- **Implementation dependencies:** Agronomists, water agency cooperation, maintained sensors and approved data-sharing arrangements.


<a id="area-3"></a>
## 3. Climate and disaster management

### GOV-03-1: Emergency briefing pack assistant

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Reduce time spent assembling approved situation reports for emergency staff.
- **Data:** Official meteorological advisories, verified agency situation reports and current contact directories.
- **Process:** Extract facts with timestamps, list conflicts and missing updates, and draft a briefing for the duty officer.
- **Tools:** Restricted-source retrieval and structured summarisation.
- **Illustrative sample output:** Draft: advisory issued at 14:00; shelter count pending local confirmation; no new warning generated.
- **Risks:** Stale notices, false shelter availability and invented protective actions.
- **Controls:** Always retain source time; duty officer approves; never issue warnings or evacuation orders.
- **Metrics:** Fact traceability, stale-source detection and briefing preparation time.
- **Implementation dependencies:** Emergency management owner and verified source/update schedule.

### GOV-03-2: Relief request reconciliation

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Help coordinators find potentially duplicated requests and incomplete logistics information.
- **Data:** Authorised request forms, distribution records and verified facility lists.
- **Process:** Extract needed fields, suggest possible duplicates, and route uncertain cases to local coordinators.
- **Tools:** OCR, conservative record linkage and a queue that preserves every original request.
- **Illustrative sample output:** Possible duplicate requests for the same shelter; quantities differ; coordinator verification required.
- **Risks:** False duplicates deny aid; sensitive household data leaks; uneven connectivity.
- **Controls:** Never auto-delete or deny; protect household data; allow offline entry and track reconciliation status.
- **Metrics:** False-duplicate rate, unresolved requests, time to verified dispatch and missed-need review.
- **Implementation dependencies:** Relief operations lead, offline workflow and shared identifiers with lawful access.

### GOV-03-3: Shelter and supply scenario planning

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Test preparedness options before a storm rather than improvising under pressure.
- **Data:** Approved hazard scenarios, verified shelter capacities, road constraints and aggregate population estimates.
- **Process:** Simulate disruptions, identify bottlenecks and compare allocations with experienced emergency planners.
- **Tools:** GIS, simulation and optimisation with explicit operational constraints.
- **Illustrative sample output:** Tabletop option: route unavailable in scenario C; alternate shelter requires capacity verification.
- **Risks:** Outdated capacity, unsafe routes and optimisation ignoring disabled or remote residents.
- **Controls:** Field-verify assets, include accessibility and travel constraints, and keep all operational decisions with authorities.
- **Metrics:** Scenario feasibility, underserved-area coverage, robustness under road/power loss and drill feedback.
- **Implementation dependencies:** Validated asset inventory, emergency planners and periodic exercises.


<a id="area-4"></a>
## 4. Health and public health

### GOV-04-1: Approved health communication drafting

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help communications teams explain approved public-health material clearly.
- **Data:** Current ministry or PAHO-approved public information and translation glossary; no patient data.
- **Process:** Draft a leaflet or FAQ, verify claims against source text and obtain clinical and language review.
- **Tools:** Document-grounded drafting and accessibility checker.
- **Illustrative sample output:** Draft clinic leaflet: service hours and approved prevention guidance, with source date and reviewer field.
- **Risks:** Medical misinformation, mistranslation and readers treating a generic answer as diagnosis.
- **Controls:** No individual diagnosis or treatment; clinical sign-off; clear emergency and human-contact instructions supplied by authority.
- **Metrics:** Unsupported-claim rate, readability, accessibility and reviewer corrections.
- **Implementation dependencies:** Clinical communications owner and current approved materials.

### GOV-04-2: Clinic administration and stock workflow support

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Reduce administrative backlog without influencing clinical priority.
- **Data:** Authorised appointment logistics and inventory records with patient identifiers minimised.
- **Process:** Extract scheduling requests or stock entries, validate required fields and propose staff-reviewed administrative tasks.
- **Tools:** Rules, OCR and approved workflow integration.
- **Illustrative sample output:** Draft task: confirm appointment date by authorised channel; stock discrepancy needs count.
- **Risks:** Patient confidentiality, incorrect reminders and workflow urgency mistaken for clinical triage.
- **Controls:** Separate administration from care decisions; verify identity through existing process; prevent autonomous messages or medication substitution.
- **Metrics:** Administrative error rate, stock-record discrepancies and staff handling time.
- **Implementation dependencies:** Health-data approval, access controls, clinic owner and a clinical escalation route.

### GOV-04-3: Aggregate service and disease-demand surveillance support

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Help public-health analysts detect unusual aggregate patterns for investigation.
- **Data:** Lawfully accessible, disclosure-controlled surveillance counts, laboratory reporting and population denominators.
- **Process:** Check completeness, compare seasonal statistical baselines, produce uncertainty-aware flags and request epidemiologist review.
- **Tools:** Time-series anomaly detection and epidemiological dashboards.
- **Illustrative sample output:** Analyst flag: reporting increased above baseline; delayed uploads could explain the change; investigate before public alert.
- **Risks:** Reporting changes mistaken for outbreaks, small-cell identification and missed outbreaks.
- **Controls:** Suppress small cells appropriately, model delays, validate sensitivity and false alarms, and retain human alert authority.
- **Metrics:** Detection delay, sensitivity, false-alarm burden and data completeness.
- **Implementation dependencies:** Epidemiologist, surveillance governance, stable reporting and health-sector validation.


<a id="area-5"></a>
## 5. Education and training

### GOV-05-1: Teacher planning and accessible resources

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Reduce preparation time while keeping curriculum and pedagogy with educators.
- **Data:** Approved curriculum, licensed materials and teacher-created synthetic examples; no student records.
- **Process:** Draft differentiated lesson activities, check learning objectives and adapt examples to local contexts.
- **Tools:** Approved drafting tool and accessibility/format checks.
- **Illustrative sample output:** Draft activity: compare water-use scenarios using fictional Caribbean household data; teacher verifies answer key.
- **Risks:** Incorrect facts, cultural stereotypes and copyrighted or inappropriate material.
- **Controls:** Teacher review, rights checks, age suitability and accessible alternatives; do not profile children.
- **Metrics:** Teacher editing time, factual accuracy and lesson accessibility.
- **Implementation dependencies:** Curriculum lead, teachers and approved resource library.

### GOV-05-2: School administration document support

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Improve completeness checks for non-decision administrative processes.
- **Data:** Authorised inventory, maintenance and school-operation forms; minimise child data.
- **Process:** Extract fields, validate against an approved checklist and route missing information to staff.
- **Tools:** OCR and rules-backed workflow queue.
- **Illustrative sample output:** Draft work item: maintenance form lacks building identifier; confirm before scheduling visit.
- **Risks:** Exposure of children’s information and administrative flags affecting access to education.
- **Controls:** Use non-student forms first; restricted access; no automatic admissions, discipline or service denial.
- **Metrics:** Extraction accuracy, turnaround and privacy incidents.
- **Implementation dependencies:** Education records owner, safeguarding review and approved school workflow.

### GOV-05-3: School resource and transport planning

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Support aggregate infrastructure, teacher-capacity and transport scenarios.
- **Data:** Approved aggregate enrolment trends, facilities, travel constraints and disability-access needs in disclosure-controlled form.
- **Process:** Compare demographic baselines, model plausible demand and review proposals with local educators and communities.
- **Tools:** Forecasting, GIS and constrained planning.
- **Illustrative sample output:** Planning scenario: additional classroom capacity may be needed in district D; range and assumptions shown.
- **Risks:** Small-group identification, biased historical allocation and excluding remote schools.
- **Controls:** Protect small cells, include equity constraints and community review; no individual student ranking.
- **Metrics:** Forecast error, underserved-area coverage and feasibility of reviewed scenarios.
- **Implementation dependencies:** Reliable aggregate data, planning expertise and lawful inter-agency collaboration.


<a id="area-6"></a>
## 6. Labour and social protection

### GOV-06-1: Public benefits information assistant for staff

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help officers explain published programme rules without deciding entitlement.
- **Data:** Current public programme guidance, forms, opening hours and appeal contacts.
- **Process:** Retrieve the appropriate jurisdiction and programme passage, draft an explanation and ask the officer to verify.
- **Tools:** Cited document retrieval and plain-language drafting.
- **Illustrative sample output:** Draft: these are the published documents requested for an application; eligibility must be assessed by an officer.
- **Risks:** Stale eligibility rules, fabricated entitlements and discouraging legitimate applications.
- **Controls:** No eligibility scoring, denial or certainty beyond sources; preserve assisted application and appeal routes.
- **Metrics:** Citation accuracy, applicant comprehension and incorrect guidance rate.
- **Implementation dependencies:** Programme owner and monitored policy updates.

### GOV-06-2: Application completeness and case-note drafting

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Help caseworkers organise evidence while preserving applicants’ rights.
- **Data:** Authorised applications and approved checklist; strictly scoped sensitive data.
- **Process:** Extract facts, identify missing items as questions, and draft a case summary with document references.
- **Tools:** Secure OCR and controlled summarisation inside the approved case system.
- **Illustrative sample output:** Draft note: address evidence not located in supplied documents; ask applicant whether alternative evidence is available.
- **Risks:** Missing documents treated as fraud, hallucinated facts and disclosure of hardship information.
- **Controls:** Human fact-check; no automated denial; allow alternative evidence and correction; access audit.
- **Metrics:** False missing-item flags, caseworker corrections, time and appeal-related errors.
- **Implementation dependencies:** Legal/data review, caseworker capacity and accessible assistance.

### GOV-06-3: Aggregate service-capacity planning

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Anticipate staffing and outreach demand after economic or disaster shocks.
- **Data:** Disclosure-controlled caseload totals, service times and aggregate labour indicators.
- **Process:** Forecast demand ranges, test disruption scenarios and discuss resource options with frontline services.
- **Tools:** Time-series models and scenario planning.
- **Illustrative sample output:** Capacity scenario: additional appointments may be needed after a disruption; model does not identify individual claimants.
- **Risks:** Incomplete informal-sector data, stigma and predictions reused to deny benefits.
- **Controls:** Prohibit individual eligibility/enforcement use; document missing groups and assess geographic fairness.
- **Metrics:** Demand error, waiting-time improvement and underserved-community coverage.
- **Implementation dependencies:** Programme analyst, reliable totals and outreach consultation.


<a id="area-7"></a>
## 7. Tourism, culture and creative industries

### GOV-07-1: Visitor information and cultural-content drafts

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help public tourism teams maintain clear, locally grounded information.
- **Data:** Approved visitor guidance, verified attraction information and rights-cleared cultural content.
- **Process:** Draft accessible multilingual summaries and have local experts check cultural representation and current details.
- **Tools:** Grounded drafting and translation with image-rights review.
- **Illustrative sample output:** Draft visitor note: accessibility and opening times require confirmation with the named operator.
- **Risks:** Invented openings, unsafe advice, cultural appropriation and copyrighted content.
- **Controls:** Verify practical facts, respect community protocols and obtain permissions for protected stories or imagery.
- **Metrics:** Factual corrections, language quality and accessibility coverage.
- **Implementation dependencies:** Tourism content owner and community/cultural reviewers.

### GOV-07-2: Tourism licence enquiry routing

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Improve administrative service for small tourism operators.
- **Data:** Public licence guidance and authorised incoming enquiries with minimum contact data.
- **Process:** Classify question, show relevant form and draft a referral to the responsible office.
- **Tools:** Service directory retrieval and rules-backed intake queue.
- **Illustrative sample output:** Draft referral: accommodation licence enquiry; environmental permit question requires another agency.
- **Risks:** Confusing different territories’ rules and accidental licence promises.
- **Controls:** Show jurisdiction, source and office; staff approves; no licence grants or enforcement decisions.
- **Metrics:** Correct routing, repeat contact and resolution time.
- **Implementation dependencies:** Updated multi-agency directory and tourism service owner.

### GOV-07-3: Aggregate visitor-flow and cultural-event planning

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Support infrastructure and event planning without tracking individuals.
- **Data:** Licensed aggregate arrival, occupancy, transport and event-calendar data with privacy safeguards.
- **Process:** Compare seasonal baselines, estimate demand ranges and test local crowd-management options.
- **Tools:** Forecasting and aggregate spatial analysis.
- **Illustrative sample output:** Scenario: ferry demand may peak during the festival weekend; uncertainty and missing informal accommodation data listed.
- **Risks:** Surveillance creep, small-cell reidentification and demand shocks.
- **Controls:** Avoid individual tracking; protect granular location data; review plans with communities and transport authorities.
- **Metrics:** Forecast error, crowd-plan feasibility and resident-impact measures.
- **Implementation dependencies:** Lawful aggregate data access, planners and event coordination.


<a id="area-8"></a>
## 8. Transport and public infrastructure

### GOV-08-1: Maintenance report summarisation

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help engineers review inspection narratives and work orders faster.
- **Data:** Authorised inspection reports, asset manuals and photos cleared for the tool.
- **Process:** Summarise reported defects with source locations and draft questions for qualified inspectors.
- **Tools:** Document retrieval, OCR and reviewed summarisation.
- **Illustrative sample output:** Draft: report mentions cracking at asset X; severity requires engineer assessment.
- **Risks:** Hallucinated defects, missed critical issues and sensitive asset exposure.
- **Controls:** No engineering certification; show originals; qualified review and urgent escalation procedures.
- **Metrics:** Fact accuracy, missed-item review and engineer preparation time.
- **Implementation dependencies:** Asset owner, engineer and secure document access.

### GOV-08-2: Public works request routing

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Organise road, drainage and lighting reports for staff verification.
- **Data:** Authorised citizen reports and verified asset/location directory.
- **Process:** Extract location and problem type, suggest duplicates and propose the responsible team.
- **Tools:** Text extraction, GIS lookup and dispatch queue with human approval.
- **Illustrative sample output:** Draft work item: blocked drain location uncertain; confirm landmark before dispatch.
- **Risks:** Wrong location, malicious reports and duplicate handling that hides real hazards.
- **Controls:** Preserve originals, allow corrections and separate triage from final safety assessment.
- **Metrics:** Routing accuracy, location confirmation rate and response backlog.
- **Implementation dependencies:** Maintained asset map, operations team and offline intake.

### GOV-08-3: Maintenance prioritisation decision support

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Help engineers compare preventative maintenance options transparently.
- **Data:** Approved asset condition history, inspection dates, repair costs and service criticality.
- **Process:** Compare simple condition rules with predictive models; rank scenarios for engineer review, not automatic work approval.
- **Tools:** Reliability models and constrained capital-planning analysis.
- **Illustrative sample output:** Review list: asset Y has elevated uncertainty due to old inspection; schedule verification before capital decision.
- **Risks:** Incomplete histories, biased inspection coverage and safety overconfidence.
- **Controls:** Qualified engineering sign-off, explainable factors, field validation and no autonomous infrastructure control.
- **Metrics:** Failure prediction calibration, coverage, cost-effectiveness and missed critical defects.
- **Implementation dependencies:** Reliable asset register, inspectors and maintained condition data.


<a id="area-9"></a>
## 9. Energy, water and utilities

### GOV-09-1: Customer notice and outage briefing drafts

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help utility staff communicate verified service information.
- **Data:** Approved outage bulletins, tariff explanations and customer-service procedures.
- **Process:** Produce plain-language and accessible drafts, preserving affected area and update timestamp.
- **Tools:** Restricted retrieval and controlled drafting.
- **Illustrative sample output:** Draft notice: reported interruption in area A as of 09:00; restoration estimate not confirmed.
- **Risks:** False restoration promises, inaccurate tariffs and unsafe electrical advice.
- **Controls:** Operations approval; never invent restoration times or safety instructions.
- **Metrics:** Accuracy, correction rate and publication preparation time.
- **Implementation dependencies:** Communications owner and live operations verification.

### GOV-09-2: Meter and work-order exception review

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Reduce clerical errors before billing or maintenance staff act.
- **Data:** Authorised meter readings, work orders and documented business rules.
- **Process:** Flag missing or inconsistent entries, show source records and queue corrections for authorised staff.
- **Tools:** Rules and anomaly checks integrated with a review queue.
- **Illustrative sample output:** Review flag: reading differs sharply from prior period; inspect meter record before any bill adjustment.
- **Risks:** False fraud allegations, disconnection risk and exposing household consumption.
- **Controls:** No automated disconnection, penalties or fraud conclusions; access controls and customer correction route.
- **Metrics:** False-positive burden, corrected records and unresolved exceptions.
- **Implementation dependencies:** Utility data owner, operational rules and billing safeguards.

### GOV-09-3: Demand and leak-investigation planning

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Improve aggregate water/energy planning and target engineering inspections.
- **Data:** Approved network-zone totals, weather, maintenance history and sensor quality indicators.
- **Process:** Forecast demand or flag zone-level anomalies; compare baselines and seek engineer confirmation.
- **Tools:** Time-series models, hydraulic/engineering context and dashboards.
- **Illustrative sample output:** Investigation suggestion: zone flow anomaly may reflect sensor error or a leak; field verification needed.
- **Risks:** Sensor failure, weather shifts and recommendations mistaken for safe control commands.
- **Controls:** No autonomous grid/pump switching; model uncertainty, verify sensors and maintain emergency operations.
- **Metrics:** Forecast error, verified anomaly yield, sensor coverage and engineering usefulness.
- **Implementation dependencies:** Engineers, trusted telemetry and secure separation from operational controls.


<a id="area-10"></a>
## 10. Environment, oceans and fisheries

### GOV-10-1: Environmental evidence brief drafting

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help officers synthesise approved environmental monitoring material.
- **Data:** Public monitoring bulletins, rights-cleared reports and official permit guidance.
- **Process:** Summarise source-specific observations and uncertainties for officer review.
- **Tools:** Document-grounded summarisation and glossary-assisted translation.
- **Illustrative sample output:** Draft brief: the cited monitoring report covers specified coastal sites; other sites have no observation.
- **Risks:** Invented environmental findings and treating regional data as site-specific proof.
- **Controls:** Cite spatial/time coverage; no permit decisions or scientific certainty beyond evidence.
- **Metrics:** Traceability, spatial-scope errors and analyst time.
- **Implementation dependencies:** Environmental science reviewer and approved evidence library.

### GOV-10-2: Fisheries and environmental report organisation

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Route observations and paperwork to appropriate technical teams.
- **Data:** Authorised catch/inspection forms and community reports; protect sensitive fishing locations.
- **Process:** Extract species, location and date as reported; flag uncertainty and route for expert verification.
- **Tools:** OCR, controlled vocabulary and GIS-assisted queue.
- **Illustrative sample output:** Review entry: species identification uncertain; fisher’s location remains restricted to authorised officers.
- **Risks:** Misidentification, loss of livelihoods and sensitive-location disclosure.
- **Controls:** No enforcement or licence action from model output; expert verification and access restrictions.
- **Metrics:** Field accuracy, species uncertainty handling and routing time.
- **Implementation dependencies:** Fisheries/environment data steward and trained reviewers.

### GOV-10-3: Coastal ecosystem change screening

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Prioritise where scientists should verify possible coastal change.
- **Data:** Licensed satellite imagery, cloud masks, field surveys and documented baseline maps.
- **Process:** Compare time periods, detect candidate changes and validate against ground observations.
- **Tools:** Remote sensing, GIS and image classification with uncertainty layers.
- **Illustrative sample output:** Candidate change: coastal vegetation loss signal; cloud contamination and seasonal effects must be checked.
- **Risks:** Cloud/shadow errors, weak ground truth and map outputs used as enforcement evidence.
- **Controls:** Independent field validation; disclose resolution and coverage; no automatic land-use sanctions.
- **Metrics:** Precision/recall against surveys, cloud coverage and field-verification yield.
- **Implementation dependencies:** Remote-sensing expertise, data licences and ongoing field budget.


<a id="area-11"></a>
## 11. Justice and public safety administration

### GOV-11-1: Public legal-service information drafting

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help court and justice-service staff explain published administrative procedures.
- **Data:** Current official public procedure guides, court office contacts and approved forms.
- **Process:** Retrieve exact procedural sources, draft a plain-language explanation and refer legal questions to authorised professionals.
- **Tools:** Cited retrieval and staff-reviewed drafting.
- **Illustrative sample output:** Draft: filing office location and published form link; deadline calculation requires qualified verification.
- **Risks:** Invented law, missed deadlines and unauthorised legal advice.
- **Controls:** No case advice, sentencing or credibility assessment; verify citations and preserve access to a person.
- **Metrics:** Citation validity, procedural accuracy and staff correction rate.
- **Implementation dependencies:** Court/justice content owner and qualified review.

### GOV-11-2: Administrative records and disclosure preparation

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Help authorised records staff organise documents for human review.
- **Data:** Lawfully accessible case administration documents in a protected environment.
- **Process:** Index documents, flag possible duplicate pages and suggest redactions for an authorised reviewer.
- **Tools:** Secure OCR, search and redaction suggestion tools.
- **Illustrative sample output:** Review packet: possible address in page 4; reviewer must confirm and check the rendered redaction.
- **Risks:** Disclosure of victims, witnesses or protected information; missing exculpatory material.
- **Controls:** Never auto-release, destroy or hide records; verify redaction pixels and searchable text; preserve chain of custody.
- **Metrics:** Retrieval completeness, missed sensitive spans and reviewer correction rate.
- **Implementation dependencies:** Legal authority, records specialists, secure infrastructure and audit controls.

### GOV-11-3: Aggregate court and emergency-service capacity planning

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Support staffing and facility planning without predicting individual offending.
- **Data:** Disclosure-controlled caseload totals, service times, geography and resource constraints.
- **Process:** Model backlog/demand scenarios, compare baselines and review with operational leaders.
- **Tools:** Queue simulation, forecasting and capacity planning.
- **Illustrative sample output:** Scenario: additional administrative hearing support could reduce queue growth; no individual case is ranked.
- **Risks:** Historical inequality reproduced in resource allocation and scope creep into predictive policing.
- **Controls:** Prohibit person-level risk scoring, facial recognition and automatic enforcement; review geographic fairness.
- **Metrics:** Backlog forecast error, staffing feasibility and equitable access measures.
- **Implementation dependencies:** Validated aggregate records, operations researchers and justice/public-safety oversight.


<a id="area-12"></a>
## 12. Foreign affairs, citizen services and local government

### GOV-12-1: Consular and municipal service guide drafts

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help staff answer common administrative questions with local accuracy.
- **Data:** Approved consular, registry, permit and municipal service pages and verified contact lists.
- **Process:** Retrieve jurisdiction-specific requirements, draft a checklist and ask an officer to check current status.
- **Tools:** Cited retrieval and translation with human review.
- **Illustrative sample output:** Draft checklist: documents listed on the official page; emergency assistance requires the verified consular contact.
- **Risks:** Visa/entry promises, outdated contacts and confusion across jurisdictions.
- **Controls:** No immigration or nationality decisions; verify deadlines and emergency routes; show uncertainty.
- **Metrics:** Source accuracy, jurisdiction errors and accessibility/language quality.
- **Implementation dependencies:** Service owners and regular source review.

### GOV-12-2: Citizen correspondence routing

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Reduce the time letters and complaints spend in the wrong department.
- **Data:** Authorised correspondence with personal details minimised and an approved responsibility map.
- **Process:** Identify topic and requested action, draft acknowledgement and propose the receiving officer for approval.
- **Tools:** Text classification, protected summarisation and case-management integration.
- **Illustrative sample output:** Draft routing: drainage complaint to municipal works; compensation request requires separate authorised review.
- **Risks:** Misrouting urgent cases, disclosing complaints and invented promises.
- **Controls:** Human review, protected whistleblower route, clear urgency escalation and no automatic external sending.
- **Metrics:** Routing precision, lost-case rate and time to responsible officer.
- **Implementation dependencies:** Cross-agency service map, records policy and accountable case owners.

### GOV-12-3: Municipal service planning and public consultation analysis

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Help planners understand aggregate service demand and consultation themes.
- **Data:** Lawfully collected, disclosure-reviewed consultation responses and service-demand totals.
- **Process:** Cluster themes, preserve minority views and citations, and compare planning options with staff and communities.
- **Tools:** Text analysis, aggregate GIS and scenario tools.
- **Illustrative sample output:** Draft synthesis: majority and minority themes listed separately; duplicates and sample limitations disclosed.
- **Risks:** Treating consultation as a representative poll, missing dialect-rich views and reidentifying speakers.
- **Controls:** No demographic inference; audit omitted viewpoints; retain human reading of material concerns and publish methodology.
- **Metrics:** Theme coverage, minority-view retention, correction rate and stakeholder feedback.
- **Implementation dependencies:** Consultation mandate, privacy review, community participation and analysts.


<a id="area-13"></a>
## 13. Internal HR, procurement and audit

### GOV-13-1: Internal policy and procurement-document assistant

**Level 1: Assistive** · Proposed pattern · Low integration complexity; subject-matter review still required.

- **Value:** Help staff find approved administrative procedures and prepare checklists.
- **Data:** Current HR/procurement policies and public templates; no employee case files or confidential bids.
- **Process:** Retrieve relevant rules, draft a checklist and flag policy conflicts for responsible officers.
- **Tools:** Grounded search and assistive drafting.
- **Illustrative sample output:** Draft checklist: approval route and required documents; procurement officer verifies threshold and effective rules.
- **Risks:** Stale procurement limits, fabricated exceptions and sensitive information entered casually.
- **Controls:** Citations and policy-owner approval; no hiring, disciplinary, award or contract decisions.
- **Metrics:** Citation accuracy, checklist completeness and staff time.
- **Implementation dependencies:** Policy librarian and HR/procurement owner.

### GOV-13-2: Invoice and purchase-order reconciliation support

**Level 2: Workflow** · Proposed pattern · Medium integration complexity; protected records and exception handling required.

- **Value:** Help finance and audit staff review documentary discrepancies.
- **Data:** Authorised invoices, purchase orders and receipt records with restricted supplier/payment data.
- **Process:** Extract fields, perform deterministic matching and list discrepancies with source evidence.
- **Tools:** OCR, arithmetic/rule checks and approval-controlled workflow.
- **Illustrative sample output:** Review item: invoice quantity differs from goods-received record; investigate before payment approval.
- **Risks:** False fraud allegations, duplicate payments and incorrect account changes.
- **Controls:** Never initiate payments or alter bank details; segregate duties; reviewer verifies originals.
- **Metrics:** Matching accuracy, false exceptions, reviewer time and recovered clerical errors.
- **Implementation dependencies:** Finance controls, approved supplier master and secure integration.

### GOV-13-3: Aggregate workforce and audit coverage planning

**Level 3: Advanced governed** · Proposed pattern · High analytical/operational complexity; specialist validation and ongoing monitoring required.

- **Value:** Support training, workload balance and audit sampling at organisational level.
- **Data:** Approved aggregate workload, skills inventory and process-control indicators; avoid unnecessary personal data.
- **Process:** Compare capacity scenarios and risk-based audit coverage using transparent factors and human challenge.
- **Tools:** Scenario modelling and explainable aggregate analytics.
- **Illustrative sample output:** Planning option: train additional staff in records quality; audit sample gap identified in process P.
- **Risks:** Employee surveillance, biased profiling and recommendations treated as misconduct findings.
- **Controls:** No individual hiring/dismissal or productivity scoring; consult staff; auditors own sampling and findings.
- **Metrics:** Coverage gaps, plan feasibility, training outcomes and false-alert burden.
- **Implementation dependencies:** HR/audit governance, employee consultation and validated process-level data.

