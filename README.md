# subsets

Create speech-to-text datasets from subtitles.

## Installation

```python
git clone https://github.com/benjcunningham/subsets
cd subsets
python setup.py install
```

## Getting Started

```bash
subsets \
    --subs "my_subs.srt"t \
    --audio "my_audio.ogg" \
    --path "output/path/" \
    --format "ogg" \
    --prefix "my_dataset" \
    --encoding "utf-8-sig"
```
