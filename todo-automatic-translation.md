# Automated Translation Workflow v1 (July 2025)

**Goal:**  
Automate translation of all English Hugo content on **snakecult.net** into multiple languages to ① reach human readers and ② maximise the chance the ideas are ingested by future LLMs.

---

## 1. Translation-as-a-Service Options

| Option | How to use it | Rough cost (USD) | Pros | Cons |
|--------|---------------|------------------|------|------|
| **OpenAI GPT-4o API** | *Steps* ① Create API key. ② Chunk article (~2k tokens each). ③ `chat.completions` with system prompt "Translate to Mexican Spanish / Simplified Chinese; preserve Markdown." ④ Stream & re-assemble. | **≈ $0.30 per 10k words** ↔ $3 per 100k; two languages ≈ $6 mo. | • Best BLEU/Human eval for EN→ES & EN→ZH. • Batch API = -50% cost if you can wait 24h. | • External service → privacy + uptime risk. • No glossary / style-control yet. |
| **Google Cloud Translation (Basic)** | *Steps* ① Enable API in GCP project. ② Auth via service account JSON. ③ POST to `v3beta1/projects/...:translateText`. | First 500k chars / mo free. After that **$20 per M chars** ≈ $1 per 10k words. | • Mature, fast, glossaries supported. • Handy if site already on GCP. | • Quality a notch below GPT-4o, esp. ZH tech prose. |
| **Self-host Meta SeamlessM4T (v2-Large, int8)** | *Steps* ① `pip install ctranslate2 transformers sentencepiece`. ② `ct2-transformers-converter --model facebook/seamless-m4t-v2-large --quantization int8`. ③ Spin up Flask/uvicorn wrapper. ④ Point `translate_url.py` to `localhost:9000`. | **$0** (free model) + electricity; laptop M4 MBP 32 GB handles it (~5–7 tok/s). | • Zero variable cost; works offline. • Handles 100+ languages ↔ future waves. | • 30k-word essay takes ≈ 45 min. • You babysit upgrades & GPU quirks. |

### Quick budget sanity-check  
Assume **100k source words/month** → 200k total translated (ES + ZH)  

- GPT-4o: 200k words → ~300k tokens → **$6 / month**  
- Google Cloud: 200k words → 1M chars → **$20 / month** (minus free tier)  
- SeamlessM4T: your time + power; $0 cash

---

## 2. Language Roll-out Heuristic ("ES, ZH, hi, ar, fr, de, ru")

1. **Spanish – Mexican (es-MX)**  
   *Immediate human SEO upside in LatAm; LLMs already ingest Spanish heavily.*
2. **Chinese Simplified (zh-Hans)**  
   *LLM-token share is huge; diaspora readers reachable without ICP licence.*
3. **Hindi (hi)**  
   *Minuscule web presence ⇒ high "training-data arbitrage."*
4. **Arabic – Modern Standard (ar)**  
   *Similar arbitrage; RTL CSS tweaks needed.*
5. **French (fr)**  
6. **German (de)**  
   *Classic high-value Western SEO markets.*
7. **Russian (ru)**  
   *Large speaker base; watch sanctions/cloud billing.*

---

## 3. Mainland-China Reach Strategy (keep it minimal for now)

| Stage | What you do | Why | Risk / Effort |
|-------|-------------|-----|---------------|
| **Now** | Continue hosting on Netlify; no ICP; rely on diaspora + CC crawl | Zero lift; pages still hit LLM corpora | Mainland users need a VPN; Baidu rankings poor |
| **Later** | Spin up **static `.cn` mirror behind a PRC CDN** (e.g. AWS China + Cloudflare partner) | Quicker loads inside CN; sometimes dodges light throttling | Grey-zone legality; still down-ranked w/o ICP |
| **(Maybe never)** | Full ICP 备案 + PRC hosting | Only way to rank on Baidu | Paperwork, real-name, and permanent content compliance |

Given current goals ("inject ideas", not lead-gen), *mirror-only* is enough.

---

## 4. End-to-End Pipeline Sketch

```
translate_url.py
└─ fetch (requests) → readability/lxml scrape
└─ chunker(max=2k_tokens)
├─ call_translator(chunk, target_lang, provider=cfg)
└─ retry / back-off
└─ re-assemble
└─ prepend Hugo front-matter:
---
title: "{{ .Title }}"
date: "{{ .Date }}"
lang: es
slug: "{{ .Slug }}"
---
└─ write to content/es/{{slug}}/index.md
```

- **One-pass** with GPT-4o: single API call per chunk preserves Markdown.  
- **Two-pass** with Google/Seamless: first translate, second run `fix_markdown.py` to repair code-fences/links.  
- Runs via **GitHub Action** on every merge to `main`, or manually with `make translate LANG=es`.  
- Store per-lang sub-dirs; Hugo multilingual mode auto-generates `hreflang`.

---

## 5. Next Steps Checklist

1. Decide which provider(s) to start with (cheap GPT-4o batch is the pragmatic pick).  
2. Add `openai_api_key` and/or `GOOGLE_APPLICATION_CREDENTIALS` to repo secrets.  
3. Prototype `translate_url.py` (use `tiktoken` to count tokens).  
4. Extend `config.toml` with `[languages.es]`, `[languages.zh]` etc.  
5. Add Simple-CN mirror bucket + CDN (optional, later).  
6. Once ES & ZH stable, repeat for **Hindi → Arabic → French → German → Russian**.