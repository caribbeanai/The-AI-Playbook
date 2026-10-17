# Caribbean readiness and safeguards

[Return to government playbook](README.md)

## Design for the actual jurisdiction

The Caribbean is not one legal system, language community or procurement market. Name the country or territory, responsible institution, applicable public-sector mandate and local reviewer in every pilot. CARICOM membership does not create one uniform data-protection regime. Do not assume that EU rules automatically govern every Caribbean public service, or that a vendor's GDPR claim establishes local compliance.

Before using personal records, obtain legal advice on the processing basis, sector rules, public-record retention, freedom-of-information obligations, data-subject rights, automated decisions and cross-border transfers. For example, Jamaica's information commissioner describes eight data-protection standards, including minimisation, security and cross-border safeguards. Those Jamaican requirements must not be presented as universal Caribbean law. See [sources](sources.md).

## A localisation checklist

- **Language and dialect:** Record which languages users actually need: English and Caribbean English varieties, Jamaican Patwa, Haitian Creole, French, Spanish, Dutch, Papiamento/Papiamentu, Portuguese where relevant, and locally used Indigenous or other community languages. Do not equate an accent with literacy or capability. Test code-switching, names, place names, spelling variants and spoken numbers. Obtain native-speaker review; label unvalidated translations. Legal and emergency notices need authorised translations.
- **Small populations:** Even aggregated tables can identify a person in a village, rare occupation or small island. Use disclosure review, appropriate suppression and access controls. Do not assume removing names anonymises data. Test whether a model memorises records or exposes small groups.
- **Connectivity and devices:** Provide light text pages, printable material and a staffed telephone or counter route. Test on older phones and interrupted connections. Cache approved public content with version and expiry dates. Never cache confidential records on shared devices. Store-and-forward workflows need encryption, conflict handling and clear status receipts.
- **Hurricanes and continuity:** Rehearse power loss, telecoms interruption, a vendor outage and loss of a key staff member. Maintain offline operating procedures and restore tests. AI-generated summaries never override meteorological or emergency-management authorities. Predetermine who can suspend the system and communicate a fallback.
- **Accessibility:** Use WCAG 2.2 as a testable design reference, alongside applicable local requirements and direct testing with disabled users. Check keyboard operation, screen-reader reading order, form errors, contrast, captions and text resizing. Offer accessible alternatives to CAPTCHA, voice-only and smartphone-only processes.
- **Local costs:** Budget in the agency's operating currency and include foreign-exchange exposure, taxes, procurement effort, connectivity, integration, staff review, evaluation, translation, storage, support, incident response and exit. A low token price is not a low service cost.
- **Small teams:** Assign a service owner, data steward, security contact, frontline reviewer and escalation authority. Roles may be shared, but approvals and conflicts must remain clear. A regional shared service can pool expertise only with suitable agreements, access boundaries and lawful data transfer.
- **Data gaps:** Check paper records, missing addresses, informal employment, multiple islands, seasonal migration and uneven sensor coverage. Treat missing data as unknown, not zero. Track who is absent from the training and evaluation records.

## Data and tool rules

Begin with public or synthetic data. An agency-approved environment is required before introducing restricted data. Keep prompts and outputs subject to the same classification as source records. Contracts must identify hosting locations, subprocessors, retention, deletion, model-training use, support access, incident notification and exit arrangements. An in-region endpoint alone does not establish residency: logs, backups, support and subprocessors also matter.

Use the least privilege needed. Separate test from production; avoid bulk exports where a scoped retrieval interface will work. Do not paste citizen, patient, child, employee, tax or immigration records into a consumer AI service. Define a retention schedule with the records officer rather than automatically storing every prompt forever.

For retrieval-based assistants, allow only approved, versioned sources; return the document title, effective date and passage used. Make abstention a valid output. Treat instructions inside uploaded files, emails and webpages as untrusted content. Do not let retrieved text grant tool permissions or change system policy. Keep external actions behind a narrow allowlist and approval gate.

## Human oversight that works

Reviewers need time, training, original evidence and authority to disagree. Record what they changed and why without turning the audit log into a new uncontrolled personal-data store. Define which errors demand a pause rather than merely another review. Provide citizens with a human contact and correction or appeal path appropriate to the service. Never claim that oversight removes the need for legal authority or evaluation.

## Evaluation and go/no-go

Agree numerical thresholds before testing; the catalogue's metrics are candidates, not universal target values. Use held-out, locally representative cases and an honest baseline such as current staff practice, a checklist, search or a seasonal average. Measure both benefit and harm: unsupported claims, incorrect routing, missed urgent cases, unfair variation, time spent reviewing, cost per completed service and failures during outages.

Report results by relevant language, island or service channel where lawful and statistically meaningful. Small samples need confidence intervals and qualitative review, not sweeping fairness claims. Separate training and test periods for forecasts, prevent future-data leakage and include abnormal seasons. Require specialist review for health, emergency, infrastructure and justice applications.

Before release, record version, dataset period, evaluation result, approved use, prohibited use, monitoring owner, incident route, rollback procedure and next review date. Re-evaluate after model, prompt, corpus, policy, vendor or integration changes. Stop if sources become stale, a serious incident occurs, performance crosses a defined limit, or the human fallback cannot cope.
