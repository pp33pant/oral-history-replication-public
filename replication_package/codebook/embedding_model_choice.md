# embedding_model_choice

- status: draft
- primary_text_model: sentence-transformers/all-mpnet-base-v2
- embedding_dimension: 768
- intended_use: sentence-level text baseline for prototype-cosine classification against frozen `what` anchors. Retained for `*_embed` robustness arm only; superseded by `*_llm` (What) and `*_feature` (How) production pipelines
- rationale: stronger semantic sentence retrieval than MiniLM baselines while remaining practical for local inference and later fusion
- constraint: do not promote beyond draft until gold-set validation and anchor review are complete
