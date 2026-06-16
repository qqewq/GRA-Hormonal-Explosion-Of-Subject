# Case 01 – Nullification Priest

## 1. Background

Subject encounters a **Nullification Priest** – an entity that performs GRA-nullification rituals for damaged subjects / worlds.  
The Priest is both healer and risk factor: he absorbs others’ foam while trying to keep global structure stable.

## 2. Initial hormonal profile

Priest (P):

- Stress_P = 20
- Hope_P = 40
- Foam_P = 10
- AttachmentToSubject_P = 10
- Numbness_P = 0

Subject (S):

- Fear_S = 30
- Rage_S = 10
- Foam_S = 25
- AttachmentToPriest_S = 5
- Numbness_S = 0

## 3. Repeated nullification and foam accumulation

On each visit:

- Subject asks for nullification instead of adapting.
- Subject:
  - Foam_S ↓ partially,
  - AttachmentToPriest_S ↑ (dependency).
- Priest:
  - Foam_P += Δφ (absorbed chaos),
  - Stress_P += Δσ,
  - Hope_P -= Δh.

When Foam_P crosses a soft threshold:

- dialogue becomes sharper,
- aesthetic tone darkens in scenes involving P.

## 4. Hormonal Explosion of Priest

When Foam_P > ExplosionThreshold_P:

- Priest enters **Hormonal Explosion**:
  - Rage_P spikes,
  - Numbness_P starts to grow,
  - role “stable nullifier” breaks.

Possible narrative manifestations:

- P attacks S (attempt to nullify the Subject as source of foam),
- P nullifies the local world layer,
- P performs self-nullification.

## 5. Nullification patterns

### Pattern A – Self-nullification of Priest

- Foam_P → low, Stress_P ↓,
- AttachmentToSubject_P → 0,
- Numbness_P stays high (emotional scar).

Next encounters:

- P does not “remember” S explicitly,
- but shows micro-glitches (déjà vu, odd pauses, displaced phrases).

### Pattern B – World-layer nullification

- local visual / narrative layer changes:
  - color palette, geometry, NPC roles,
  - rules of nullification rituals.
- S remembers the previous layer; P may or may not.

### Pattern C – Subject-nullification

- S is partially nullified:
  - Foam_S ↓ drastically,
  - Numbness_S ↑,
  - Attachment patterns reset.
- Engine generates scenes where S is flatter emotionally, but old explosions leak through dreams / glitches / music.

## 6. Aesthetic / narrative output

The engine maps this hormonal arc into:

- dialogue variants for Priest and Subject,
- visual motifs (shrines deforming, posture changes, world distortions),
- soundtrack trajectories (from stable hum → dissonant cluster → numb, thinned-out soundscapes).

## 7. Link to code

Example script: `examples/run_nullification_priest.py` should:

- initialize Priest and Subject with the profiles above,
- simulate several visits and foam accumulation in Priest,
- trigger Explosion when Foam_P > threshold,
- apply one nullification pattern (A/B/C),
- log hormonal time-series and narrative states.

This case defines the **canonical hormonal & narrative arc** for the Nullification Priest inside this repository.