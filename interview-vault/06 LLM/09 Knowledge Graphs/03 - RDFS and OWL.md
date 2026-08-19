# RDFS & OWL

**Prev:** [[02 - RDF and Turtle]] · **Next:** [[04 - SPARQL]]

---

## In plain English

Raw triples are just facts. **RDFS** adds **vocabulary** (classes, subclasses). **OWL** adds **logic** (rules, constraints) for richer reasoning.

---

## RDFS (start here)

| Term | Meaning | Example |
|------|---------|---------|
| `rdfs:Class` | Type of thing | `Professor` is a class |
| `rdfs:subClassOf` | Inheritance | `Professor` subclass of `Person` |
| `rdfs:domain` | Property applies to | `teaches` domain `Professor` |
| `rdfs:range` | Property points to | `teaches` range `Course` |

**Inference example:** if `Alice` is a `Professor`, and `Professor` subclass of `Person`, infer `Alice` is a `Person`.

---

## OWL (when you need more)

| Feature | Use |
|---------|-----|
| `owl:equivalentClass` | Two classes mean the same |
| Restrictions (`someValuesFrom`) | "Every Professor teaches some Course" |
| `owl:inverseOf` | `teaches` / `taughtBy` |
| Transitive properties | `partOf` chains |

**Cost:** heavier reasoning — use when compliance or complex validation matters.

---

## When to use which

| Stage | Technology |
|-------|------------|
| MVP ontology | RDFS or simple schema |
| Medical / legal / enterprise semantics | OWL + SHACL validation |

---

## Common traps

| Trap | Correct |
|------|---------|
| OWL on day 1 for startup | Start simple; grow schema |
| Confuse class and instance | `Professor` = class; `Alice` = instance |

---

**Next:** [[04 - SPARQL]]
