"""
Usage: python converter.py [--inp="DP.tsv"] [--mode="xml"] run
"""

import json
from pathlib import Path

from fire import Fire
import pandas as pd

from src import __root__
from _models import Row, Word
from _writer import TSVWriter, PKLWriter, XMLWriter


class Converter:
    def __init__(self, inp="*.tsv", mode="tsv"):
        self.inp = Path.joinpath(__root__, "inp", "converter").glob(inp)
        self.filter = json.load(
            Path.joinpath(__root__, "conf", "filter.json").open(encoding="utf-8")
        )
        self.mode = mode

        if self.mode == "tsv":
            self.writer = TSVWriter
        elif self.mode == "pkl":
            self.writer = PKLWriter
        elif self.mode == "xml":
            self.writer = XMLWriter
        else:
            raise ValueError("--mode should be set to any of: 'tsv', 'pkl', or 'xml'")

    def run(self):
        for filename in self.inp:
            df = pd.read_csv(filename, sep="\t", header=None, na_filter=False)

            if self.filter:
                df = df[
                    eval(
                        " & ".join(
                            f"df[{idx}].isin({self.filter[idx]})" for idx in self.filter
                        )
                    )
                ]

            with self.writer(
                Path.joinpath(
                    __root__,
                    "out",
                    "db" if self.mode == "pkl" else f"{filename.stem}.{self.mode}",
                )
            ) as out:
                for idx, row in df.iterrows():
                    row = Row(row.map(str.strip).to_list())
                    word = Word(filename.stem, idx, row.word, row.ana)

                    if self.mode == "tsv":
                        out.write(row.src, word.pos, *word.ana, word.lemma)
                    elif self.mode == "pkl":
                        out.write(word.reg, word.msd.pickled)
                    else:
                        out.write(row)


if __name__ == "__main__":
    Fire(Converter)
