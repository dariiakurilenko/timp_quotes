import random

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

quotes = [
    "Жизнь — это то, что происходит, пока вы строите другие планы. — Джон Леннон",
    "Единственный способ сделать отличную работу — это любить то, что вы делаете. — Стив Джобс",
    "Будьте тем изменением, которое хотите видеть в мире. — Махатма Ганди",
    "Сложности — это просто возможность проявить свою силу. — Аноним",
    "Успех — это не окончание, неудача — это не фатально: важно лишь мужество продолжать. — Уинстон Черчилль",
    "Не отступай перед трудностями. Смотри им прямо в лицо. Смотри, пока не одолеешь их. ",
    "Живи так, словно читаешь книгу. И люби так, словно читаешь стихи. ",

]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quote', methods=['GET'])
def get_quote():

    quote = random.choice(quotes)
    return jsonify({"quote": quote})


@app.route('/quote', methods=['POST'])
def add_quote():

    data = request.get_json()


    if 'quote' not in data:
        return jsonify({"error": "Цитата отсутствует."}), 400


    new_quote = data['quote']
    quotes.append(new_quote)

    return jsonify({"message": "Цитата добавлена!", "quote": new_quote}), 201


if __name__ == '__main__':
    app.run(debug=True)
