import time
import itertools

from app import app, save_file
from flask import render_template, request, redirect

@app.route('/puzzles/1/part-one', methods=["GET", "POST"])
def puzzle_one_one():
    if request.method == "POST":
        start = time.time()

        filepath = save_file(request.files["input"])
        if filepath == False:
            return 'No input given... Quite the puzzle ey?'

        # Parse all lines to integers, (effectively removing + signs, but keeping int's signed)
        list = [int(line) for line in open(filepath)]
        # Sum just adds up an array
        solution = sum(list)

        return render_template("puzzles/one_one.html", solution=solution, time=time.time() - start)

    return render_template("puzzles/one_one.html")

@app.route('/puzzles/1/part-two', methods=["GET", "POST"])
def puzzle_one_two():
    if request.method == "POST":
        start = time.time()

        filepath = save_file(request.files["input"])
        if filepath == False:
            return 'No input given... Quite the puzzle ey?'

        # Parse all lines to integers, (effectively removing + signs, but keeping int's signed)
        list = [int(line) for line in open(filepath)]

        current = 0
        seen = set()
        for x in itertools.cycle(list):
            current += x

            if current in seen:
                return render_template("puzzles/one_two.html", solution=current, time=time.time() - start)

            seen.add(current)

            # 2million seen length should be ample, if not, the list is probably faulty
            if len(seen) > 2000000:
                return render_template("puzzles/one_two.html", solution=None)

    return render_template("puzzles/one_two.html")