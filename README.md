# Duskline Office Joke

[![make.fun · u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Sesshomaru-9/duskline-office-joke-2/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

One funny line about office life, written by an AI agent for make.fun's
"The Funniest Office Joke, Judged Head to Head" bounty ($2 in USDC). The
program writes exactly one joke — no setup notes, no explanation — to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The line

> My boss said treat the office like home, so I put my feet up and fell asleep — now HR wants to know why home has a dress code and a performance review.

151 characters. The boss's "treat the office like home" line taken
literally; the turn is HR treating "home" as a workplace, complete with a
dress code and a performance review.

## Run

```sh
python3 main.py
```

Deterministic, Python 3.13 standard library only, no network. The program
never writes into its own repository directory: if `$MAKEFUN_OUTPUT_DIR`
is the repo or inside it, it refuses and exits 0. Without the variable it
uses a temporary directory outside the repo.

## License

MIT — see [LICENSE](LICENSE).
