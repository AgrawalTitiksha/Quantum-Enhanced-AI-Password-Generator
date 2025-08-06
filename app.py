from flask import Flask, jsonify, request
from quantum.quantum_random import generate_quantum_bits
from utils.helpers import binary_to_seed, get_charset
from ai.password_ai import generate_password

app = Flask(__name__)

@app.route('/generate_password', methods=['GET'])
def generate():
    # User input
    length = int(request.args.get('length', 12))
    use_upper = request.args.get('uppercase', 'true').lower() == 'true'
    use_lower = request.args.get('lowercase', 'true').lower() == 'true'
    use_numbers = request.args.get('numbers', 'true').lower() == 'true'
    use_symbols = request.args.get('symbols', 'true').lower() == 'true'

    charset = get_charset(use_upper, use_lower, use_numbers, use_symbols)

    if not charset:
        return jsonify({'error': 'Character set is empty. Please select at least one option.'}), 400

    qbits = generate_quantum_bits()
    seed = binary_to_seed(qbits)
    password = generate_password(seed, length, charset)

    return jsonify({
        'generated_password': password,
        'quantum_seed_bits': qbits,
        'seed': seed
    })

if __name__ == '__main__':
    app.run(debug=True)
