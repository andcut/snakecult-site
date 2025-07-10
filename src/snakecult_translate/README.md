# snakecult_translate

A modular translation toolkit tailored for Hugo-based static sites.
It lets you translate Markdown content into **any target language** using
OpenAI models, with three workflow styles:

| Mode | Script | When to use |
|------|--------|-------------|
| **Single** | `cli_one.py` | One-off file or ad-hoc tests |
| **Parallel** | `cli_parallel.py` | Translate many small files concurrently via regular Chat Completions; good for < 10–20 docs |
| **Batch Async** | `cli_batch_async.py` | Uses OpenAI *Batch API* ― 50 % cheaper, best for dozens / hundreds of files |

---

## 0. Prerequisites

```bash
pip install -r requirements.txt
# put your key in either:
#   • .env.translation   (OPENAI_API_KEY=sk-...)
#   • or as an environment variable OPENAI_API_KEY
```

## 1. Quick recipes

Translate a single file in place:
```bash
python -m src.snakecult_translate.cli_one content/posts/foo.md
```

Translate every Markdown under `content/` into French (as an example), **in parallel**:
```bash
python -m src.snakecult_translate.cli_parallel --src-root content \
       --dst-root content/fr --model gpt-4o --limit 100
```

### Batch API (cheap!)
Create a long-running job at OpenAI and wait until it finishes:
```bash
python -m src.snakecult_translate.cli_batch_async --chunk --chunk-size-chars 25000
```
* Flags of interest*
* `--limit N` Only submit first N (largest) files
* `--no-wait` Submit and exit – you can come back later with `--resume`
* `--resume --batch-id batch_xyz` Download results & assemble Markdown

## 2. Tracking your jobs

The script stores a mapping file for each submission in **batch_work/**:
```
batch_work/
  batch_batch_<batch_id>_mapping.json
```

To see how those jobs are doing:
```bash
python -m src.snakecult_translate.cli_batch_status           # one-shot snapshot
python -m src.snakecult_translate.cli_batch_status --watch   # live updating
python -m src.snakecult_translate.cli_batch_status --assemble   # auto-download completed jobs
```

`cli_batch_status` is non-destructive; by default it only reads job status.
When `--assemble` is provided, it will call the underlying `cli_batch_async`
with `--resume` to pull the finished translations.

---

## 3. Example workflow

```bash
# 1. Submit a big batch and leave (don't block)
python -m src.snakecult_translate.cli_batch_async --chunk --no-wait

# 2. Go for coffee ☕️

# 3. Later, check progress and automatically download if done
python -m src.snakecult_translate.cli_batch_status --assemble

# 4. Review translated posts under content/fr/, commit, push, etc.
```

---

## 4. Implementation notes
* **Chunking** – Files > `--chunk-size-chars` are split and recombined with
  `<!-- CHUNK BREAK -->` separators after translation.
* **Cost estimation** – Utilities in `utils.py` let you approximate token
  counts and USD cost before you hit the API.
* **Polling** – Batch jobs are polled every 30 s (configurable) when
  `--resume` is used.

Feel free to tweak or expand; this README is meant to be a living doc. 