---
layout: post
title: "Agentic AI: Model Autonomy, and the Harder Question"
date: 2026-07-18
excerpt: "Everyone's asking whether AI agents are good enough to put in production. Wrong question. The gating variable was never capability. It was reversibility — and LLMs are making it dangerously easy to forget."
---

<div class="post-intro">
<p>Everyone's asking whether AI agents are "good enough" to put in production.</p>
<p><strong>Wrong question.</strong></p>
<p>We spent a decade learning this lesson the hard way with a different kind of AI. Reinforcement-learning agents were trading, pricing, routing, and recommending autonomously years before LLMs existed. And in the domains where a wrong action was catastrophic and irreversible — healthcare, industrial control — we deliberately kept them out, no matter how capable they got.</p>
<p>The gating variable was never capability. It was reversibility.</p>
<p>That lesson still holds, and LLMs are making it dangerously easy to forget. A few lines of SDK code now put a model in the driver's seat of a real business process — and the fluent, confident way it explains itself makes us trust it in ways the capability doesn't warrant. An articulate rationalisation looks like judgment. It isn't.</p>
<p>So the question for any agentic system isn't "how smart is the model." It's: what does an action cost if it goes wrong, and can I undo it?</p>
<ul>
<li><strong>Drafting text, proposing options?</strong> Cheap, reversible. Let it run.</li>
<li><strong>Moving money, deleting records, changing access?</strong> Expensive, irreversible. Cage it, or keep a human between the decision and the consequence.</li>
</ul>
<p class="dragon">You don't let a dragon run amok. You ride it — on reins.</p>
</div>

*A field guide for architects deciding how — and whether — to put a language model in the driver's seat.*

<img src="/img/2026-06-07-image1.jpg" alt="Agentic AI" style="display: block; width: 100%; margin: 20px 0 30px;">

There is a lot of noise right now about agents, agent frameworks, and "agentic AI platforms." Most of it conflates layers that are actually distinct, and almost none of it asks the question that matters most: not *how* to build an agent, but *when you should let one act on its own*.

This piece does two things. First, it untangles the stack — what AgentCore, Strands, the Claude Agent SDK, Bedrock, Copilot Studio, and the rest actually are, and which ones are even comparable to each other. Second, and more importantly, it makes an argument about deployment that the landscape conversation usually skips: the right question for an agentic system is not "is the model good enough," it is "what is the cost and reversibility of the actions I am letting it take." A decade of pre-LLM history already answered the underlying question, and we are at risk of un-learning it.

---

## Part 1 — Untangling the stack

The single most common confusion in this space is comparing things that live at different layers. People put "Copilot Studio" next to "Bedrock" and try to decide between them, which is like choosing between a steering wheel and an engine. They are not alternatives; they are different parts of the same car.

There are four distinct layers, and almost every vendor has a product (or a gap) at each:

**1. The model / inference layer.** Where the model weights actually run and produce output. Bedrock, Azure AI Foundry / Azure OpenAI, Vertex AI, and the first-party Anthropic and OpenAI APIs all live here. This is the "brain," and it is stateless — request in, response out.

**2. The authoring framework / SDK layer.** The library you use to *write* the agent: the reasoning loop, the tools, the memory handling. AWS's Strands SDK, Anthropic's Claude Agent SDK, Google's ADK, and open-source frameworks like LangGraph and CrewAI all live here. This decides *how the agent thinks and acts* — and nothing about where it runs or how it is governed.

**3. The runtime / operating platform layer.** The managed infrastructure that *runs* the agent in production: isolated execution, persistent memory, identity brokering, policy enforcement, observability. AWS Bedrock AgentCore is the headline product here. Azure AI Foundry Agent Service and Google's Vertex AI Agent Engine are its true peers. This is the operating/governance plane.

**4. The development / build surface.** Where a human actually builds: a CLI, an IDE, or a low-code studio. AgentCore's CLI, the Vertex Agent Builder console, and — crucially — **Microsoft's Copilot Studio** all live here.

That last point resolves the most common headline confusion. Copilot Studio gets compared to Bedrock and AgentCore, but it is neither. It is a *build surface* — the low-code front door. Its real peer is the AgentCore CLI, not AgentCore itself. Microsoft simply leads with its build surface as the public face of its stack, while AWS leads with its runtime — so the two brands that get compared in headlines actually sit a layer apart.

### The consolidated map

| Ecosystem | Authoring SDK / Framework | Runtime / Operating Platform | Dev Tool / Build Surface | Inference Layer | Model families on that inference layer |
|---|---|---|---|---|---|
| **AWS** | Strands SDK | Bedrock **AgentCore** | AgentCore CLI/SDK + IDE; Bedrock console | **Bedrock** (proprietary + open-weight via Project Mantle) | Amazon Nova/Titan · Anthropic Claude · OpenAI GPT + Codex · Meta Llama · Mistral · Cohere · AI21 · DeepSeek · Qwen · MiniMax · Moonshot (Kimi) · GLM |
| **Microsoft / Azure** | Microsoft Agent Framework | Azure AI **Foundry Agent Service** | **Copilot Studio** (low-code) *or* VS Code + Foundry SDK | **Azure OpenAI / Foundry** | OpenAI GPT (native), Phi · Anthropic Claude · Meta Llama · Mistral · DeepSeek · Qwen |
| **Google / GCP** | ADK | Vertex AI **Agent Engine** | Vertex Agent Builder console + ADK CLI | **Vertex AI** | Gemini (native), Gemma · Anthropic Claude · Meta Llama · Mistral · partner models |
| **Anthropic** | Claude Agent SDK | *(no self-hostable platform)* | Claude Code / Cowork + SDK | **Anthropic API** | Claude only |
| **OpenAI** | Agents SDK | *(OpenAI-hosted only)* | Codex, ChatGPT | **OpenAI API** | GPT / o-series / Codex only |
| **Cross-cloud governance** | *(framework-agnostic)* | **Agent Management Platform** *(over other runtimes)* | Its own console | *(sits above inference)* | model-agnostic |
| **Open-source** | LangChain / LangGraph · CrewAI · AutoGen | *self-host; or LangSmith / LangGraph Platform* | Any IDE | BYO | any |

> *Notes:*
>
> - *Names — especially Microsoft's — and model/region availability shift frequently. Verify the specific cells you'll build on against primary docs.*
> - *Scope: this table covers **general-purpose stacks** you'd choose between to build an arbitrary application. Platform-bound vertical agents (Salesforce Agentforce, ServiceNow, Workday, etc.) are out of scope — they build agents inside their own product's data gravity, not stacks you'd pick as a general build target.*
> - *The layers aren't always as clean as the columns suggest. Most open-source frameworks are self-hosted, but the LangChain ecosystem is the exception — LangChain/LangGraph author the agent, while LangSmith (observability/evals) and LangGraph Platform (managed deployment) also cover the runtime/governance layer.*

### Two findings this map makes visible

**1. The inference layer has become a multi-vendor marketplace, so model availability is no longer a lock-in lever.** A year ago, "which models can I get" was a real reason to pick a cloud. No longer. Claude, GPT, Llama, DeepSeek, and Qwen are now reachable through all three hyperscalers. Even the assumption that OpenAI models lived only on Azure is gone — GPT-5.x and Codex went generally available on Bedrock in mid-2026 after the OpenAI–Microsoft exclusivity was dissolved. The consequence: the lock-in decision has moved *up* a layer, from inference to the runtime/governance plane. Choose your cloud on governance and ecosystem fit, and treat model selection as a per-workload dial.

**2. The model vendors ship an SDK and finished apps, but no self-hostable operating platform.** Note the runtime column for Anthropic and OpenAI — "no self-hostable platform" and "OpenAI-hosted only" respectively. They give you an authoring framework (the Agent SDK) and finished products (Claude Code, Cowork, Codex, ChatGPT), but not a managed, run-it-in-your-own-cloud platform with deterministic policy, identity brokering, and audit-grade observability. That operating plane is what you either assemble yourself or rent from a hyperscaler (AgentCore et al.) or a vendor-neutral governance layer.

> **⚠️ A note on model provenance.** The marketplace now includes Chinese open-weight families (DeepSeek, Qwen, GLM, Kimi). Hosting them on a hyperscaler keeps *inference* inside your cloud's controls, which neutralizes the most acute data-egress concern. But open weights mean the safety properties are whatever the lab baked in, and runtime guardrails wrap the *interaction*, not the *weights*. Whether to use them at all is a governance-stance call only you can make — and in some sectors it is simply ruled out regardless of how well they are hosted.

---

## Part 2 — What the Runtime / Operating Platform layer is actually *for*

The Runtime/Operating Platform layer delivers five distinct capabilities: isolation, identity brokering, policy enforcement, observability, and managed memory. Most teams treat these as a checklist — line items on an enterprise architecture review or a procurement requirement. That framing misses the point. Each exists because a specific class of real failure happens without it. And of the five, four do the same kind of job while one is fundamentally different: four are *risk controls* that bound what an agent can do — because an LLM agent is a non-deterministic actor that takes real-world actions on behalf of real users — while the fifth, memory, is an *enabling capability* that happens to be provided by the same runtime.

**The four risk controls — bounding the agent's autonomy:**

- **Isolation** contains the blast radius. The moment an agent can run code, browse, or hold secrets, it is executing semi-arbitrary actions driven by model output — and potentially by untrusted input it reads. Per-session isolation makes cross-tenant leakage and injection-driven host compromise structurally hard rather than one-bug-away.

- **Identity brokering** constrains *whose authority* the agent acts under. When an agent calls a downstream system on a user's behalf, it must act within *that user's* permissions — not as an omnipotent service account. This is the classic *confused-deputy* problem, and it is the one most likely to bite a multi-tenant application. It also preserves the audit trail compliance requires.

- **Policy** is deterministic enforcement that lives *outside* the agent's reasoning. Prompting ("never delete production data") is a request, not a guarantee. A policy engine intercepts a disallowed action *before execution*, regardless of how the model justified it — and regardless of whether the model was jailbroken or injection-manipulated.

- **Observability** is how you debug a non-deterministic, multi-step system, catch silent quality drift, produce audit evidence, and spot a runaway loop burning spend.

**The one that's a capability, not a guardrail:**

<ul><li><p><strong>Managed memory</strong> is externalized state. The model is stateless; anything the agent should "remember" past its context window has to live outside it. Without it you get amnesia, context-window overflow, and no personalization. Memory is the odd one out on this list — it's an <em>enabling capability</em> that makes a stateful, multi-session agent work, not a control that protects you. It's grouped with the runtime services because the platform provides it alongside them, but it belongs in a different category: the other four bound what the agent can <em>do</em>, while memory expands what it can <em>be</em>. (And memory is itself something you govern — it can leak across sessions, retain sensitive data, or be poisoned — so it sits partly <em>under</em> the other four, not beside them.)</p></li></ul>

### The responsibility most teams miss

Here is the trap. The frameworks make it *easy* to hand a model real tools and autonomy. But the controls that make that safe are largely *opt-in* — the unenforced path is the documented, frictionless, quickstart path, and the enforced path is an assembled-yourself afterthought.

This matters because **defaults are normative.** What ships on versus off signals what is expected. A fifteen-line "hello world" that gives a model tool access with zero enforcement is teaching every reader that this is the normal way to do it and the rest is decoration. The mature version of every other risky technology eventually flips this — browsers ship same-origin policy on, cloud buckets went private-by-default after enough public-exposure incidents. Agentic tooling is still pre-that-step. It is shipping the buckets public.

So the practical guidance for any team adopting this stuff: **assume the safe defaults are yours to install.** The vendor provides the *mechanism* (the policy engine, the identity broker, the isolation). The *policy content* — what a destructive action is in your domain, which user may touch which record, what your auditors require — is irreducibly yours, because only you hold that information. Mechanism is the vendor's job; policy is the operator's job. The failure mode is a team that doesn't realize the application-layer guardrails were theirs to build.

---

## Part 3 — The harder question: *should* a model be acting at all?

Everything above is about *how* to build and govern an agent. The more important question is whether to give it autonomy in the first place — and here a little history is clarifying.

### Two axes, not one

"AI" spans a 2×2, not a binary:

- **Output breadth:** a number in [0,1] (a fraud score) versus unbounded output (natural language, or — in agentic use — *actions*).
- **Autonomy:** the model *informs* a decision a human owns, versus the model *acts* and *drives a loop* itself.

<img src="/img/2026-06-07-image3.png" alt="The two axes of AI risk: a 2×2 of autonomy (informs vs. acts) against output breadth (narrow vs. broad). Bounded predictive models like XGBoost sit in the safe informs-narrow corner; agentic LLMs sit in the acts-broad danger corner alongside RL agents and recommender loops." style="display: block; max-width: 100%; height: auto; margin: 20px 0;">

|  | Narrow output | Broad / unbounded output |
|---|---|---|
| **Informs (no autonomy)** | XGBoost fraud scoring, credit models, classifiers | GANs, generative text/image |
| **Acts (autonomy)** | Simple rule-triggered auto-actions | **RL trading & control agents, recommender loops — and now agentic LLMs** |

The "acts-broad" cell is where the heavyweight control plane is needed — and **it was occupied for years before LLMs.** Reinforcement-learning agents in algorithmic trading, planetary-scale bandit systems in ad real-time bidding, recommender loops in streaming and social feeds, dynamic pricing, network routing, datacenter control — all of these were learned policies taking consequential autonomous actions in feedback loops. The entire discipline of *safe RL* — action constraints, kill-switches, human-in-the-loop overrides — exists because the field already learned you cannot let an opaque learned policy act unconstrained.

So the popular story that "autonomous AI is new and we have no precedent" is wrong. We have a decade of precedent. What is genuinely new is that LLMs made the dangerous quadrant *cheap and easy to enter* — a few lines of SDK code, no RL expertise required — and added new attack surfaces (hallucination, prompt injection) that controlled RL environments largely didn't face.

### The principle the history actually teaches

Look at *where* autonomous AI got deployed versus where it was deliberately withheld. Ad tech, recommenders, pricing, and routing deployed it freely. Healthcare treatment policies and most industrial control were researched extensively but *kept human-gated.*

The dividing line was never capability. It was **reversibility and cost-per-action.** Cheap, reversible, high-volume actions — where a bad action is survivable and learnable-from — got autonomy with light controls. Expensive, irreversible actions — where a single bad action is catastrophic — either cleared an overwhelming control bar or stayed human-in-the-loop. A decade of deployment is essentially a natural experiment confirming that principle.

### So what changed with LLMs — really?

Here is the uncomfortable part. On the dimension that actually gated RL deployment — *can I bound this thing's behavior well enough to trust it with irreversible consequences* — **almost nothing has improved, and arguably it got harder.** LLMs are less inspectable than a defined RL policy, carry new failure modes RL didn't, and remain formally unverifiable.

What changed is **generality, accessibility, and broader competence per unit of effort** — none of which is the same as *trustworthiness for irreversible actions.* Broader competence with an unchanged failure profile is, if anything, more dangerous, because it invites trust across a wider surface. There is one real improvement on the safety side — better external scaffolding (approval gates, structured output, the control plane) — but that is a *cage around* an untrusted model, not a more trustworthy model.

And there is a genuinely new calibration hazard: RL agents were *honestly* opaque — nobody mistook a Q-function for a colleague. An LLM's articulate, fluent rationalization *looks* like trustworthy judgment and isn't. Fluency is not reliability, but humans are wired to read it that way.

### The decision rule

This leads to a clean rule for deploying agentic systems, and it is the one to take into any architecture review:

> **The question is not "how capable is the model." It is "what is the cost and reversibility of the actions I am letting it take" — and that determines how much of the control plane you actually need.**

- An agent **drafting text or proposing options** (cheap, reversible, human owns the commitment) needs little. This is decision support with a faster drafting step — not the dangerous quadrant at all.
- An agent **moving money, deleting records, or changing access** (expensive, irreversible) needs the full apparatus — or, more honestly, should usually have a human between the decision and the consequence.

The responsible deployments are precisely the ones that *don't require solving the unsolved problem*: reversible/cheap actions, human-in-the-loop, or actions caged so tightly by a deterministic control plane that the model's unreliability can't reach anything irreversible. The irresponsible ones quietly bet that fluency and benchmark scores mean the irreversible-action problem is solved. It isn't.

So when someone proposes an LLM agent for a consequential, irreversible role, the right challenge is not "how good is the model." It is: **"what changed about your ability to bound or reverse its actions?"** If the answer is "the control plane" — good, let's inspect the cage. If the answer is "the model is just really good now" — that is the RL-era mistake in better language, and a decade of deliberate non-deployment in high-consequence domains is the evidence that capability was never the gating variable.

---

## What to take away

1. **Know your layer.** Inference, authoring framework, runtime/operating platform, build surface. Most "X vs Y" debates evaporate once you place each product in its layer.
2. **Model choice is no longer the lock-in decision.** It moved up to the governance plane. Pick the cloud on ecosystem and governance fit.
3. **The safe defaults are yours to install.** Vendors ship the mechanism; you own the policy content. Don't let an opt-in safety story become an unsafe baseline.
4. **Govern in proportion to autonomy and consequence — not model type.** A bounded predictive model and an autonomous action-taking agent are different risk profiles, and they always were.
5. **The deployment gate is reversibility and cost-per-action, not capability.** This is the most durable principle in the whole field, learned the hard way over a decade and worth refusing to un-learn.

The capability is real and the opportunity is real. But the maturity move — the thing that separates teams that deploy this well from teams that get burned — is treating the model as a capable, fallible component to be bounded and verified, not a trustworthy actor to be turned loose. Govern proportionally to what an action *costs* if it goes wrong, and you will deploy the safe cases fast and keep a human between the model and the cliff edge for the rest.
