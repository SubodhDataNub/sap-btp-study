# 00 — SAP BTP Documentation Map

> **What this is:** a map of the 2,065 pages in `btp-cloud-platform/docs/`, grouped into 21 topic clusters (plus one cross-cutting cluster that has no section of its own).
>
> **How it was built:** from the repo's own table of contents (`docs/index.md`), file names and first headings only. No page bodies were read yet.
>
> **Repo snapshot:** last upstream sync 2026-10-12 ("Update from SAP DITA CCMS"). Each `.md` file corresponds to a page on help.sap.com/docs/btp.
>
> **Counting rule:** every page is counted in exactly one cluster (the most specific TOC branch it sits under), so the cluster counts add up to 2,065.

All links below are relative to this file and point into `../btp-cloud-platform/docs/`.

---

## The big picture in one table

| # | Cluster | Pages | Relevance to you* |
|---|---|---:|---|
| **A** | **Platform foundations** | | |
| 01 | Platform overview & glossary | 16 | ★★★ |
| 02 | Account model & regions | 9 | ★★★ |
| 03 | Entitlements, commercial models & billing | 17 | ★★★ |
| 04 | Account administration in the cockpit | 33 | ★★★ |
| **B** | **Cloud Foundry runtime** | | |
| 05 | Cloud Foundry environment basics & getting started | 17 | ★★★ |
| 06 | Services in Cloud Foundry (instances, bindings, keys) | 20 | ★★★ |
| 07 | Runtimes & buildpacks (Node.js, Python, Java) | 58 | ★★ (Node/Python ★★★, Java ★) |
| 12 | CF org/space administration & the `cf` CLI | 51 | ★★★ |
| 13 | CF application operations, logs & audit logging | 33 | ★★ |
| **C** | **Building and shipping apps** | | |
| 16 | Dev tools & programming models (BAS, CAP, HANA) | 10 | ★★★ (but thin, see gaps) |
| 08 | UI: HTML5 Application Repository & App Router | 56 | ★★★ |
| 09 | Application security (XSUAA in your app) | 26 | ★★★ |
| 10 | Multitenant (SaaS) applications | 12 | ★★ |
| 11 | MTA deployment & CI/CD | 64 | ★★★ |
| **D** | **Security & identity (platform level)** | | |
| 14 | XSUAA service, role collections, IdP trust, users | 139 | ★★★ (core) / ★ (deep reference) |
| **E** | **Automation & tooling** | | |
| 15 | btp CLI, management APIs, MCP, Infrastructure as Code | 53 | ★★★ (btp CLI) / ★★ (APIs) |
| **F** | **Connectivity & destinations** (cross-cutting, no own section) | *(scattered)* | ★★★ but **mostly NOT in this repo** |
| **G** | **Extensions & integrations** | | |
| 17 | Extending S/4HANA Cloud, SuccessFactors; formations; system registration | 84 | ★★ |
| **H** | **Other environments** | | |
| 18 | Kyma (Kubernetes) environment | 234 | ★ |
| 19 | ABAP environment | 1,111 | ★ |
| 20 | Neo environment | 13 | Awareness only (legacy) |
| **I** | **Support** | | |
| 21 | Support, operating model, platform updates | 9 | ★ |
| | **Total** | **2,065** | |

\* ★★★ = core to a CAP + Fiori + Node.js developer on Cloud Foundry; ★★ = useful soon; ★ = awareness or reference.

**Key takeaway:** more than half the repo (1,111 pages, 54%) is about the **ABAP environment**, and another 234 pages are about **Kyma**. Only about **700 pages** are relevant to your role, and the curriculum will focus on those.

---

## A. Platform foundations

### 01 · Platform overview & glossary — 16 pages
Landing pages for each documentation section, the "what is BTP" page, the glossary, and the tools and programming-models overview.
- [sap-business-technology-platform-6a2c1ab.md](../btp-cloud-platform/docs/sap-business-technology-platform-6a2c1ab.md): what BTP is
- [10-concepts/basic-platform-concepts-73beb06.md](../btp-cloud-platform/docs/10-concepts/basic-platform-concepts-73beb06.md)
- [10-concepts/solutions-and-services-7613d9c.md](../btp-cloud-platform/docs/10-concepts/solutions-and-services-7613d9c.md)
- [10-concepts/environments-15547f7.md](../btp-cloud-platform/docs/10-concepts/environments-15547f7.md): CF vs Kyma vs ABAP vs Neo
- [10-concepts/tools-programming-models-programming-languages-and-apis-9b15170.md](../btp-cloud-platform/docs/10-concepts/tools-programming-models-programming-languages-and-apis-9b15170.md) and its children `tools-abcae5b.md`, `programming-models-042061d.md`, `programming-languages-730d82d.md`, `apis-d1d1107.md`
- [glossary-e67a143.md](../btp-cloud-platform/docs/glossary-e67a143.md)

### 02 · Account model & regions — 9 pages
Global account → directories → subaccounts, trial vs enterprise, regions and API endpoints, HA/DR.
- [10-concepts/account-model-8ed4a70.md](../btp-cloud-platform/docs/10-concepts/account-model-8ed4a70.md)
- [10-concepts/trial-accounts-and-free-tier-046f127.md](../btp-cloud-platform/docs/10-concepts/trial-accounts-and-free-tier-046f127.md)
- [10-concepts/enterprise-accounts-171511c.md](../btp-cloud-platform/docs/10-concepts/enterprise-accounts-171511c.md)
- [10-concepts/regions-350356d.md](../btp-cloud-platform/docs/10-concepts/regions-350356d.md)
- [10-concepts/regions-and-api-endpoints-available-for-the-cloud-foundry-environment-f344a57.md](../btp-cloud-platform/docs/10-concepts/regions-and-api-endpoints-available-for-the-cloud-foundry-environment-f344a57.md)
- [10-concepts/resilience-high-availability-and-disaster-recovery-e3ac4f7.md](../btp-cloud-platform/docs/10-concepts/resilience-high-availability-and-disaster-recovery-e3ac4f7.md)
- [20-getting-started/getting-a-global-account-d61c281.md](../btp-cloud-platform/docs/20-getting-started/getting-a-global-account-d61c281.md)

### 03 · Entitlements, commercial models & billing — 17 pages
Entitlements vs quotas, consumption-based vs subscription-based models, free service plans, metering, usage and cost monitoring, budgets.
- [10-concepts/entitlements-and-quotas-00aa2c2.md](../btp-cloud-platform/docs/10-concepts/entitlements-and-quotas-00aa2c2.md)
- [10-concepts/commercial-models-263d400.md](../btp-cloud-platform/docs/10-concepts/commercial-models-263d400.md)
- [10-concepts/what-is-the-consumption-based-commercial-model-7047eb4.md](../btp-cloud-platform/docs/10-concepts/what-is-the-consumption-based-commercial-model-7047eb4.md)
- [10-concepts/what-is-the-subscription-based-commercial-model-239b6e0.md](../btp-cloud-platform/docs/10-concepts/what-is-the-subscription-based-commercial-model-239b6e0.md)
- [10-concepts/using-free-service-plans-524e108.md](../btp-cloud-platform/docs/10-concepts/using-free-service-plans-524e108.md)
- [10-concepts/service-plans-and-metering-for-cloud-foundry-runtime-8d41fa4.md](../btp-cloud-platform/docs/10-concepts/service-plans-and-metering-for-cloud-foundry-runtime-8d41fa4.md)
- [50-administration-and-ops/managing-entitlements-and-quotas-using-the-cockpit-c824874.md](../btp-cloud-platform/docs/50-administration-and-ops/managing-entitlements-and-quotas-using-the-cockpit-c824874.md)
- [50-administration-and-ops/monitoring-usage-and-consumption-costs-in-your-global-account-de6f0db.md](../btp-cloud-platform/docs/50-administration-and-ops/monitoring-usage-and-consumption-costs-in-your-global-account-de6f0db.md)

### 04 · Account administration in the cockpit — 33 pages
Cockpit navigation, managing global accounts, directories and subaccounts, enabling environments, Joule in the cockpit.
- [50-administration-and-ops/account-administration-in-the-cockpit-8061ecc.md](../btp-cloud-platform/docs/50-administration-and-ops/account-administration-in-the-cockpit-8061ecc.md)
- [50-administration-and-ops/navigate-in-the-cockpit-0874895.md](../btp-cloud-platform/docs/50-administration-and-ops/navigate-in-the-cockpit-0874895.md)
- [50-administration-and-ops/managing-global-accounts-using-the-cockpit-667f34b.md](../btp-cloud-platform/docs/50-administration-and-ops/managing-global-accounts-using-the-cockpit-667f34b.md)
- [50-administration-and-ops/managing-directories-using-the-cockpit-f495ac1.md](../btp-cloud-platform/docs/50-administration-and-ops/managing-directories-using-the-cockpit-f495ac1.md)
- [50-administration-and-ops/managing-subaccounts-using-the-cockpit-55d0b6d.md](../btp-cloud-platform/docs/50-administration-and-ops/managing-subaccounts-using-the-cockpit-55d0b6d.md)
- [50-administration-and-ops/create-a-subaccount-05280a1.md](../btp-cloud-platform/docs/50-administration-and-ops/create-a-subaccount-05280a1.md)
- [50-administration-and-ops/enable-environment-or-create-environment-instance-78c14b6.md](../btp-cloud-platform/docs/50-administration-and-ops/enable-environment-or-create-environment-instance-78c14b6.md)
- [50-administration-and-ops/account-administration-using-joule-in-the-cockpit-3d7626b.md](../btp-cloud-platform/docs/50-administration-and-ops/account-administration-using-joule-in-the-cockpit-3d7626b.md): AI assistant (6 pages)

---

## B. Cloud Foundry runtime (your main environment)

### 05 · Cloud Foundry environment basics & getting started — 17 pages
What CF on BTP is, supported and unsupported CF features, BTP-specific configuration, availability zones, trial and enterprise setup, your first app.
- [10-concepts/cloud-foundry-environment-9c7092c.md](../btp-cloud-platform/docs/10-concepts/cloud-foundry-environment-9c7092c.md)
- [10-concepts/supported-and-unsupported-cloud-foundry-features-f8a351c.md](../btp-cloud-platform/docs/10-concepts/supported-and-unsupported-cloud-foundry-features-f8a351c.md)
- [10-concepts/sap-btp-specific-configurations-9809fa4.md](../btp-cloud-platform/docs/10-concepts/sap-btp-specific-configurations-9809fa4.md)
- [20-getting-started/getting-started-with-a-trial-account-in-the-cloud-foundry-environment-e50ab7b.md](../btp-cloud-platform/docs/20-getting-started/getting-started-with-a-trial-account-in-the-cloud-foundry-environment-e50ab7b.md)
- [20-getting-started/setting-up-your-trial-account-fa5deb9.md](../btp-cloud-platform/docs/20-getting-started/setting-up-your-trial-account-fa5deb9.md)
- [20-getting-started/setting-up-a-trial-account-from-the-command-line-a21360f.md](../btp-cloud-platform/docs/20-getting-started/setting-up-a-trial-account-from-the-command-line-a21360f.md)
- [30-development/developing-your-first-application-bc8d5c0.md](../btp-cloud-platform/docs/30-development/developing-your-first-application-bc8d5c0.md)
- [30-development/best-practices-0859096.md](../btp-cloud-platform/docs/30-development/best-practices-0859096.md)

### 06 · Services in Cloud Foundry — 20 pages
Service instances, user-provided services, bindings, service keys, update and delete (each with cockpit and CLI variants), boosters.
- [30-development/using-services-in-the-cloud-foundry-environment-f22029f.md](../btp-cloud-platform/docs/30-development/using-services-in-the-cloud-foundry-environment-f22029f.md)
- [30-development/about-services-d1d0fc8.md](../btp-cloud-platform/docs/30-development/about-services-d1d0fc8.md)
- [30-development/creating-service-instances-8221b74.md](../btp-cloud-platform/docs/30-development/creating-service-instances-8221b74.md)
- [30-development/binding-service-instances-to-applications-e98280a.md](../btp-cloud-platform/docs/30-development/binding-service-instances-to-applications-e98280a.md)
- [30-development/creating-service-keys-4514a14.md](../btp-cloud-platform/docs/30-development/creating-service-keys-4514a14.md)
- [30-development/creating-user-provided-service-instances-a44355e.md](../btp-cloud-platform/docs/30-development/creating-user-provided-service-instances-a44355e.md)
- [30-development/boosters-fb1b561.md](../btp-cloud-platform/docs/30-development/boosters-fb1b561.md)

### 07 · Runtimes & buildpacks — 58 pages
50 of the 58 pages are about the SAP Java buildpack. Node.js and Python have 3 pages each.
- [30-development/development-languages-2d0ff22.md](../btp-cloud-platform/docs/30-development/development-languages-2d0ff22.md)
- [30-development/developing-node-js-in-the-cloud-foundry-environment-3a7a0be.md](../btp-cloud-platform/docs/30-development/developing-node-js-in-the-cloud-foundry-environment-3a7a0be.md) + [tips-and-tricks-for-node-js-applications-3a5fe88.md](../btp-cloud-platform/docs/30-development/tips-and-tricks-for-node-js-applications-3a5fe88.md) + [node-js-buildpack-troubleshooting-1462ff0.md](../btp-cloud-platform/docs/30-development/node-js-buildpack-troubleshooting-1462ff0.md)
- [30-development/developing-python-in-the-cloud-foundry-environment-acf8f49.md](../btp-cloud-platform/docs/30-development/developing-python-in-the-cloud-foundry-environment-acf8f49.md)
- [30-development/developing-java-in-the-cloud-foundry-environment-a3f9006.md](../btp-cloud-platform/docs/30-development/developing-java-in-the-cloud-foundry-environment-a3f9006.md): reference only for you
- [30-development/connect-an-application-to-postgresql-via-tls-certificate-a04a06d.md](../btp-cloud-platform/docs/30-development/connect-an-application-to-postgresql-via-tls-certificate-a04a06d.md): the **only** PostgreSQL page in the repo (Java-oriented)

### 12 · CF org/space administration & the `cf` CLI — 51 pages
Orgs, spaces, members, CF roles, space quotas, installing and logging in with the `cf` CLI, CLI plug-ins (including the MTA plug-in).
- [50-administration-and-ops/about-roles-in-the-cloud-foundry-environment-0907638.md](../btp-cloud-platform/docs/50-administration-and-ops/about-roles-in-the-cloud-foundry-environment-0907638.md)
- [50-administration-and-ops/about-user-management-in-the-cloud-foundry-environment-8e6ce96.md](../btp-cloud-platform/docs/50-administration-and-ops/about-user-management-in-the-cloud-foundry-environment-8e6ce96.md)
- [50-administration-and-ops/org-administration-using-the-cockpit-c4c25cc.md](../btp-cloud-platform/docs/50-administration-and-ops/org-administration-using-the-cockpit-c4c25cc.md)
- [50-administration-and-ops/org-administration-using-the-cloud-foundry-cli-927377f.md](../btp-cloud-platform/docs/50-administration-and-ops/org-administration-using-the-cloud-foundry-cli-927377f.md)
- [50-administration-and-ops/download-and-install-the-cloud-foundry-command-line-interface-4ef907a.md](../btp-cloud-platform/docs/50-administration-and-ops/download-and-install-the-cloud-foundry-command-line-interface-4ef907a.md)
- [50-administration-and-ops/log-on-to-the-cloud-foundry-environment-using-the-cloud-foundry-command-line-interface-7a37d66.md](../btp-cloud-platform/docs/50-administration-and-ops/log-on-to-the-cloud-foundry-environment-using-the-cloud-foundry-command-line-interface-7a37d66.md)
- [50-administration-and-ops/cf-cli-plug-ins-dc28ce3.md](../btp-cloud-platform/docs/50-administration-and-ops/cf-cli-plug-ins-dc28ce3.md) (15 pages)
- [50-administration-and-ops/managing-space-quotas-4e5f0ee.md](../btp-cloud-platform/docs/50-administration-and-ops/managing-space-quotas-4e5f0ee.md)

### 13 · CF application operations, logs & audit — 33 pages
Environment variables, start/stop/restage, scaling instances, routes and custom domains, security groups, troubleshooting, audit logging.
- [50-administration-and-ops/application-operations-in-the-cloud-foundry-environment-0f1286a.md](../btp-cloud-platform/docs/50-administration-and-ops/application-operations-in-the-cloud-foundry-environment-0f1286a.md)
- [50-administration-and-ops/manage-environment-variables-9984a29.md](../btp-cloud-platform/docs/50-administration-and-ops/manage-environment-variables-9984a29.md)
- [50-administration-and-ops/restage-an-application-26255c4.md](../btp-cloud-platform/docs/50-administration-and-ops/restage-an-application-26255c4.md)
- [50-administration-and-ops/troubleshoot-applications-2ae6772.md](../btp-cloud-platform/docs/50-administration-and-ops/troubleshoot-applications-2ae6772.md)
- [50-administration-and-ops/about-routes-in-the-cockpit-4af288c.md](../btp-cloud-platform/docs/50-administration-and-ops/about-routes-in-the-cockpit-4af288c.md)
- [50-administration-and-ops/audit-logging-in-the-cloud-foundry-environment-f92c86a.md](../btp-cloud-platform/docs/50-administration-and-ops/audit-logging-in-the-cloud-foundry-environment-f92c86a.md) (16 pages)

---

## C. Building and shipping apps

### 16 · Dev tools & programming models (BAS, CAP, HANA) — 10 pages
**Thin in this repo.** These are mostly overview pages that point out to other SAP documentation sets (see the gaps section).
- [30-development/sap-business-application-studio-c736960.md](../btp-cloud-platform/docs/30-development/sap-business-application-studio-c736960.md)
- [30-development/developing-with-the-sap-cloud-application-programming-model-00823f9.md](../btp-cloud-platform/docs/30-development/developing-with-the-sap-cloud-application-programming-model-00823f9.md)
- [30-development/developing-business-applications-using-node-js-29c25e5.md](../btp-cloud-platform/docs/30-development/developing-business-applications-using-node-js-29c25e5.md)
- [30-development/core-data-services-cds-language-reference-documentation-855e00b.md](../btp-cloud-platform/docs/30-development/core-data-services-cds-language-reference-documentation-855e00b.md)
- [30-development/business-application-pattern-a1de162.md](../btp-cloud-platform/docs/30-development/business-application-pattern-a1de162.md) *(counted in cluster 05)*
- [30-development/developing-sap-hana-in-the-cloud-foundry-environment-14224d7.md](../btp-cloud-platform/docs/30-development/developing-sap-hana-in-the-cloud-foundry-environment-14224d7.md)
- [30-development/consuming-apis-d4cae3e.md](../btp-cloud-platform/docs/30-development/consuming-apis-d4cae3e.md)
- Related, but filed under the ABAP environment: [30-development/develop-an-sap-fiori-application-and-deploy-it-to-cloud-foundry-using-sap-business-applic-2498cbf.md](../btp-cloud-platform/docs/30-development/develop-an-sap-fiori-application-and-deploy-it-to-cloud-foundry-using-sap-business-applic-2498cbf.md)

### 08 · UI: HTML5 Application Repository & App Router — 56 pages
How Fiori/UI5 apps are stored (HTML5 Application Repository) and served (standalone App Router or managed App Router), `xs-app.json` routing, destinations, environment variables, extending the App Router.
- [30-development/developing-html5-applications-in-the-cloud-foundry-environment-11d77aa.md](../btp-cloud-platform/docs/30-development/developing-html5-applications-in-the-cloud-foundry-environment-11d77aa.md)
- [30-development/html5-application-repository-f8520f5.md](../btp-cloud-platform/docs/30-development/html5-application-repository-f8520f5.md) (14 pages)
- [30-development/application-router-01c5f9b.md](../btp-cloud-platform/docs/30-development/application-router-01c5f9b.md) (35 pages)
- [30-development/routing-configuration-file-c103fb4.md](../btp-cloud-platform/docs/30-development/routing-configuration-file-c103fb4.md): `xs-app.json` (15 pages)
- [30-development/application-routes-and-destinations-3cc788e.md](../btp-cloud-platform/docs/30-development/application-routes-and-destinations-3cc788e.md)
- [30-development/managed-application-router-589a239.md](../btp-cloud-platform/docs/30-development/managed-application-router-589a239.md)
- [30-development/developing-sapui5-839cb81.md](../btp-cloud-platform/docs/30-development/developing-sapui5-839cb81.md)

### 09 · Application security (XSUAA in your app) — 26 pages
`xs-security.json`, scopes, role templates, protecting apps, token handling, principal propagation between apps, mTLS, instance-based authorizations.
- [30-development/adding-authentication-and-authorization-419ae2e.md](../btp-cloud-platform/docs/30-development/adding-authentication-and-authorization-419ae2e.md)
- [30-development/protecting-your-application-7c5c565.md](../btp-cloud-platform/docs/30-development/protecting-your-application-7c5c565.md)
- [30-development/using-an-application-security-descriptor-file-0a69484.md](../btp-cloud-platform/docs/30-development/using-an-application-security-descriptor-file-0a69484.md): `xs-security.json`
- [30-development/reference-information-f90961d.md](../btp-cloud-platform/docs/30-development/reference-information-f90961d.md): syntax reference (3 pages)
- [30-development/create-role-collections-with-predefined-roles-fe75054.md](../btp-cloud-platform/docs/30-development/create-role-collections-with-predefined-roles-fe75054.md)
- [30-development/best-practices-when-handling-access-tokens-8d39ef3.md](../btp-cloud-platform/docs/30-development/best-practices-when-handling-access-tokens-8d39ef3.md)
- [30-development/tutorials-for-the-sap-authorization-and-trust-management-service-902ae80.md](../btp-cloud-platform/docs/30-development/tutorials-for-the-sap-authorization-and-trust-management-service-902ae80.md)

### 10 · Multitenant (SaaS) applications — 12 pages
Provider and subscriber model, SaaS Provisioning service, subscribing in the cockpit.
- [30-development/developing-multitenant-applications-in-the-cloud-foundry-environment-5e8a2b7.md](../btp-cloud-platform/docs/30-development/developing-multitenant-applications-in-the-cloud-foundry-environment-5e8a2b7.md)
- [30-development/register-the-multitenant-application-to-the-sap-saas-provisioning-service-3971151.md](../btp-cloud-platform/docs/30-development/register-the-multitenant-application-to-the-sap-saas-provisioning-service-3971151.md)
- [50-administration-and-ops/subscribe-to-multitenant-applications-using-the-cockpit-7a3e396.md](../btp-cloud-platform/docs/50-administration-and-ops/subscribe-to-multitenant-applications-using-the-cockpit-7a3e396.md)

### 11 · MTA deployment & CI/CD — 64 pages
The largest CF-developer cluster: `mta.yaml` (modules, resources, parameters, properties), `.mtar` archives, extension descriptors (`.mtaext`), blue-green deployment, the deploy service, plus two CI/CD overview pages.
- [30-development/multitarget-applications-in-the-cloud-foundry-environment-d04fc0e.md](../btp-cloud-platform/docs/30-development/multitarget-applications-in-the-cloud-foundry-environment-d04fc0e.md) (59 pages)
- [30-development/getting-started-0ce9938.md](../btp-cloud-platform/docs/30-development/getting-started-0ce9938.md): MTA getting started
- [30-development/defining-multitarget-application-deployment-descriptors-for-cloud-foundry-f48880b.md](../btp-cloud-platform/docs/30-development/defining-multitarget-application-deployment-descriptors-for-cloud-foundry-f48880b.md)
- [30-development/multitarget-application-structure-f443b9f.md](../btp-cloud-platform/docs/30-development/multitarget-application-structure-f443b9f.md): modules, resources, parameters (7 pages)
- [30-development/list-of-supported-mta-parameters-6aa426e.md](../btp-cloud-platform/docs/30-development/list-of-supported-mta-parameters-6aa426e.md)
- [30-development/mta-deployment-descriptor-examples-66a7033.md](../btp-cloud-platform/docs/30-development/mta-deployment-descriptor-examples-66a7033.md)
- [30-development/defining-mta-extension-descriptors-50df803.md](../btp-cloud-platform/docs/30-development/defining-mta-extension-descriptors-50df803.md)
- [30-development/blue-green-deployment-of-multitarget-applications-772ab72.md](../btp-cloud-platform/docs/30-development/blue-green-deployment-of-multitarget-applications-772ab72.md)
- [30-development/frequently-asked-questions-6062ecc.md](../btp-cloud-platform/docs/30-development/frequently-asked-questions-6062ecc.md) / [mta-operation-failure-f3e97ff.md](../btp-cloud-platform/docs/30-development/mta-operation-failure-f3e97ff.md)
- [10-concepts/continuous-integration-and-delivery-ci-cd-fe74df5.md](../btp-cloud-platform/docs/10-concepts/continuous-integration-and-delivery-ci-cd-fe74df5.md) + [30-development/continuous-integration-and-delivery-fdead30.md](../btp-cloud-platform/docs/30-development/continuous-integration-and-delivery-fdead30.md)

---

## D. Security & identity (platform level)

### 14 · XSUAA service, role collections, IdP trust, users — 139 pages
Roughly: Security Administration 79 (IdP trust 36, role collections 12, building roles for apps 9, XSUAA secrets 13, users 6), XSUAA service reference 44 (31 of them monitoring and troubleshooting), principal propagation 4, data protection and privacy 8, plus concept pages.
- [10-concepts/introduction-to-identity-and-access-management-on-sap-btp-51c1677.md](../btp-cloud-platform/docs/10-concepts/introduction-to-identity-and-access-management-on-sap-btp-51c1677.md): **start here**
- [10-concepts/platform-users-4401316.md](../btp-cloud-platform/docs/10-concepts/platform-users-4401316.md) / [10-concepts/business-users-2e68494.md](../btp-cloud-platform/docs/10-concepts/business-users-2e68494.md)
- [60-security/what-is-the-sap-authorization-and-trust-management-service-649961f.md](../btp-cloud-platform/docs/60-security/what-is-the-sap-authorization-and-trust-management-service-649961f.md)
- [60-security/authorization-entities-5d8ed75.md](../btp-cloud-platform/docs/60-security/authorization-entities-5d8ed75.md): scopes → roles → role collections
- [60-security/default-role-collections-of-sap-btp-a6a0072.md](../btp-cloud-platform/docs/60-security/default-role-collections-of-sap-btp-a6a0072.md)
- [50-administration-and-ops/working-with-role-collections-393ea0b.md](../btp-cloud-platform/docs/50-administration-and-ops/working-with-role-collections-393ea0b.md)
- [50-administration-and-ops/building-roles-and-role-collections-for-applications-eaa6a26.md](../btp-cloud-platform/docs/50-administration-and-ops/building-roles-and-role-collections-for-applications-eaa6a26.md)
- [50-administration-and-ops/trust-and-federation-with-identity-providers-cb1bc8f.md](../btp-cloud-platform/docs/50-administration-and-ops/trust-and-federation-with-identity-providers-cb1bc8f.md)
- [50-administration-and-ops/default-identity-provider-d6a8db7.md](../btp-cloud-platform/docs/50-administration-and-ops/default-identity-provider-d6a8db7.md)
- [60-security/security-recommendations-for-sap-authorization-and-trust-management-service-0578b80.md](../btp-cloud-platform/docs/60-security/security-recommendations-for-sap-authorization-and-trust-management-service-0578b80.md)
- [60-security/monitoring-and-troubleshooting-1b3e89e.md](../btp-cloud-platform/docs/60-security/monitoring-and-troubleshooting-1b3e89e.md): error catalogue (31 pages)

---

## E. Automation & tooling

### 15 · btp CLI, management APIs, MCP, Infrastructure as Code — 53 pages
- [10-concepts/cloud-management-tools-caf4e4e.md](../btp-cloud-platform/docs/10-concepts/cloud-management-tools-caf4e4e.md): cockpit vs btp CLI vs APIs vs Terraform
- [50-administration-and-ops/account-administration-using-the-sap-btp-command-line-interface-btp-cli-7c6df2d.md](../btp-cloud-platform/docs/50-administration-and-ops/account-administration-using-the-sap-btp-command-line-interface-btp-cli-7c6df2d.md) (33 pages)
- [50-administration-and-ops/download-and-start-using-the-btp-cli-client-8a8f17f.md](../btp-cloud-platform/docs/50-administration-and-ops/download-and-start-using-the-btp-cli-client-8a8f17f.md)
- [50-administration-and-ops/command-syntax-of-the-btp-cli-69606f4.md](../btp-cloud-platform/docs/50-administration-and-ops/command-syntax-of-the-btp-cli-69606f4.md)
- [50-administration-and-ops/how-to-work-with-the-btp-cli-11d9f67.md](../btp-cloud-platform/docs/50-administration-and-ops/how-to-work-with-the-btp-cli-11d9f67.md) / [commands-in-the-btp-cli-a03a555.md](../btp-cloud-platform/docs/50-administration-and-ops/commands-in-the-btp-cli-a03a555.md)
- [50-administration-and-ops/account-administration-using-apis-1c8db14.md](../btp-cloud-platform/docs/50-administration-and-ops/account-administration-using-apis-1c8db14.md): Cloud Management service, Service Manager, usage APIs (19 pages)
- [50-administration-and-ops/account-administration-using-mcp-servers-2d167cb.md](../btp-cloud-platform/docs/50-administration-and-ops/account-administration-using-mcp-servers-2d167cb.md): new, AI-agent administration
- [50-administration-and-ops/account-administration-using-infrastructure-as-code-8d201e4.md](../btp-cloud-platform/docs/50-administration-and-ops/account-administration-using-infrastructure-as-code-8d201e4.md): Terraform (1 page)

---

## F. Connectivity & destinations (cross-cutting): ⚠️ mostly not in this repo

There is **no Connectivity or Destination service section** in this repo. The pages that do exist are either about how the App Router consumes destinations, or are ABAP-environment-specific. The real Destination service and Cloud Connector documentation lives in a **separate SAP documentation set** (SAP BTP Connectivity), so this curriculum will cover only the parts the repo supports and tell you where the rest lives.
- [30-development/application-routes-and-destinations-3cc788e.md](../btp-cloud-platform/docs/30-development/application-routes-and-destinations-3cc788e.md): App Router → destination
- [30-development/destinations-6b303d0.md](../btp-cloud-platform/docs/30-development/destinations-6b303d0.md): the App Router `destinations` environment variable
- [30-development/automatic-creation-of-destination-configurations-be0acbf.md](../btp-cloud-platform/docs/30-development/automatic-creation-of-destination-configurations-be0acbf.md): HTML5 repo
- [30-development/sap-connectivity-apiext-4ed6d63.md](../btp-cloud-platform/docs/30-development/sap-connectivity-apiext-4ed6d63.md): Java only
- [50-administration-and-ops/integration-in-btp-apps-via-sap-destination-service-877d48c.md](../btp-cloud-platform/docs/50-administration-and-ops/integration-in-btp-apps-via-sap-destination-service-877d48c.md): ABAP context
- [30-development/integration-and-connectivity-f6c7368.md](../btp-cloud-platform/docs/30-development/integration-and-connectivity-f6c7368.md): ABAP context (130 pages), including on-premise connectivity via Cloud Connector

---

## G. Extensions & integrations

### 17 · Extensions & integrations — 84 pages
Registering SAP systems (S/4HANA Cloud, SuccessFactors) in a global account, formations, consent, and extension scenarios on CF and Kyma.
- [40-extensions/extensibility-and-integration-concepts-3ce5e05.md](../btp-cloud-platform/docs/40-extensions/extensibility-and-integration-concepts-3ce5e05.md)
- [40-extensions/adding-registering-and-deregistering-systems-2ffdaff.md](../btp-cloud-platform/docs/40-extensions/adding-registering-and-deregistering-systems-2ffdaff.md)
- [40-extensions/automating-integrations-using-formations-68b04fa.md](../btp-cloud-platform/docs/40-extensions/automating-integrations-using-formations-68b04fa.md)
- [40-extensions/extending-sap-s-4hana-cloud-in-the-cloud-foundry-and-kyma-environment-40b9e6c.md](../btp-cloud-platform/docs/40-extensions/extending-sap-s-4hana-cloud-in-the-cloud-foundry-and-kyma-environment-40b9e6c.md) (27 pages)
- [40-extensions/extending-sap-successfactors-in-the-cloud-foundry-and-kyma-environment-9e33934.md](../btp-cloud-platform/docs/40-extensions/extending-sap-successfactors-in-the-cloud-foundry-and-kyma-environment-9e33934.md) (17 pages)

---

## H. Other environments

### 18 · Kyma (Kubernetes) environment — 234 pages
Kyma modules (168 pages: API Gateway, Istio, Serverless, Eventing, Telemetry and others), kubectl access, Kyma dashboard, Kyma security.
- [10-concepts/kyma-environment-468c2f3.md](../btp-cloud-platform/docs/10-concepts/kyma-environment-468c2f3.md)
- [10-concepts/kyma-runtime-basic-concepts-4a0dd09.md](../btp-cloud-platform/docs/10-concepts/kyma-runtime-basic-concepts-4a0dd09.md)
- [20-getting-started/getting-started-in-the-kyma-environment-d1abd18.md](../btp-cloud-platform/docs/20-getting-started/getting-started-in-the-kyma-environment-d1abd18.md)
- [30-development/development-in-the-kyma-environment-606ec61.md](../btp-cloud-platform/docs/30-development/development-in-the-kyma-environment-606ec61.md)
- [70-getting-support/comparison-between-the-operating-models-of-kyma-and-cloud-foundry-runtimes-3978f94.md](../btp-cloud-platform/docs/70-getting-support/comparison-between-the-operating-models-of-kyma-and-cloud-foundry-runtimes-3978f94.md) *(counted in cluster 21)*: ⚠️ now only a "content has moved" stub; use [operating-model-9aafc94.md](../btp-cloud-platform/docs/70-getting-support/operating-model-9aafc94.md) for the CF vs Kyma responsibilities table

### 19 · ABAP environment — 1,111 pages
ABAP Cloud development (RAP, ADT for Eclipse, released objects: 253 pages), lifecycle management with gCTS and ATC, IAM, communication scenarios, 315 pages of Fiori admin apps.
- [10-concepts/abap-environment-11d6265.md](../btp-cloud-platform/docs/10-concepts/abap-environment-11d6265.md)
- [20-getting-started/getting-started-in-the-abap-environment-2ffdd24.md](../btp-cloud-platform/docs/20-getting-started/getting-started-in-the-abap-environment-2ffdd24.md)
- [30-development/development-in-the-abap-environment-31367ef.md](../btp-cloud-platform/docs/30-development/development-in-the-abap-environment-31367ef.md)
- [30-development/abap-restful-application-programming-model-33a301e.md](../btp-cloud-platform/docs/30-development/abap-restful-application-programming-model-33a301e.md)
- [50-administration-and-ops/administration-and-operations-in-the-abap-environment-c4fd102.md](../btp-cloud-platform/docs/50-administration-and-ops/administration-and-operations-in-the-abap-environment-c4fd102.md)

### 20 · Neo environment — 13 pages: **awareness only (legacy)**
SAP's original, proprietary BTP environment. The repo keeps one concept page plus Neo trust-setup and principal-propagation pages, and points to a migration guide toward the "multi-cloud foundation" (CF/Kyma/ABAP).
- [10-concepts/neo-environment-0f79436.md](../btp-cloud-platform/docs/10-concepts/neo-environment-0f79436.md): includes the "Migration from the Neo to the Multi-Cloud Foundation" section
- [20-getting-started/neo-environment-trust-setup-55d3664.md](../btp-cloud-platform/docs/20-getting-started/neo-environment-trust-setup-55d3664.md)
- [60-security/principal-propagation-from-the-neo-environment-to-the-multi-cloud-foundation-6e194f8.md](../btp-cloud-platform/docs/60-security/principal-propagation-from-the-neo-environment-to-the-multi-cloud-foundation-6e194f8.md)

---

## I. Support

### 21 · Support, operating model, platform updates — 9 pages
- [70-getting-support/getting-support-5dd7398.md](../btp-cloud-platform/docs/70-getting-support/getting-support-5dd7398.md)
- [70-getting-support/operating-model-in-the-cloud-foundry-environment-de55b6e.md](../btp-cloud-platform/docs/70-getting-support/operating-model-in-the-cloud-foundry-environment-de55b6e.md): who is responsible for what (SAP vs you)
- [70-getting-support/platform-updates-and-notifications-99070c7.md](../btp-cloud-platform/docs/70-getting-support/platform-updates-and-notifications-99070c7.md)

---

## ⚠️ Gaps: topics you need that this repo does not really cover

| Topic | What the repo has | Where the real docs live (outside this repo) |
|---|---|---|
| **Destination service & Cloud Connector** | Scattered App Router and ABAP pages (cluster F) | SAP BTP Connectivity documentation (separate help.sap.com doc set) |
| **SAP Business Application Studio** | 1 overview page + a few ABAP-context setup pages | SAP Business Application Studio documentation (separate) |
| **CAP (Cloud Application Programming Model)** | 6 pointer pages (Node.js, Java, CDS reference links) | capire, SAP's CAP documentation site |
| **Fiori elements / SAPUI5 development** | UI5 overview page, HTML5 repo and App Router hosting | SAPUI5 SDK and SAP Fiori tools documentation |
| **SAP Build Work Zone / launchpad** | Only referenced from ABAP and HTML5 pages | SAP Build Work Zone documentation |
| **SAP HANA Cloud** | 1 CF overview page + ABAP pages | SAP HANA Cloud documentation |
| **PostgreSQL on BTP** | 1 page (Java + TLS) | PostgreSQL, hyperscaler option documentation |
| **Cloud logging / Application Logging** | Audit logging only (and Kyma telemetry) | SAP Cloud Logging documentation |
| **CI/CD service in depth** | 2 overview pages | SAP Continuous Integration and Delivery documentation |
| **SAP Cloud Identity Services (IAS)** | Referenced from trust and federation pages | SAP Cloud Identity Services documentation |

In lessons, I'll teach these topics only as far as the repo supports them and say clearly where it stops.

## ⚠️ Possibly outdated or conflicting content, to verify in Phase 3

1. **Neo environment & SAP Web IDE.** About 21 files still mention Web IDE, which is a Neo-era tool succeeded by Business Application Studio, and there's a Neo-specific "Enabling SAP Web IDE Full-Stack" page. Treat as legacy.
2. **Mixed `cf` CLI versions.** Pages under development and admin mention `cf6` (~40 times), `cf7` (~42) and `cf8` (~51). Some commands and flags changed between CLI versions, so I'll check which version each lesson's commands assume.
3. **Two blue-green approaches.** `legacy-blue-green-deployment-764308c.md` sits next to the current blue-green MTA deployment pages, and there's also an "(Experimental) Rollback" page. I'll check which one is recommended.
4. **"SAP HANA Service" support page** (`70-getting-support/providing-details-for-sap-hana-service-database-problems-75cde53.md`). This likely refers to the older SAP HANA Service rather than SAP HANA Cloud. To verify.
5. **Duplicate CI/CD overviews.** There's one in `10-concepts` and one in `30-development`; I'll check whether they agree.
6. **Explicitly deprecated pages** (headings say so): Kyma "Function Runtime Deprecation Schedule", ABAP "Create a Communication Arrangement for Cloud Connector Integration (Deprecated)", "Custom Logic (Deprecated)", "Manage Security Audit Log (Deprecated)", "(Deprecated) Test Integration (SAP_COM_0510)".
7. **Same title, different context.** Several pages share a title, such as "Create a Destination" (×2), "Troubleshooting" (×many) and "Best Practices" (×2). Each lesson will link the exact file to avoid confusion.
8. **CF vs Kyma comparison page is now a stub.** `comparison-between-the-operating-models-of-kyma-and-cloud-foundry-runtimes-3978f94.md` only says "content has moved"; the real content is in `operating-model-9aafc94.md`.
9. **Old PostgreSQL example in the MTA docs.** `30-development/resources-9e34487.md` shows service plan `v9.6-dev` (PostgreSQL 9.6 is long out of support), and the same page marks the `org.postgresql` resource type as deprecated.
10. **Backing-service list may be dated.** `30-development/business-application-pattern-a1de162.md` lists MongoDB, Redis and RabbitMQ as platform backing services. Verify against SAP Discovery Center. `developing-sap-hana-in-the-cloud-foundry-environment-14224d7.md` also still links a modeling guide written for SAP Web IDE.
11. **Comparison questions aren't covered.** There's no page comparing BTP with AWS/Azure/GCP, HANA Cloud with PostgreSQL, or "when to use CF vs Kyma vs ABAP". The facts are spread across pages and the syllabus pulls them together in capstone module M18.
12. **Java 7/8 statement.** `10-concepts/prerequisites-and-restrictions-e6ddaef.md` says the SAP BTP Tools for Java were tested with Java 7 and Java 8. That's outdated (found in M01).
13. **Region vs data centre.** `10-concepts/basic-platform-concepts-73beb06.md` equates a region with "one data center", but `regions-350356d.md` says a region can contain several data centres. Also, the Neo sunset date (31 Dec 2028) is stated in Basic Platform Concepts but not on the Neo Environment page (found in M01).
