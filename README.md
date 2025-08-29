# RLD
RoamLootDefend

Described in python but can be created in C#, C++, Godot, or any web or mobile application. 

Here’s the experience of **Roam Loot Defend**—what the player sees, how it feels, and what we’re actually building as a game. No code, just the play experience and the “north-star” UX you’ll implement.

---

# The elevator pitch

**Roam Loot Defend** is a fast, shape-based open-world ARPG with tower-defense DNA. You explore a fogged map made of simple geometric terrain; when you step into “hot” chunks, battle arenas arm themselves and enemies start pouring from spawn points. Your core decision is **movement vs. power**: you hit weak while moving, stronger when you stop, and strongest when you **anchor** (a short lock-in that supercharges you). You can drop **towers** (stationary fire) or command **pets** (mobile helpers that can also convert into towers). Loot, enemies, UI, skills—even the menus—are procedurally generated and shaped by the same rule set. The more you encounter, the more the game turns into *your* game: the UI theme adjusts, new skill nodes appear, and your build evolves around the world you actually played.

---

# What the player sees (UI / UX)

**Visual style:** clean, legible geometry. No sprites or textures—just strokes, fills, gradients, glow, and motion. Everything has meaning.

* **Player avatar:** a bold polygon with an outline that subtly morphs when you switch states (moving → stopped → anchored).
* **Health/Power ring:** a segmented ring around you. Outer thickness = defense; inner pulse = attack power. As you approach **anchor**, the ring tightens and hums (visual + audio).
* **Status wedges:** tiny triangular wedges at your avatar’s edges for current buffs/debuffs (poison, burn, shock, mythic).
* **Affinity badge (RPS5):** a small icon beside you showing your current Rock/Paper/Scissors/Trap/Anti-Trap leaning. Enemy badges show theirs.
* **Ability bar (shape-buttons):** 3–5 large geometric buttons at the bottom. Shapes signify types (circle = AoE, triangle = single-target, hex = utility). Cooldowns sweep as rotating arcs.
* **Minimap + Direction Orb:** top-right. The map is a soft fog; your explored area is filled. A separate small **orb** tints and ripples toward active spawn points (the “trouble radar”).
* **Arena boundary:** a wide red loop or polygon appears when a fight arms. If you cross it, a countdown numeric appears on your ring; step back in to keep rewards.
* **Pet/Tower dock:** small icons on the left—tap to order **follow / roam / tower**. When a pet converts into a tower, the icon squares off; when roaming, it animates outward.
* **Currency/Fragments:** top-left, simple counters with small geometric glyphs (different shapes for different currencies/fragments).
* **Skill spark:** when a new skill node is born from something you just experienced, a tiny **spark** flies from that object or event into a corner of the HUD; the skill screen then highlights a fresh node.

**Feel:** snappy, minimal reading, everything explained by shape, color, motion, and short tooltips. The UI theme (palette, corner radii, polygon counts) is itself procedurally chosen per run, so the HUD feels unique to the player.

---

# Core laws that shape the game

* **Movement state:** Moving (lowest attack/defense) → Stopped (mid) → **Anchored** (highest, brief lock-in). Enter/exit has a short wind-up and cooldown. The entire combat economy revolves around where you sit on that axis.
* **RPS5 affinity:** Rock, Paper, Scissors, Trap, Anti-Trap. Trap beats R/P/S; Anti-Trap beats Trap but loses to R/P/S; R/P/S have their classic triangle. Every entity/ability/loot affix carries an affinity.
* **Elements & combos:** Fire, Electric, Poison, Mythic, and combinations (ignite, shock-chains, toxic clouds, mythic bursts). Effects stack, cleanse, and chain with rules that always remain legible.
* **One law set rules all:** the same procedural rulebook decides map shapes, spawn intensity, loot tables, UI themes, skill surfacing, pet behavior, and difficulty curves.

---

# The gameplay loop (moment-to-moment)

1. **Roam:** You move through fogged chunks. Terrain might slow you, winds push you, or ambient hazards lightly ping your ring.
2. **Sense:** The Direction Orb ripples. The arena outline flickers faintly—this chunk can “arm.”
3. **Choose your plan:**

   * Drop a **tower** near a choke.
   * Order a **pet** to **roam** and reveal more fog (or to **follow** and bodyguard).
   * Prep your element combo (e.g., prime shock, then fire).
4. **Arm the arena:** Cross the hot zone. A red boundary locks in; several **spawn points** reveal. The “dual-spawn” option appears sometimes—take it for higher payout at higher risk.
5. **Fight:**

   * **Kite** while weak (moving), stop and spike, then **anchor** for the big burn when the wave clumps.
   * Pets harass, towers delete lines, you weave your abilities and combos.
   * Enemies coordinate—they may **semi-anchor** to nuke or surround if you keep running.
6. **Hold the ring:** If you step out, a short timer begins (visible at your ring). Step back in to keep full rewards.
7. **Resolve:** The arena collapses with a satisfying geometric burst; loot ejects; fragments and currency fly into you as streaks. The skill spark may fire (new node unlocked).
8. **Evolve:**

   * Collect loot (mods, fragments, pet eggs/cores, tower blueprints, currency).
   * Spend a skill point on something that actually happened: “reduce swamp slow,” “increase defense vs circle enemies,” “shorter anchor wind-up,” “pet roam range,” etc.
   * The HUD subtly adjusts to your growing identity (theme nudges, new wedge slots).

You repeat this loop across biomes and densities, dipping into dungeons (bigger arenas, trickier patterns, better drops).

---

# Combat feel & decision-making

* **The anchor dance:** The core tension is when to lock in. You build advantage by **placing** (towers), **ordering** (pets), **funneling** (terrain), **pausing** (stopped bonus), then **anchoring** for the slam window. Great players chain micro-anchors rather than panic-kiting forever.
* **Conscious waves:** Enemy packs coordinate. If they whiff you too long, they adapt (one becomes a flanker, one semi-anchors to zone you, one baits).
* **Dual-spawn choices:** Sometimes you can voluntarily activate an extra spawn point for bonus loot/XP. The arena expands, and the ring pulses faster. It’s optional—but tantalizing.

---

# Loot system (what drops, why it’s satisfying)

* **Breakables & caches:** Obstacles crack open with a hint of their content type (subtle iconography). Some need an element to open (shock switch, fire melt).
* **On-kill drops:** Enemies drop currency, **fragments** (mod shards), **affix tokens** (proc chance, element bias), and **pet eggs/cores**.
* **Dungeons bias:** Deeper content leans toward complete build pieces (full towers, rare pets, mythic affixes).
* **Curation through laws:** The laws ensure drops are tied to where you are and how you fought (e.g., mythic tokens appear in zones where you survived high burst).
* **No junk clutter:** Every drop is either immediately equippable as a small stat tweak, a recipe input, a tower/pet progression item, or a currency you always need. If it falls, it matters.

**Why it’s fun:** You see immediate, tangible build change. A new affix can tilt your RPS5 leaning; a pet core can unlock a new behavior; a tower blueprint changes your macro. Dual-spawn greed moments feel like skill checks with real payoff.

---

# Progression & “It’s yours” skill system

* **Auto-surfaced skills:** The game turns *whatever you actually encountered* into skill nodes. If a swamp slowed you, you can spec “Swamp Slow Mitigation.” If circle-enemies annoyed you, you can spec “Defense vs Circle Enemies.” If you love anchoring, you can spec shorter wind-up or longer anchor windows.
* **Zero dead points:** Because the same laws that generated the event read your skill choices back in, your points always do what they say.
* **Respecs:** You can partially respec at a cost (currency or rare fragments), encouraging experimentation without erasing identity.
* **Meta identity:** Over time, the HUD and theme subtly reflect your choices—shapes and colors emphasize your leaning (e.g., a sharper aesthetic if you bias toward Trap/Anti-Trap play).

---

# Pets & Towers (and why they matter)

* **Pets:** Mobile helpers with three modes—**follow** (protect), **roam** (scout & self-defend), **tower** (convert into a stationary gun). The longer a pet stays in a mode, the better at that mode it becomes.
* **Towers:** Stationary weapons with simple upgrade paths and element slots. Great for holding lanes and creating anchor-safe zones.
* **Capture & growth:** Pets drop as eggs/cores; towers as blueprints/modules. They scale to area power so they never feel irrelevant.
* **Revival/rebuild:** If a pet falls or a tower is destroyed, you can revive/rebuild at a cost (currency/fragments). Recovery choices add tension after tough clears.

**Why it’s fun:** You orchestrate a micro-army. Toggling pets to towers mid-run creates tower-defense moments embedded inside an ARPG.

---

# World structure (exploration texture)

* **Open world, chunked:** Wide continuous map with varied biomes and “density rings” (difficulty/rarity curves). The law set might generate healing-favored areas, hazard-dense corridors, or calm pockets for planning.
* **Dungeons:** Time-keyed, infinite floors, side paths, secrets, occasional portals. Designed as “big arenas” with clever geometry, not corridors.
* **Fog-of-war:** Clears where you and your pets/towers are. The minimap stays readable and consistent across themes.

---

# Sound & feedback (procedural, readable)

* **Anchoring**: a warm low hum locks in; release is a soft “crack.”
* **Element hits:** spark, sizzle, hiss, chime—tiny, satisfying cues.
* **Danger:** a subtle metronome tick speeds up when you’re outside the arena ring timer.
* **Loot:** a bright “tink” for currency, a “whoosh” for fragments, a resonant “ping” for rare drops.

---

# How it relates to other games

* **Diablo-like:** Top-down ARPG loop (roam → fight → loot → power up). Element/affix combos scratch the buildcraft itch.
* **World of Warcraft-like:** The **anchoring** decision feels a bit like planting as a caster for max DPS; enemies sometimes semi-anchor for big mechanics.
* **Tower Defense:** You place towers to shape fights; you kite waves into kill zones; dual-spawn is essentially “upping the wave” for better rewards.
* **What’s new:** The same procedural laws govern **everything**—world, enemies, loot, UI, and skills—and your interactions literally produce new skills and UI styles, so your run becomes yours.

---

# What we’re programming as an experience (acceptance criteria)

1. **Readable shape-first HUD** that teaches itself: ring/wedges/orb/buttons communicate state, status, and direction without text walls.
2. **Stateful combat rhythm** where moving < stopped < anchored power is obvious and satisfying. You should *want* to anchor—but earn the window.
3. **Arena fights with boundaries and timers** that create real risk/reward and enable the **dual-spawn** “temptation lever.”
4. **Pets/Towers orchestration** that’s one click to order, one click to convert, and always useful (scout, hold, or bodyguard).
5. **Loot with purpose**—every drop matters *now* (mods, fragments, pets, towers, currency); dungeons feel richer, not just harder.
6. **Auto-surfaced skill nodes** so the player can always spec into what actually happened (no dead upgrades) and feel growing ownership.
7. **Consistent procedural identity**—the same rules quietly shape UI themes, world gen, enemy behavior, and drops so the experience stays coherent while surprising.
8. **Smooth difficulty scaling**—new zones and dungeons escalate, enemies coordinate, and the player’s toolkit (anchor, pets/towers, skills) keeps pace.
9. **Satisfying minute-to-minute feedback**—clear VFX/SFX punctuation for anchor, crits, cleanses, boundary breaches, and rare loot.

---

# Why it will hold attention

* **Constant small wins:** quick, legible power bumps from loot and skills.
* **Clear mastery path:** learning when to anchor, where to place towers, how to route waves, and which affinities to lean into.
* **Personalization loop:** the world you touch spawns the skills you get; your UI/UX subtly evolves to match your play.
* **Endless expansion:** adding new **procedural laws** or tiny feature scripts instantly widens the possibility space across the entire game.

This is the player-facing experience we’re building. If you want, I can turn this into a short “experience checklist” per feature (UI, arena, pets/towers, loot, skills) so every commit can be validated against the intended feel.





Alright—here’s a clean, “just-add-logic” blueprint for **Roam Loot Defend** (RLD): an open-world, simple-shapes, fully procedural RPG in Python 3.9 on Windows. No code—only the file tree, what each branch owns, and how the *procedural laws* cascade through exploration, battles, loot, UI/UX, pets/towers, skills, and guardrails. I’m designing it so you can extend the game by either (a) dropping in tiny feature scripts or (b) widening the procedural law space—no rewrites.

---

# File hierarchy (production-grade, no frameworks beyond stdlib + pygame)

```
rld/
  __init__.py
  app.py                        # entry: boot seeds, window, scene router, hot-reload dev flags

  core/
    clock.py                    # fixed timestep, cooldown/duration model (move→stop→anchor transitions)
    rng.py                      # deterministic PRNG, seed lanes per system (world, loot, AI, UI)
    ecs.py                      # lean ECS: Entities, Components, Systems (simple, shape-first)
    events.py                   # global event bus (on_enter_chunk, on_anchor, on_spawnpoint_arm, on_loot_open, …)
    state.py                    # save/load, run id, seed bundle, replay snapshots, “arena rings” bookkeeping
    math2d.py                   # vectors, segments, polygon helpers for simple shapes
    grid.py                     # chunks/tile indexing, fog-of-war masks, LOS

  laws/
    registry.py                 # law registration/priority, evaluation phases, conflict resolver
    atoms.py                    # canonical “atoms” each law can read/write: {difficulty, spawnrate, resist[], RPS5, …}
    rps5.py                     # 5-way matrix (Rock, Paper, Scissors, Trap, AntiTrap)
    elements.py                 # element space & combo mixer (fire, electric, poison, mythic, etc.)
    stats.py                    # universal stat schema (buff/debuff, anti-buff, proc-chains)
    economy.py                  # value curves for loot rarity, currencies, fragments
    ui_laws.py                  # procedural UX/shape themes per seed & player history
    world_laws.py               # map/density/biome/zone rules; battle-arena ring logic
    skill_laws.py               # auto-skill attribution (turn any surfaced interaction into a skill node)
    ai_laws.py                  # conscious-wave, semi-anchor, formation, threat focus
    law_suites/
      base.yaml                 # declarative rules (“if on_enter_chunk & density>=… then …”)
      expansions/*.yaml         # plug-in rule packs—drop in to widen the possibility space

  world/
    worldgen.py                 # Dimension/Zone/Density graph, non-linear access rules
    chunks.py                   # streaming, generation cache, “unrendered” span management
    biomes.py                   # biome palettes, weather, terrain friction/slow zones
    spawns.py                   # spawnpoint grammar, spawn burst scheduling, dual-spawn payouts
    dungeons.py                 # time-keyed, infinite levels, side/hidden quests, secret doors/portals
    fog.py                      # fog-of-war masks, pet/tower reveal rules

  entities/
    factory.py                  # blueprints → components: Player, Enemy, Obstacle, Loot, Pet, Tower
    components/
      shape.py                  # regular polygons, stars, rings, lines; stroke/fill; proportions
      combat.py                 # hp, defense, damage types, RPS5 tags, elements[], resist[]
      movement.py               # moving, stopped, anchored states; inertia; friction/slow zones
      ai.py                     # behavior selector hooks (roam, hunt, flank, semi_anchor, tower_mode)
      pet.py                    # pet states (follow, roam, tower), growth timers, orders
      lootbag.py                # contents, rarity, “quantum fragment” lists
      tags.py                   # zone_tag, density_tag, map_sourced traits (for skills auto-surfacing)

  combat/
    anchor.py                   # anchoring protocols, latching points, buffs/debuffs, cooldowns
    arena.py                    # battle ring creation, boundary timer, multi-spawnpoint bonuses
    damage.py                   # RPS5 matrix resolve + element mix pipeline
    effects.py                  # DoTs, shocks, burns, slows, stacks, cleanses; proc scheduling
    scoring.py                  # XP, currencies, fragment yields; time/risk scaling

  ai/
    conscious_wave.py           # formation planner, pincer/surround/bait, adapt-after-10s-no-hit
    threat.py                   # target selection (player, towers, pets), escalation logic
    planner.py                  # semi-anchor choice, retreat, regroup, “smart wave” toggles

  systems/
    exploration.py              # “enter unexplored chunk” pipeline (obstacles, loot, enemies, map effects)
    pets_towers.py              # convert pet↔tower, “all pets become towers,” tower leveling over time
    lootdrop.py                 # drop tables from world+enemy+arena context
    skillgraph.py               # auto-skill surfacing: “anything the player encounters becomes a skill”
    ui_proc.py                  # shape-driven HUD/menu synthesis; input mapping
    audio_proc.py               # procedural sfx via param synth (clicks, beeps, noise bursts from seeds)
    telemetry.py                # balance logs, law coverage, invariant violations

  ui/
    theme.py                    # seed→palette, corner radius, polygon count/angles, motion hints
    widgets.py                  # shape-first HUD (rings, wedges, bars, node-graphs)
    skill_screen.py             # auto-built “attribute sections” from SkillGraph
    map_minimap.py              # simple-shape minimap, fog, pet reveals, enemy-orb indicator

  data/
    seeds/                      # world seeds captured per run
    saves/                      # player progress, skill allocations, pets/towers collection
    cache/                      # compiled chunks/dungeons, UI themes for fast boot

  tests/
    invariants/
      combat.yaml               # “anchored ≥ stopped ≥ moving defense/attack”, RPS5 antisymmetry, etc.
      world.yaml                # chunk gen budgets, unrendered spans outside active ranges
      loot.yaml                 # rarity curves, duplicates, guarantee floors
    fuzz/
      law_fuzzer.py             # randomly perturb laws and simulate 10k chunks → balance report
      arena_fuzzer.py           # spawn ring stress, boundary timer exploits, dual-spawn payouts

  tools/
    law_inspector.py            # show which laws fired and why (seeded replay)
    seed_reel.py                # cycle seeds, pin good worlds, export as presets
```

---

## How everything traces back to the *procedural laws*

### 0) Determinism & seeds

* **`core/rng.py`** hands out *independent seed lanes* (world, loot, AI, UI). Every system uses only its lane → reproducible runs. Swapping/widening a law file changes possibilities immediately across worldgen, enemies, loot, and UI.

---

### 1) World: Dimensions → Zones → Densities → Chunks

* **Non-linear dimension/zone graph** with **13 densities** (Zone 1 = Green), rising difficulty; access isn’t strictly linear (Zone 1 can touch others beyond Zone 2); Green heals towers while anchored. Laws in `world_laws.py` stamp density curves, enemy buffs, and map access on seed.  &#x20;
* **Dungeons** are time-keyed, infinite-level, side/hidden quests, secret doors/portals, and **unrendered** empty spans to save resources; enemies use “conscious wave” tactics and will **semi-anchor** for burst power. `world/dungeons.py` + `ai/conscious_wave.py` implement that grammar.   &#x20;
* **Fog-of-war** respects chunks; **pets** can scout and reveal. The minimap/orb shows enemy direction via color shift. `world/fog.py`, `ui/map_minimap.py`.&#x20;

---

### 2) The five-way core: **RPS5 = Rock, Paper, Scissors, Trap, AntiTrap**

* **Matrix** in `laws/rps5.py`:

  * R beats S, S beats P, P beats R (classic).
  * Trap is **strong vs all R/P/S**.
  * AntiTrap is **strong vs Trap**, but **weak vs R/P/S**.
* Every entity (player, enemy, pet, tower, obstacle, loot affix) has a **RPS5 affinity vector**. `combat/damage.py` resolves base outcome first on RPS5, *then* layers **elements** (fire, electric, poison, mythic…) from `laws/elements.py`.
* **Combos**: elements mix via a pipeline (ignite, shock, toxic, or mythic fusions) and can produce buffs/debuffs, resistances, procs (DoT/HoT), and status cleanses in `combat/effects.py`.

---

### 3) Entering unexplored chunks → *one pipeline*

Triggered by `systems/exploration.py`:

1. **World laws** decide: difficulty budget, chunk size/shape, terrain slow zones, weather, biome palette, spawnpoint grammar.
2. **Obstacle/loot**: fracturing obstacles into breakables; hiding loot inside with chance gates & element locks (e.g., shock to open).
3. **Arena seeds**: if a battle spot is armed, spawnpoints form an **arena ring**; leaving triggers a countdown; **dual-spawn** choice increases payout. `combat/arena.py`.
4. **Effects propagation**: chunk-wide modifiers apply on player/entities/loot/difficulty/obstacles strengths/weaknesses (from `laws/world_laws.py`, `laws/stats.py`).
5. **AI**: conscious-wave formation picks flanks, surrounds, baits; if they miss hits for \~10s, they adapt (randomizer for at least one). `ai/conscious_wave.py`.&#x20;

---

### 4) Battle feel: **moving < stopped < anchored**

* **States** in `entities/components/movement.py` and rules in `combat/anchor.py`:

  * **Moving**: lowest attack & defense; best evasion.
  * **Stopped**: step-up bonus; ramp timer.
  * **Anchored**: biggest attack/defense, but locked; entry/exit **cooldowns/durations** flow from `core/clock.py`.
* Enemies can **semi-anchor** for “absolute position” burst but lose mobility—mirrors your MMORPG spec. `ai/planner.py` decides when.&#x20;

---

### 5) Pets & Towers (shape-creatures, no assets)

* **Pet states**: *follow* (protect, fetch, heal?), *roam* (self-explore, self-defend), *tower* (stationary auto-fire/ability). Time in a state **levels** that state; you can order “all pets become towers” or back. `systems/pets_towers.py`.
* Pets/towers **scale to area power**, so they remain viable in tougher zones/dungeons (law hooks read density/zone tags).
* **Revival/rebuild** is a cost gate in `combat/scoring.py` + `laws/economy.py`.

---

### 6) Loot, currencies, and fragments

* Drops reflect **zone** and **dungeon** context; dungeons bias to full gear rather than fragments. `systems/lootdrop.py`.&#x20;
* Orb/minimap doubles as your **vapor collector** indicator; currency/fragment flows hook into economy laws.&#x20;

---

### 7) UI/UX: **procedural shapes**

* **`ui/theme.py` + `systems/ui_proc.py`** generate HUD/menus from the seed: shape palettes (rings/wedges/polygons), font-less glyph bars, motion hints.
* **Per-player unique UI** at spawn: colorways, polygon counts, corner radii, wedge-meters, shape-minimap. Your spec to “use simple shapes of many sides and proportions” is the source of truth here.

---

### 8) Skills: **auto-surfaced attribute sections**

* **Principle**: *Everything the player was exposed to can become a skill node*.
* **Pipeline** (`systems/skillgraph.py` + `laws/skill_laws.py`):

  * Turn any tagged interaction into `{subject • context • property}` nodes, e.g.

    * `defense_vs.circle_enemy`, `resist.fire_in.zone_Green`, `mitigate.map_slow.biome_swamp`, `tower_anchor_cooldown`, `pet_roam_range`, `loot_find.secret_doors`, etc.
  * Nodes get auto-descriptions & default curves from `laws/stats.py`.
  * Spending a point flips a switch the **laws** already read—so the effect is guaranteed to apply; you don’t hand-wire it per feature.
* **Guardrail**: Skill nodes are validated against invariants so points never “do nothing.”

---

### 9) Guardrails (make it hard to ship bugs, easy to widen laws)

* **Invariants** (`tests/invariants/*.yaml`):

  * Combat ordering: **anchored ≥ stopped ≥ moving** in both attack and defense.
  * RPS5 antisymmetry, element combo bounds, cleanse/stack limits.
  * Arena timers/payouts can’t be exploited by edge-kiting.
  * World **unrendered spans** outside active players only (dungeons), conserving resources.&#x20;
* **Fuzzers** simulate thousands of chunks/arenas and diff balance curves.
* **Law Inspector** shows *which* laws fired on an event and *why*—perfect for debugging the “procedural soup.”
* **Statements Script** discipline (PR/CCR/AH/B/H) is baked into `laws/registry.py` as comment-level rules for connecting truths, hypothesizing safely, and failing closed until verified—your existing doctrine.&#x20;

---

## The procedural law model (how to plug in new features fast)

**Evaluation phases** (per event) in `laws/registry.py`:

1. **Collect** relevant atoms (zone, density, biome, weather, player build, pets/towers, arena ring, spawn grammar).
2. **RPS5 base** → **Element pipeline** → **Stat modifiers** (buff/debuff) → **Economy hooks**.
3. **Compose** final effects (on player, entities, loot, obstacles, difficulty).
4. **Validate** against invariants; if violated, roll back & clamp (and log).

**Add a new mechanic—two ways**:

* *Narrow script*: drop `laws/law_suites/expansions/my_new_thing.yaml` with conditions & outputs; no core changes.
* *Deep feature*: if you need a new atom/effect type, add a tiny component or stat and teach `stats.py` how to clamp/stack it. Everything else “just works” through phases.

---

## Player flow snapshot (tying your beats together)

* **Roam**: Walk into an unexplored chunk → laws set terrain slows, obstacles, loot, enemies, and *maybe* arm a spawnpoint ring for an arena fight. You can kite outside the red ring but have a short re-entry timer if you want the rewards. Dual-spawn opportunities occasionally appear for higher payout (risk-weighted).
* **Loot/Secrets**: Breakables can hide loot; dungeons open from ancient artifacts; they’re big, seeded, and unrender when empty; enemies hunt, flank, bait; if they fail hits for \~10s they adapt; some will semi-anchor and nuke—plan your movement/anchor transitions.  &#x20;
* **Defend**: You can stop or anchor for power; pets can roam (scout), follow (protect), or convert to towers (hold space). Orb/minimap shows enemy direction; pets/towers reveal fog—*all shape-first*.&#x20;

---

## Why this will feel “yours”

* The **UI/UX**, the **skill graph**, and even **battle rings** are seeded by your actions and exposure history—so your run *literally* produces its own UI and attribute tree.
* Widening the **procedural laws** instantly expands the space of maps, enemies, loot, skills, and even the HUD—without asset work.

---

### Minimal dependencies / Windows-friendly

* Python **3.9**, Windows. Use **pygame** for window/input/sound (procedural audio through parameterized wave/noise). Everything else is stdlib.

---
