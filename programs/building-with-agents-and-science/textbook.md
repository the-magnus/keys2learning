# Building with agents and science

The textbook: six modules. What the program is and why is in `about.md`, how a voice session runs in `../tutoring.md`, a learner's progress in their `workbook.md`, under `local/`. Checked 2026-11-11 by web search, mostly against secondary summaries, and every module again 2026-11-12; a point marked (unconfirmed) is from the tutor's knowledge, not found in a source that day, and a point marked (the tutor's link) joins two sources in a way neither of them does. Check a module's unconfirmed points before it is taught.

Each source is marked with the kind of evidence it is, so a claim can be weighed by what stands behind it (module 1, concept 8):
1. **Review:** a systematic review or meta-analysis of many studies.
2. **Trial:** a randomised controlled trial; it can show cause.
3. **Study:** data collected and analysed without random assignment, such as a field experiment or a survey; it shows association.
4. **Benchmark:** models measured on a fixed set of tasks; it shows what they do on those tasks.
5. **Theory:** a researcher's framework, built from research and cases; a claim for evidence to test.
6. **Practice:** a practitioner's or vendor's advice, from experience.
7. **Summary:** someone's account of another source.

The first four are evidence, roughly strongest first, though a well-made study can outweigh a weak trial; theory and practice are what the evidence is held against.

Each module has the same parts:
1. **Idea:** the module in one or two lines.
2. **Concepts:** the few concepts it rests on, each with its thinker.
3. **Sources:** where to read them.
4. **Reason:** a question to reason through with the tutor, on the learner's own system.
5. **Build:** the piece of the learner's system the module ends in.
6. **Brings:** what it gives the builder.
7. **Must cover:** the points the sources themselves stress; the tutor makes sure each lands, and the workbook records which did.

## Overview
1. Which kind of work is this? (Snowden, Sarasvathy; Dybå and Dingsøyr)
2. What is worth doing? (Rumelt, Rother)
3. The road (Goldratt and Dettmer; Forsgren and DORA)
4. Agents as team members (Klein, Woods and colleagues; Kahneman; the evidence on AI and tests; the craft of agentic engineering)
5. Seeing it at a glance (Shneiderman, Tufte)
6. Staying well in it (Sarasvathy, Klein)

## 1. Which kind of work is this?
1. **Idea:** work differs in kind. Where cause and effect can be known in advance, plan or analyse; where they show only in hindsight, probe. A system that treats all work one way fails for part of it.
2. **Concepts:**
   1. **Ordered and unordered systems** (Snowden): in ordered systems cause and effect can be known in advance; in unordered ones only in hindsight.
   2. **The Cynefin domains** (Snowden): clear, complicated, complex and chaotic, plus confusion, each with its own way to decide: sense, categorise, respond; sense, analyse, respond; probe, sense, respond; act, sense, respond.
   3. **Constraints** (Snowden): clear work has rigid constraints, complicated work governing ones (laws, rules, codes that set limits), complex work enabling ones (which give those in the system the ability to do something, and adapt to the context), and chaos lacks them. In the complex, one manages the constraints, not the outcome.
   4. **Safe-to-fail probes** (Snowden): small experiments whose failure can be afforded; what works is amplified, what doesn't is dampened.
   5. **Causal and effectual logic** (Sarasvathy): causal logic picks means toward a given goal and fits where the future can be predicted; effectual logic picks goals the given means can reach and fits under uncertainty.
   6. **Start from the present** (Snowden): describe the present and ask what can change from here, a direction of travel and not a goal: map the present, make small changes, watch what happens; "more stories like these, fewer like those" (Cynefin wiki, [Vector theory of change](https://cynefin.io/wiki/Vector_theory_of_change); the Cynefin Centre's 2022 paper on it; "start from the present" is this textbook's label, not his).
   7. **A framework is a method for one domain** (Snowden, Dybå and Dingsøyr): agile frameworks and their like are bundles of methods, each fit for some domains and harmful in others; Snowden calls agile "good practice, poor theory". Taken as wholes, agile methods have very little evidence behind them: a systematic review of 36 empirical studies graded its strength "very low", so "any estimate of effect … is very uncertain". Single practices can be tested one by one, as modules 3 and 4 do.
   8. **How strong is the evidence** (Dybå and Dingsøyr, after the GRADE scale): evidence is graded high, moderate, low or very low, starting from the design (trials above observational studies) and moved up or down by the studies' quality, their consistency, and how directly they fit the case at hand. A claim is weighed by the kind of evidence behind it; this textbook marks each source's kind.
3. **Sources:** Kurtz and Snowden (2003), "The new dynamics of strategy", *IBM Systems Journal* 42(3), 462–483 (theory); Snowden and Boone (2007), "A Leader's Framework for Decision Making", *Harvard Business Review* (theory); Snowden and Rancati (2021), *Managing complexity (and chaos) in times of crisis: a field guide for decision makers*, EU Joint Research Centre, [JRC123629](https://publications.jrc.ec.europa.eu/repository/handle/JRC123629) (practice); the Cynefin wiki on [constraints](https://cynefin.io/wiki/Constraints) and [constraint mapping](https://cynefin.io/wiki/Constraint_mapping) (practice); Sarasvathy (2001), "Causation and Effectuation", *Academy of Management Review* 26(2), 243–263 (theory); Dybå and Dingsøyr (2008), "Empirical studies of agile software development: A systematic review", *Information and Software Technology* 50, 833–859, section 5.2 (review); Snowden's "good practice, poor theory", reported by [InfoQ, 2012](https://www.infoq.com/news/2012/09/snowden-agile-practice-theory) (summary).
4. **Reason:** take the open work toward one target of yours and sort it by domain. Where was complex work planned as if it were known, and where was known work treated as an experiment?
5. **Build:** every piece of work in the system carries its domain, and each domain has its own shape of next step: a task, an analysis, or a probe that says what result would amplify it and what would dampen it.
6. **Brings:** the right way of working for each piece, and words for why a plan that fits known work fails in the complex.
7. **Must cover:**
   1. The domain decides the method: analysis and expertise for the complicated; probe, sense, respond for the complex.
   2. Each domain has its kind of constraint: rigid, governing, enabling, none.
   3. Snowden's "constraint" is not Goldratt's (module 3): in the Theory of Constraints the constraint is managed to raise the system's throughput; in Cynefin constraints bias a system (Cynefin wiki).
   4. One target usually mixes domains, so the domain belongs to a part of the work, not to the whole (secondary summaries only, 2026-11-12: break the situation into parts and place each in a domain; not yet found in Snowden's own words).
   5. A framework adopted whole skips the question of which domain the work is in.
   6. A claim is weighed by the evidence behind it: a trial can show cause, a study or survey shows association, a benchmark shows models on fixed tasks, and a practitioner's advice is experience to be tested.

## 2. What is worth doing?
1. **Idea:** a goal is not a strategy. A direction worth following starts from a judgement of what is going on, chooses an approach that rules things out, and focuses on the part of the challenge that is both important and solvable.
2. **Concepts:**
   1. **The kernel** (Rumelt): a diagnosis, an explanation of the nature of the challenge that simplifies the situation to what is critical; a guiding policy, the overall approach, which channels and constrains action without saying exactly what to do; coherent actions, steps that reinforce each other.
   2. **Bad strategy** (Rumelt): fluff, not facing the challenge, goals mistaken for strategy, bad objectives.
   3. **The crux** (Rumelt): the most important part of a set of challenges that is addressable, with a good chance of being solved by coherent action.
   4. **Proximate objectives** (Rumelt): a target close enough to be feasible.
   5. **Challenge and target condition** (Rother): a challenge gives direction over months or years; a target condition is the next state to reach, set beyond what is known now, and the way to it is found by experiments (unconfirmed).
3. **Sources:** Rumelt, *Good Strategy Bad Strategy* (2011), chapters 3, 5 and 7, and *The Crux* (2022) (theory); summaries: [the kernel](https://concepts.dsebastien.net/concept/kernel-of-good-strategy/), [The Crux](https://www.leadershipnow.com/leadingblog/2022/05/the_crux_how_leaders_become_st.html) (summary); Rother, *Toyota Kata* (2009) (theory).
4. **Reason:** state the diagnosis of your own challenge in one sentence. What does your approach rule out? If nothing, is there a guiding policy?
5. **Build:** the learner's challenge written as a kernel: the diagnosis in one sentence, a guiding policy that names what it rules out, the crux, and the next proximate objective; and the place where each of these lives in the system.
6. **Brings:** a direction that can be argued with, and a test for whether a list of work is a strategy or a wish list.
7. **Must cover:**
   1. The kernel's three parts, and that the diagnosis comes first.
   2. A guiding policy is useful because it rules options out.
   3. Coherent actions reinforce each other; a list of activities that don't cohere isn't a strategy.
   4. The crux passes two filters, importance and addressability.

## 3. The road
1. **Idea:** the road to a target is its obstacles turned into objectives and put in order; one of them is where the road waits, and work elsewhere doesn't bring the target closer.
2. **Concepts:**
   1. **The constraint** (Goldratt): a system's output is set by its constraint; the five focusing steps are identify, exploit, subordinate, elevate, then go back to the first, without letting inertia become the constraint.
   2. **Prerequisite Tree** (Dettmer): each obstacle gets an intermediate objective that overcomes it, and the objectives are ordered by dependency; read aloud as "in order to A, we must B".
   3. **Future Reality Tree** (Dettmer): a step is tested before it is taken, by reading its effects forward; a bad effect is a negative branch, trimmed by a further step.
   4. **Categories of Legitimate Reservation** (Dettmer): the shared rules for checking any tree.
   5. **Small batches** (Forsgren, Humble and Kim; DORA): work broken into changes small enough to be quickly tested and evaluated is among the long-standing capabilities that predict software delivery performance. With AI it matters more: in DORA's 2025 survey, AI's benefits depended on small batches "with a high degree of certainty"; in 2024, each 25% more AI adoption went with an estimated 7.2% less delivery stability, which the authors think likely comes from AI making changes larger. The tutor's link: the size of a step is how fast the road gives feedback.
   6. **For diagnosis and for conflict:** the Current Reality Tree (Dettmer) is one way to make module 2's diagnosis; the Evaporating Cloud (Dettmer) waits until a real conflict needs it.
3. **Sources:** Goldratt and Cox, *The Goal* (1984) (theory); Dettmer, *The Logical Thinking Process* (2007) (practice); summaries: [the Theory of Constraints](https://docs.flyinglogic.com/thinking-with-flying-logic/overview-of-the-theory-of-constraints), [examples of constraints](https://www.tocinstitute.org/examples-of-constraints.html), [the Current Reality Tree](https://concepts.dsebastien.net/concept/current-reality-tree/), [the Prerequisite Tree](https://tocinstitute.org/prerequisite-tree.html), [the Categories of Legitimate Reservation](https://flyinglogic.com/1165/what-are-the-categories-of-legitimate-reservation/) (summary); Forsgren, Humble and Kim, *Accelerate* (2018) (study); DORA, [*Accelerate State of DevOps Report 2024*](https://services.google.com/fh/files/misc/2024_final_dora_report.pdf), the section on AI and delivery (study: survey); DORA, [*State of AI-assisted Software Development 2025*](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf), the AI Capabilities Model (study: survey of nearly 5,000).
4. **Reason:** take the obstacles to one target of yours: what is each one's objective, which objectives clear several obstacles, and which one must exist before the others can be judged?
5. **Build:** the road format of the system: obstacles with their objectives in order of dependency, the constraint marked, steps small enough to be checked soon after they are taken, and what could go wrong with a step kept as a negative branch with its trim.
6. **Brings:** a road that a person and an agent can both follow and check, and a short way to say why one thing comes first.
7. **Must cover:**
   1. Improving a non-constraint doesn't improve the system.
   2. Each obstacle names what to aim for; one objective can clear several obstacles.
   3. Two kinds of logic, each read aloud: sufficient cause, "if A, then B"; necessary condition, "in order to A, we must B".
   4. A step is tested forward before it is taken, and each negative branch gets its trim.
   5. Small steps give fast feedback; with AI, which makes large changes easy, keeping them small matters more, not less.

## 4. Agents as team members
1. **Idea:** an agent that does a task is automation; one that can be worked with is a team member. That takes shared understanding kept up on both sides, and an agent whose state can be seen, whose course can be changed and whose behaviour can be foreseen. For a language model, part of this is built around the model, not asked of it.
2. **Concepts:**
   1. **Joint activity and common ground** (Klein, Feltovich, Bradshaw, Woods): working together rests on an agreement to work toward shared goals and on common ground, what each party knows the other knows, which must be kept up and repaired as the work goes.
   2. **Ten challenges for a team player** (Klein, Woods, Bradshaw, Hoffman, Feltovich): among them, an agent must be reasonably predictable and able to predict others, and its intentions and actions must be easy for others to read; also that it can be directed, and that it makes its status obvious.
   3. **When a quick judgement can be trusted** (Kahneman and Klein): only where the environment is regular and the judge has learned it with rapid, clear feedback; confidence is no guide. Held up to a model's fluent output, the same question applies (the tutor's link). Measured with AI tools: in a randomised trial, 16 experienced open-source developers took 19% longer with AI on 246 tasks, yet afterwards believed it had made them 20% faster (METR, 2025).
   4. **Context is a scarce resource** (Anthropic): a model has a finite attention budget, so the aim is the smallest set of high-signal tokens that makes the wanted outcome likely; curation happens every time something is passed to the model.
   5. **Tests are the agent's feedback** (Mathews and Nagappan; Fucci and colleagues): given tests along with the problem, models solved 12.0% and 8.5% more problems on two benchmarks, and feeding failing tests back added about 3% more. For people, the evidence on test-driven development is weaker: a meta-analysis of 27 studies found a small gain in quality and little or none in productivity, and a study of 39 professionals found the gain came from short, steady cycles, while whether the test was written first "had no important influence". The tutor's link: a test is a specification the agent can run, and the rapid, clear feedback that concept 3 asks for.
   6. **Engineer the system around the model** (Krivitsky, *Professional Agentic Product Engineering Guide*): a ladder from the prompt to the plan, verification, rules enforced by the harness (the guide's "Enforce"), orchestration and supervision; climb only as far as the work needs. Concept 5 gives the evidence for its verification step.
   7. **Rules as constraints** (the tutor's link to module 1): a rule for an agent is a constraint. A governing one sets a limit the harness enforces; an enabling one gives the agent a way to act well in context.
   8. **A coupled system:** the person's attention and the system's ease depend on each other. A system that is easier to read and steer takes less of the person, who then holds up less of the work (the tutor's link to module 3's constraint).
3. **Sources:** Klein, Woods, Bradshaw, Hoffman and Feltovich (2004), "Ten Challenges for Making Automation a 'Team Player' in Joint Human-Agent Activity", *IEEE Intelligent Systems* 19(6), 91–95, [record](https://archive.cps-vo.org/node/62405) (theory), [summary](https://blog.acolyer.org/2020/01/10/ten-challenges-for-automation/) (summary); Klein, Feltovich, Bradshaw and Woods (2005), "Common Ground and Coordination in Joint Activity", in Rouse and Boff (eds.), *Organizational Simulation*, Wiley, chapter 6 (theory); Kahneman and Klein (2009), "Conditions for intuitive expertise: a failure to disagree", *American Psychologist* 64(6), 515–526 (theory, from two research traditions); Becker, Rush, Barnes and Rein, METR (2025), "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", [arXiv 2507.09089](https://arxiv.org/abs/2507.09089) (trial, 16 developers, early-2025 models); Mathews and Nagappan (2024), "Test-Driven Development for Code Generation", [arXiv 2402.13521](https://arxiv.org/abs/2402.13521), section 4.2 (benchmark, function-level tasks); Rafique and Mišić (2013), "The Effects of Test-Driven Development on External Quality and Productivity: A Meta-Analysis", *IEEE Transactions on Software Engineering* 39(6), 835–856 (review; abstract only); Fucci, Erdogmus, Turhan, Oivo and Juristo (2017), "A Dissection of the Test-Driven Development Process", *IEEE Transactions on Software Engineering* 43(7), 597–614, [arXiv 1611.05994](https://arxiv.org/abs/1611.05994) (study, 82 tasks); Anthropic, [Effective context engineering for AI agents](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents) (practice); Krivitsky, [Professional Agentic Product Engineering Guide (Updated Continuously)](https://github.com/krivitsky/professional-agentic-product-engineering) (practice).
4. **Reason:** take one recent piece of work with an agent that went wrong or cost you attention. What did each of you believe the other knew? Could you see its state, change its course, foresee what it would do?
5. **Build:** who does what between the person and the agents: what only the person decides; what an agent must always show (its state, its evidence, a guess marked as a guess); the tests an agent gets before it writes code; which rules the harness enforces instead of the person repeating them; and what enters an agent's context and what stays out.
6. **Brings:** agents that take less of the builder's attention, and tokens spent where they change the outcome.
7. **Must cover:**
   1. Teamwork needs an agent that is predictable and whose intentions can be read, not only one that is capable.
   2. Common ground is not set once; it drifts and is repaired during the work.
   3. Confidence, a person's or a model's, is no guide to being right; rapid, clear feedback is. Developers who were slower with AI believed they were faster.
   4. Context is finite: more of it is not better.
   5. What must always hold is enforced by the system around the model, not requested in the prompt.
   6. Tests before code help an agent, as a specification it can run; for people, what the evidence supports is short, steady steps, not the order of test and code.

## 5. Seeing it at a glance
1. **Idea:** a wall of text hides the work. A view earns its place by showing the whole first and the detail only when asked for.
2. **Concepts:**
   1. **The visual information-seeking mantra** (Shneiderman): overview first, zoom and filter, then details on demand. His seven tasks: overview, zoom, filter, details on demand, relate, history, extract.
   2. **Data-ink** (Tufte): the share of a graphic's ink that carries data; erase the ink that doesn't. Chartjunk is decoration that carries none or hides it.
   3. **Small multiples** (Tufte): the same small graphic repeated side by side, so the eye compares across them.
   4. **Above all else show the data** (Tufte).
3. **Sources:** Shneiderman (1996), "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations", IEEE Symposium on Visual Languages, 336–343, [technical report version](https://drum.lib.umd.edu/items/cd983adb-568a-47d3-b43a-1d8d8b8c72f4/full) (theory); Tufte, *The Visual Display of Quantitative Information* (1983) (theory), [course notes](https://faculty.cc.gatech.edu/~stasko/4460/Notes/tufte.pdf) (summary).
4. **Reason:** open the main view of your system. What is the first thing the eye lands on, and is it the thing you most need to know? What is on the page that you never read?
5. **Build:** the main view of the system's work: the whole on one screen first, then a way to zoom into a part, with the evidence and detail shown only on demand.
6. **Brings:** a system that is a pleasure to open, and less attention spent finding where things stand.
7. **Must cover:**
   1. Overview first, zoom and filter, then details on demand.
   2. Ink that carries no data is removed.
   3. Comparison needs things side by side in the same form.

## 6. Staying well in it
1. **Idea:** the builder is part of the system. A store that holds only what blocks keeps attention narrow; means, surprises and a limit on losses keep the builder creative and in the game.
2. **Concepts:**
   1. **Bird in hand** (Sarasvathy): start from the means, who you are, what you know, whom you know.
   2. **Affordable loss** (Sarasvathy): size an action by the loss you accept, set before acting.
   3. **Lemonade** (Sarasvathy): a surprise is material; ask what it could be a lever for.
   4. **Crazy quilt** (Sarasvathy): those who commit something of their own reshape the goal.
   5. **Premortem** (Klein): the plan has failed; why?
   6. **The constraint may be a person** (Goldratt): a constraint is often not physical, and exploiting it means not wasting it.
3. **Sources:** Read, Sarasvathy, Dew, Wiltbank and Ohlsson, *Effectual Entrepreneurship* (2011; second edition 2016) (theory); Klein (2007), "Performing a Project Premortem", *Harvard Business Review* 85(9), 18–19 (practice); Goldratt and Cox, *The Goal* (1984) (theory).
4. **Reason:** what did the last month of building give you, and what did it take? Which surprise in it did you use, and which did you treat as noise?
5. **Build:** a place in the system for opportunities, surprises and means beside the obstacles; an affordable loss stated on each probe; and a regular look back at how the building itself is going.
6. **Brings:** a system the builder is better for, not only one that produces.
7. **Must cover:**
   1. Goals can come from the means at hand, not only the other way round.
   2. The loss accepted is set before acting.
   3. A surprise is asked what it could be a lever for.
   4. Exploiting a constraint means not wasting it; subordinating means the rest keeps its pace.
