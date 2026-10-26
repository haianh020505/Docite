# evals — Offline Quality Evaluation

Separate from unit tests. Measures AI pipeline quality on golden datasets.

**Belongs here:** datasets (synthetic Q&A only), metric scripts, evaluation runner, reports.
**Must NOT go here:** real tenant documents, real organization names, pytest unit tests, or any production secrets.

## Metrics tracked
- Retrieval Hit@k (does the correct chunk appear in top-k?)
- Citation correctness (file name + page matches ground truth)
- No-source accuracy (correctly abstains when answer is absent)
- Cross-tenant leak check (Org A's question never retrieves Org B's chunks)

## Run
```powershell
cd evals
python run_eval.py
# Reports saved to evals/reports/ (gitignored)
```
