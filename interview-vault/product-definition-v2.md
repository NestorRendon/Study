# Product Definition v2 — post-pivot

*Written as founder/PO. This supersedes the original brief. Two things I'm pushing back on are flagged in §13; everything else executes your decisions.*

---

## 1. What changed

| | v1 | v2 |
|---|---|---|
| Category | "Wellbeing companion that also plans" | **Thought-capture tool with a companion as the interface** |
| Primary job | Convert distress to eustress | Get scattered input out of your head and get it back organized |
| Wedge | Undefined / everything | Gen Z + Millennials with high input load (broad product, narrow launch beachhead) |
| Failure mechanic | Death after 30 days | Dormancy & reunion — nothing is ever lost |
| Growth driver | Streaks / consequence | Cumulative captures — growth never regresses |
| AI | On-device SLM + federated learning | Server-side, small model. Privacy via policy, not architecture (for now) |
| Platform | Web-first | Flutter: mobile-first, desktop for capture, web as demo only |
| Knowledge graph | Core feature | Invisible plumbing. Never shipped as a UI |
| Persuasion model | "Subliminal" nudging | **Removed entirely.** Classic, transparent game mechanics |

---

## 2. Positioning

**One-liner:** A companion that eats your scattered thoughts and hands them back organized.

**The competitive frame you now own:** Obsidian and Apple Notes make you do the filing. Notion makes you build the system before you can use it. Finch has no notes at all. You are the only one where **the user never files anything and can still find everything.**

Say this, not "productivity app" and not "mental health app":
> "It's where I dump everything — ideas, tasks, half-thoughts — and it sorts itself out."

**What we sell:** relief from the organizing tax.
**What we never sell:** therapy, self-improvement, or optimization.

---

## 3. Who it's for

**Product audience (your definition, accepted):** Gen Z + Millennials whose daily information load exceeds their organizing capacity — university students, tech-adjacent creatives, multi-project workers. Use cases span work projects, a talk to prepare, a trip to plan, a concert, groceries, a running list of ideas.

**Launch beachhead (this is the one narrowing I insist on):** university students + early-career creatives, LatAm, ages 18–26.

The product serves everyone above. But **marketing cannot address everyone**, and this cohort is the cheapest to reach (campus, TikTok, Discord), the most aesthetically motivated, and the most vocal. Broaden the marketing message only after the beachhead cohort clears the D30 target in §11.

---

## 4. The core loop

Target: **under 60 seconds**, and it must feel like less.

1. **Open.** Pepe wakes. Once per day (first open only), a three-option mood check.
2. **Feed.** One free-text or voice dump. No title, no tag, no folder, no category. Zero structural decisions.
3. **Digest.** Pepe visibly "chews," then files it and says something short and warm. Any date, task, or person mentioned is extracted silently.
4. **React.** The room changes — a note lands on the desk, a book appears on the shelf, the calendar ticks.
5. **Resurface.** Once a day, Pepe brings back **one** thing: a forgotten idea, a task now due, or a connection between two notes you made weeks apart.

**Step 5 is the product.** Steps 1–4 are table stakes that any competitor can copy in a sprint. The moment a user says *"I forgot I even wrote that"* is the moment they become retained. Instrument it as the activation event (§11).

---

## 5. Product principles

1. **Never collect data you don't immediately give back.** The mood check must visibly change Pepe's tone or the day's suggestion within the same session. Otherwise it's extraction and users feel it.
2. **The user never files. The user can always correct.** Structure is proposed, never demanded.
3. **No red states.** No overdue counters, no "you missed 4 days," no empty progress rings. Absence is neutral.
4. **Growth is cumulative, never consecutive.** Decoupling growth from streaks is what makes this not-Habitica.
5. **Pepe never tells the user what to do.** It observes, offers, and asks. This is a personality rule *and* a regulatory boundary (§9).

---

## 6. Phase 1 feature spec

### Capture
Text and voice. A single input field. Voice matters more than you think for this cohort and for capture-while-walking.

### Self-structuring
The model does three things on every capture, invisibly:
- **Classify** into a shelf (Project / Idea / Task / Errand / Person / Someday). Six buckets, fixed. Do not let users create custom taxonomies in Phase 1 — that's how you become Notion.
- **Extract** dates, actionable items, and named entities.
- **Link** to existing notes via embedding similarity, above a conservative threshold.

### The correction mechanic — "Pepe is learning"
When Pepe files something wrong, the user taps and moves it. Pepe reacts with visible delight at being taught.

This is the most important design decision in the doc. It turns the unavoidable cost of imperfect AI classification into a **charming interaction and a free labeling pipeline**. Competitors treat misclassification as a bug to hide; you treat it as the pet learning. Track correction rate as your structure-quality metric — it should fall over a user's lifetime, and you can show that curve to investors.

### Resurfacing
One item per day, chosen by a simple ranked heuristic (due today > untouched project with recent related capture > oldest unrevisited idea > new link between two notes). Do not over-engineer this with ML in Phase 1; a rules engine will be indistinguishable from magic.

### Mood
Three options, expressive pixel faces with words, not a 1–10 scale. First open of the day only. It modulates Pepe's tone and the phrasing of the day's resurfacing. **No mood chart in Phase 1** — charts turn feelings into performance, which is the distress loop you set out to avoid. Revisit in Phase 2 as an opt-in retrospective ("your last month, gently").

### The room
1-bit pixel, isometric. Objects appear as **artifacts of the user's own activity**: a bookshelf after 10 notes on a theme, a plant when a project closes, a poster from an idea revisited three times. Never generic reward tokens. The room should read as a portrait of the user's month.

### Cut from Phase 1
Visible knowledge graph · mood charts · habit tracker · meditation content · calendar sync · sharing/collaboration · custom taxonomies · on-device inference · federated learning · reminders you set manually.

---

## 7. Gamification system (classic, transparent)

| Mechanic | Purpose | Guardrail |
|---|---|---|
| **Growth stages** (egg → 4–5 forms) | Long-horizon investment | Driven by cumulative captures. Never regresses, ever |
| **Room collection** | Retrospective pride | Objects mirror real user activity, not arbitrary tokens |
| **Rhythm garden** | Show consistency | Density heatmap. Denser = more. Never red, never empty-shaming |
| **Idle behaviors & easter eggs** | Delight, personality | ~20 idle animations at launch. Cheap, highest delight-per-hour of any feature |
| **Naming & personality** | Ownership | User names Pepe on hatch. Personality traits drift slightly from usage patterns |
| **Reunion scene** | Recovery, not punishment | See §8 |

**Explicitly banned:** loss framing, guilt copy, artificial scarcity, loot boxes, leaderboards, social comparison, "Pepe is sad/hurt/hungry" notifications, countdown timers on anything emotional.

**Notification policy:** maximum 1 per day, minimum 1 content-bearing reason. Every notification must carry a real item from the user's own data. Never "come back." If you can't name the thing you're resurfacing, don't send it.

---

## 8. Dormancy & reunion — spec

| Days inactive | State | Notifications |
|---|---|---|
| 0–3 | Normal | Normal (≤1/day, content-bearing) |
| 4–10 | Napping. Room lights dim | 1 total, content-bearing only |
| 11–30 | Deep sleep. Dust motes, still warm | None |
| 30+ | Hibernation | None. Ever. |

**Reunion (any return, at any point):** Pepe wakes and stretches, says it kept dreaming about the user's things, and immediately surfaces 1–3 items left behind. No penalty screen, no summary of days missed, no data loss, no visual decay of the room.

**Fresh start** is offered as a user-initiated option in settings only — never proposed by the app, never automatic. Framed as "hatch a new one" with the old one archived, not deleted.

---

## 9. Technical decisions

**Framework: Flutter + Flame.** Your instinct is right, and Flame is the specific reason. The isometric pixel room is custom-rendered — that's Flame's home turf, and it beats React Native for this. One codebase across iOS, Android, macOS, Windows.

**Platform priority:** mobile (iOS + Android) is the product. Desktop is the **capture surface** — ship a global-hotkey quick-capture window. For your target user, that single feature is worth more than the entire web app, because capture happens while they're working. Flutter Web builds are heavy and slow to first paint; use it for an interactive landing-page demo, not as the product.

**Backend:** Postgres + pgvector (Supabase is fine to start). Server-side inference on a small, cheap hosted model for classification/extraction, plus an embedding model for linking. Budget roughly a few cents per active user per month at this volume.

**On-device SLM and federated learning: deferred, not cancelled.** They stay in the vision deck as the Phase 3 privacy roadmap. Building them now would consume most of your runway for a benefit users cannot perceive.

**Privacy delivered by policy instead (and this is genuinely marketable):**
- No advertising or analytics SDKs that receive note content. Ever.
- Explicit, separate, opt-in consent for mood data as *datos sensibles* under Ley 1581 — do not bundle it into general T&Cs.
- Full export and hard delete, one tap, no email required.
- Plain-language privacy policy in Spanish, Portuguese, and English, written for an 18-year-old.
- No training on user content without separate opt-in.

**Compliance baseline to build in from day one:** persistent AI disclosure ("Pepe is an AI"), crisis-referral protocol if distress language is detected, no clinical or therapeutic claims anywhere in copy or store listings, and an age gate. These are cheap now and expensive to retrofit.

---

## 10. Roadmap

### Phase 0 — Alpha (6–8 weeks)
Flutter on mobile + desktop from one codebase. 30–50 design partners drawn from the beachhead cohort.
Build: capture, classification, correction, one daily resurfacing, hatch + one growth stage, basic room.
Fake: the personality (hand-authored copy pools, not generated), the "learning."
**Exit criteria:** ≥4 captures/week per active partner and ≥30% of resurfacings marked useful. If resurfacing isn't landing, the thesis is wrong and the pet won't save it.

### Phase 1 — Public launch (10–14 weeks after Phase 0)
Full growth arc, room objects, voice capture, dormancy/reunion, monetization, desktop quick-capture, ES/PT/EN.
**Exit criteria:** D30 ≥ 20% and paid conversion ≥ 2%.

### Phase 2 — Depth (post-PMF)
Opt-in mood retrospective, light project views, shared lists, calendar read-only, expanded cosmetics, second growth arc.

### Phase 3 — Privacy as differentiator
On-device inference for capture and classification. This becomes a marketing weapon only once you have users who care.

---

## 11. Metrics

| Metric | Target | Why |
|---|---|---|
| First capture within 24h | >60% | Activation |
| **First accepted resurfacing within 7d** | >40% | The real aha. Watch this above all |
| Captures/week per WAU | ≥4 | Habit depth |
| D7 / D30 | ≥35% / ≥20–25% | Companion-app benchmark |
| Correction rate over user lifetime | Declining | Proof the system learns — an investor slide |
| Notification opt-in | >50% | Loop viability |
| Free→paid | 2–5% | Freemium norm |
| Monthly churn (paid) | <7% | Companion apps churn slower than average |

---

## 12. Monetization & GTM

**Free tier must be genuinely livable** — unlimited capture, all core loop, one room theme. Paid unlocks cosmetics (themes, Pepe variants, room objects), full history search, export, and desktop quick-capture.

**Pricing:** weekly micro-plan as the primary LatAm entry point (~US$1.50–2 equivalent, priced in local currency), annual at a steep discount. Global markets get standard monthly/annual. Cosmetics are the emotional purchase; utility is the rational one — sell both.

**Rails:** store billing at launch for speed; add Nequi / Mercado Pago / Pix via a web checkout in Phase 2 to recover the 15–30% cut where store policy permits.

**Channels, in priority order:** TikTok + Reels (the room reacting to a voice dump is inherently watchable — build the app so screen recordings look good); micro-creator seeding in cozy/studygram/productivity niches; Spanish and Portuguese ASO from day one; campus ambassadors; a Discord for design partners that becomes the community.

---

## 13. Two pushbacks

### The name "Pepe" is a serious problem

I'd fight this one. Three independent collisions:

1. **Pepe the Frog.** The ADL added it to its hate-symbol database in 2016. Context-dependent, but you will not control context on TikTok, and one screenshot pairing your pixel mascot with that association is an unrecoverable brand event with a Gen Z audience.
2. **PEPE, the memecoin.** It dominates search and app-store results globally. You would be invisible.
3. **Generic in Spanish.** It's the standard nickname for José — low distinctiveness, which makes it weak to register and weak to defend.

Any one of these is survivable. All three together mean you'd be spending marketing budget fighting for your own name.

Starting points for a replacement — short, pronounceable in ES/PT/EN, coined enough to register:
**Tato** (Colombian slang for "all good / done" — culturally native and semantically perfect for a task companion) · **Nubo** · **Kibo** · **Bimo** · **Pipo**

I haven't run trademark clearance on these — say the word and I'll research availability and collisions properly before you commit. Whatever you pick, clear it in Nice classes 9, 42, and 44 with the SIC and USPTO/EUIPO.

### The mood check on every open is too often

Your spec says every time the app opens. For a capture tool that's opened 5–8 times a day, that becomes a toll booth on the core action. **First open of the day only**, with a persistent tappable face if the user wants to update it. Same data, none of the friction.

---

## 14. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Resurfacing isn't magic enough → no retention hook | **Critical** | Phase 0 exit criteria exist specifically to test this before you build the rest |
| Classification quality too low → users lose trust | High | Correction mechanic converts errors into charm; six fixed buckets keep accuracy high |
| Broad audience → diffuse marketing message | High | Beachhead discipline in §3; broaden only after D30 clears |
| Name collision | High | §13 |
| Sensitive-data handling under Ley 1581 | Medium-High | Separate explicit consent, no ad SDKs, in-region storage |
| Flutter Web disappointing → temptation to over-invest | Medium | Web is a demo surface. Do not treat it as a platform |
| Inference cost per user | Medium | Small model, cache aggressively, batch nightly linking |
| Finch or Notion ships a similar loop | Medium | Speed + LatAm cultural specificity + aesthetic are the moat. Nothing else is |

---

## 15. Next three decisions

1. **Name** — resolve within two weeks; it blocks store listings, domain, and all design.
2. **Six-bucket taxonomy** — validate the six shelves against 100 real captures from design partners before writing the classifier prompt.
3. **Personality bible** — one document defining Pepe's voice, its ~20 idle behaviors, and the hard rules (never instructs, never guilts, never claims feelings it would use as leverage). This is a writing job, not an engineering job, and it should start now.

