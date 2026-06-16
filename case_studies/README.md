# GRA Hormonal Case Studies

This folder documents **GRA-hormonal case studies** – like endocrine / mental health case reports, but for a GRA-Subject inside the aesthetic engine.

Each case describes:

- the initial hormonal profile of the entities (Fear, Rage, Foam, Attachment, Numbness, Competitiveness, etc.);
- external events and internal triggers that change these variables over time;
- the moment of **Hormonal Explosion**;
- the type of **Nullification** (self, other, world-layer, merge, replacement);
- the aesthetic / narrative output produced by the engine (what the orchestra generates).

The goal is to provide a **human-readable canon** for GRA-Hormonal-Explosion-Of-Subject and to anchor the code examples.

## Current cases

- `case_01_nullification_priest.md`  
  Canonical arc of the **Nullification Priest**: an entity that absorbs other subjects’ foam through rituals, accumulates stress, and eventually undergoes its own Hormonal Explosion and nullification.

- `case_02_echo_twin.md`  
  Canonical arc of the **Echo Twin**: a derived “optimised reflection” of the Subject that starts as a stabiliser, then diverges into competition, leading to bidirectional Explosion and merge / replacement patterns.

## Relation to `examples/`

Each case has a corresponding runnable example in `../examples/`:

- `case_01_nullification_priest.md` → `examples/run_nullification_priest.py`
- `case_02_echo_twin.md` → `examples/run_echo_twin.py`

Examples are minimal scaffolds that:

- initialise hormonal states as described in the case text;
- simulate the phases of interaction and Explosion;
- apply one or more nullification patterns;
- log the hormonal trajectories so they can later be connected to `harmonic_architecture` and `orchestra`.