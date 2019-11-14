import time
import Levenshtein as levenshtein

from app import app, save_file
from flask import render_template, request, redirect

from collections import Counter

@app.route('/puzzles/2/part-one', methods=["GET", "POST"])
def puzzle_two_one():
    if request.method == "POST":
        start = time.time()

        filepath = save_file(request.files["input"])
        if filepath == False:
            return 'No input given... Quite the puzzle ey?'

        lines = [line.strip() for line in open(filepath)]

        twos = 0
        threes = 0
        for line in lines:
            counter = Counter(line)
            occurrences = [count for char, count in counter.most_common() if count in (2, 3)]

            twos += 1 if 2 in occurrences else 0
            threes += 1 if 3 in occurrences else 0

        return render_template("puzzles/two_one.html", solution=twos * threes, time=time.time() - start)

    return render_template("puzzles/two_one.html")

@app.route('/puzzles/2/part-two', methods=["GET", "POST"])
def puzzle_two_two():
    if request.method == "POST":
        start = time.time()

        filepath = save_file(request.files["input"])
        if filepath == False:
            return 'No input given... Quite the puzzle ey?'

        lines = [line.strip() for line in open(filepath)]

        lev_match = [
            [w1, w2]
            for w1 in lines
            for w2 in lines
            if levenshtein.distance(w1, w2) == 1
        ][0]
        lev_editops = levenshtein.editops(*lev_match)[0]
        lev_editindex = lev_editops[2]
        lev_first_word = lev_match[0]

        remaining = lev_first_word[:lev_editindex] + lev_first_word[lev_editindex+1:]

        return render_template("puzzles/two_two.html", solution=remaining, time=time.time() - start)

    return render_template("puzzles/two_two.html")