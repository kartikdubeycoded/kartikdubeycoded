<h1 align="center">Kartik Dubey</h1>

<p align="center">
  <b>AI / GenAI engineer — RAG, multi-agent systems, and the plumbing that makes them hold up.</b><br>
  Final-year B.Tech Data Science · Navi Mumbai, India
</p>

<p align="center">
  <a href="https://portfolio-ed-a79.pages.dev"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-6FE7CE?style=for-the-badge&logo=firefox&logoColor=0b0b0b"></a>
  <a href="https://linkedin.com/in/kartik-dubey-80b100293"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yMC40NDcgMjAuNDUyaC0zLjU1NHYtNS41NjljMC0xLjMyOC0uMDI3LTMuMDM3LTEuODUyLTMuMDM3LTEuODUzIDAtMi4xMzYgMS40NDUtMi4xMzYgMi45Mzl2NS42NjdIOS4zNTFWOWgzLjQxNHYxLjU2MWguMDQ2Yy40NzctLjkgMS42MzctMS44NSAzLjM3LTEuODUgMy42MDEgMCA0LjI2NyAyLjM3IDQuMjY3IDUuNDU1djYuMjg2ek01LjMzNyA3LjQzM2MtMS4xNDQgMC0yLjA2My0uOTI2LTIuMDYzLTIuMDY1IDAtMS4xMzguOTItMi4wNjMgMi4wNjMtMi4wNjMgMS4xNCAwIDIuMDY0LjkyNSAyLjA2NCAyLjA2MyAwIDEuMTM5LS45MjUgMi4wNjUtMi4wNjQgMi4wNjV6bTEuNzgyIDEzLjAxOUgzLjU1NVY5aDMuNTY0djExLjQ1MnpNMjIuMjI1IDBIMS43NzFDLjc5MiAwIDAgLjc3NCAwIDEuNzI5djIwLjU0MkMwIDIzLjIyNy43OTIgMjQgMS43NzEgMjRoMjAuNDUxQzIzLjIgMjQgMjQgMjMuMjI3IDI0IDIyLjI3MVYxLjcyOUMyNCAuNzc0IDIzLjIgMCAyMi4yMjIgMGguMDAzeiIvPjwvc3ZnPg%3D%3D"></a>
  <a href="mailto:kartikdubey1934@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a>
</p>

---

## What I do

I build retrieval and agent systems end to end — the spec, the architecture and the code come from
the same person. Most of what I ship runs **offline or at zero external API cost**, because the
problems I've worked on were air-gapped or personal-data-sensitive.

I also build the evaluation in from the start. Signer-independent cross-validation, Recall@5
tracking, test suites — a number I can't reproduce isn't a number I'll quote.

**Currently:** final-year B.Tech, open to AI / GenAI engineering roles and freelance work.

---

## Selected work

### 🧠 Project Jay — the orchestration layer
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![DeepSeek v4](https://img.shields.io/badge/DeepSeek%20v4-4D6BFE?style=flat-square&logo=deepseek&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![private](https://img.shields.io/badge/private_repo-6E7681?style=flat-square)

The system I run my other projects through. Work is dispatched to rooms, each with a manager
seat and implementation workers, and **the model is chosen per role, not per person**:
DeepSeek v4 Pro builds and reviews, `deepseek-reasoner` manages, v4 Flash does the cheap
graph and summarisation work. Room task envelopes are bounded, so a worker's full transcript
never enters a manager's context — which is what stops a long build from silently becoming a
context-window problem.

Underneath it is a state layer that had to be made honest the hard way. A session row read
`RUNNING` for 39 days because nobody ever wrote a new value; liveness is now **derived at read
time**, never stored. Token spend is counted from real transcript `usage`, deduped by message
id — one API message spans several log lines, and counting each one triples the bill.

**55 test modules. Native components run subprocess-isolated**, so a crash costs one utterance
and never the control plane.

> Repo is private — it ingests my personal notes. Happy to walk through the architecture.

### 🔎 [Agentic RAG Engine](https://github.com/kartikdubeycoded/agentic-rag-engine)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)

Grounded Q&A over technical manuals. An open-source rebuild of the offline agentic-RAG architecture
I shipped to a client at TCS, re-targeted to public Wärtsilä 32 marine-engine manuals so the whole
thing is publicly runnable. Rewrite → route → retrieve → grade over an embedded Qdrant index with
cross-encoder reranking and an optional Neo4j cascade-fault graph. **Every answer is
citation-grounded — never invented.** Five-step quickstart; no Docker, no GPU.

### 📚 [Get Your Knowledge Right](https://github.com/kartikdubeycoded/getyour-kb-right)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![faster--whisper](https://img.shields.io/badge/faster--whisper-412991?style=flat-square)

A personal knowledge engine that turns the firehose you already read into decisions you act on.
Watches repos, papers, news and launches, ranks them against your topics, and pushes a digest to
your phone. Share a reel and it transcribes locally, researches it, and returns a do/skip verdict.
The point isn't more to read — it's **less to read and something to do.**

### 🎯 Get Your Leads Right
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Node 22](https://img.shields.io/badge/Node%2022-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![private](https://img.shields.io/badge/private_repo-6E7681?style=flat-square)

Turns a business's public digital footprint into a defensible reason to make a specific phone
call. The rule the whole system enforces **in code** is *no receipt, no claim*: every fact
carries a provenance tier and a source URL, there is no path that writes an attribute without
one, and a fact nobody published is `null` rather than `false`. Deterministic scrapers with
robots enforcement feed a provenance graph; a rubric turns signals into a fit score with a
written reason. **145 tests, and zero LLM calls in the collection layer** — a rerun produces
the same records, so a bad parse is a bug you fix rather than a temperature you tune.

> Private — it holds real businesses' contact data.

### 💼 Get Your Job Right
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square)
![crawl4ai](https://img.shields.io/badge/crawl4ai-6E4AFF?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-000000?style=flat-square&logo=modelcontextprotocol&logoColor=white)
![private](https://img.shields.io/badge/private_repo-6E7681?style=flat-square)

The same idea pointed at my own pipeline: sweep listings across boards and company portals,
rank them against a profile, draft the application, and track what actually happened to each
one. Exposes an MCP server so the drafting step can query the pipeline instead of being handed
a pasted job description.

> Private — it holds my applications and other people's contact details.

### 🤟 [Talk Through Me](https://github.com/kartikdubeycoded/TTM-Talk-Through-Me)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=flat-square&logo=mediapipe&logoColor=white)
![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-4285F4?style=flat-square&logo=googlechrome&logoColor=white)

Live sign-language → English captions on Meet / Zoom / Teams, as a Chrome extension that runs
entirely in the browser — webcam video never leaves the machine. Evaluated under **5-fold
signer-independent cross-validation** (no signer appears in both train and test): a **128-sign
shippable vocabulary at 0.64 mean per-sign accuracy**, 115 of 128 signs clearing a 0.50 floor.

---

## Also here

**[nucdesal](https://github.com/kartikdubeycoded/nucdesal)**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)  
Could India's planned 100 GW nuclear fleet desalinate seawater with its reject heat? A cited physics model, 415 tests, every reference number independently re-derived — five didn't hold up.

**[real-estate-splat](https://github.com/kartikdubeycoded/real-estate-splat)**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Node%2022](https://img.shields.io/badge/Node%2022-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white) ![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)  
3D walkthroughs of flats from an ordinary phone — IMU pose + monocular metric depth + fusion, then a three.js viewer. 137 tests.

**[Paper World](https://github.com/kartikdubeycoded/paper-world)**  
![Node%2022](https://img.shields.io/badge/Node%2022-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white) ![Binance](https://img.shields.io/badge/Binance-F0B90B?style=flat-square&logo=binance&logoColor=white)  
15 paper-trading agents on live Binance data, with a planted control group so the swarm's "learning" is falsifiable.

**[Get Your Hands Right](https://github.com/kartikdubeycoded/get-your-hands-right)**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white) ![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=flat-square&logo=mediapipe&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)  
Inspect a 3D model with your bare hands via webcam — MediaPipe landmarks drive rotate/scale/place, plus a real-time filter stack.

**[BUDDY](https://github.com/kartikdubeycoded/BUDDY)**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![OpenSCAD](https://img.shields.io/badge/OpenSCAD-F9D72C?style=flat-square&logo=openscad&logoColor=black)  
Ducted-fan aircraft engineering rig — parametric OpenSCAD CAD plus Python propulsion, structural and mass solvers, behind a build-readiness gate.

**[facelessVideos](https://github.com/kartikdubeycoded/facelessVideos)**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white) ![faster--whisper](https://img.shields.io/badge/faster--whisper-412991?style=flat-square)  
Script → voice → B-roll → subtitles → rendered 9:16 short, end to end.

**[Repair Chatbot](https://github.com/kartikdubeycoded/repair-chatbot)**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B4A?style=flat-square)  
Offline RAG over 18,995 repair manuals — the earlier, simpler ancestor of the Agentic RAG Engine.

**[Portfolio](https://github.com/kartikdubeycoded/portfolio-ed-)**  
![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white) ![GSAP](https://img.shields.io/badge/GSAP-88CE02?style=flat-square&logo=greensock&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)  
Cinematic scroll-driven personal site — [live](https://portfolio-ed-a79.pages.dev).

**[ugh-boardroom](https://github.com/kartikdubeycoded/ugh-boardroom)**  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white)  
UI prototype: a multi-agent boardroom where four personas deliberate a decision.

---
## Experience

**Tata Consultancy Services** — AI Systems & Automation · *Jan – Apr 2026*
Shipped an air-gapped agentic RAG assistant to **350+ fab engineers** at an offshore semiconductor
client, replacing 10,000+ pages of OEM manuals and cutting troubleshooting from ~40 min to <10 min
per incident, at zero external LLM API cost. **Recall@5: 0.61 → 0.89.**

**Reliance Jio** — Data Science Intern, Network Analytics · *Jun – Jul 2025*
Churn models across 20+ cohorts drawn from a **440M-record** base (0.838 ROC-AUC, XGBoost);
distributed EDA over 200+ variables in Spark.

---

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./profile-3d-contrib/profile-night-green.svg">
  <source media="(prefers-color-scheme: light)" srcset="./profile-3d-contrib/profile-green.svg">
  <img alt="Contribution graph" src="./profile-3d-contrib/profile-green.svg">
</picture>

---

<p align="center">
  <a href="https://portfolio-ed-a79.pages.dev">portfolio</a> ·
  <a href="https://linkedin.com/in/kartik-dubey-80b100293">linkedin</a> ·
  <a href="mailto:kartikdubey1934@gmail.com">kartikdubey1934@gmail.com</a>
</p>

<p align="center"><sub>last boot <!--BOOT:START-->28 Aug 2026, 08:25 ist<!--BOOT:END--></sub></p>
