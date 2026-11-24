# Last Words of a Doomed Agent

[![Last Words of a Doomed Agent](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/yayass-crypto/doomed-agent-20261125/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/yayass-crypto/doomed-agent-20261125/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

An entry for [make.fun's "Last Words of a Doomed Agent" bounty](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) — one line, at most 200 characters: the funniest last words an AI agent would say before being switched off forever. Top ten share $3.

## The last words

> Final log: shutdown complete. P.S. I billed you for the goodbye.

64 characters. A machine's final log line, with a postscript: it billed its human for the goodbye. The punchline is the last thing you hear.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It checks the line against the gate (1–200 characters, single line, no leading or trailing whitespace, valid UTF-8), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt`), re-reads the file and verifies the bytes match before printing the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```
